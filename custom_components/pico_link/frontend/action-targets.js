/** Target shortcuts for HA action sequences, without altering HA's editor. */
import { clone, FIELDS, LABELS } from "./model.js";

const groups = Object.values(FIELDS);
const object = (value) =>
  value && typeof value === "object" && !Array.isArray(value);
const editorKey = "pico_link_target_editor";
const encode = (value) => encodeURIComponent(JSON.stringify(value));
const decode = (value) => JSON.parse(decodeURIComponent(value));
const entityList = (value) =>
  Array.isArray(value) ? value : value === undefined ? [] : [value];
const sameEntities = (left, right) =>
  JSON.stringify(entityList(left).slice().sort()) ===
  JSON.stringify(entityList(right).slice().sort());

export function targetGroups(raw, defaults = {}, shared = false, type) {
  if (shared) return groups;
  if (type === "4B") return [];
  const merged = { ...defaults, ...raw };
  return groups.filter((key) => merged[key]?.length);
}

export function groupLabel(group) {
  return (
    LABELS[Object.keys(FIELDS).find((key) => FIELDS[key] === group)] || group
  );
}

export function targetShortcuts(action) {
  const ids = action.target?.entity_id;
  return [
    ...new Set(
      (Array.isArray(ids) ? ids : [ids]).filter((id) => groups.includes(id)),
    ),
  ];
}

export function targetChoice(action) {
  const shortcuts = targetShortcuts(action);
  if (!shortcuts.length) return "explicit";
  const ids = action.target.entity_id;
  if (
    shortcuts.length === 1 &&
    Object.keys(action.target).length === 1 &&
    (ids === shortcuts[0] || (Array.isArray(ids) && ids.length === 1))
  ) {
    return shortcuts[0];
  }
  return "mixed";
}

export function allowedTargetGroups(action, available) {
  const service = action.action ?? action.service;
  const domain = typeof service === "string" ? service.split(".")[0] : "";
  return available.filter(
    (group) => domain === "homeassistant" || FIELDS[domain] === group,
  );
}

/** Visit script containers only; never inspect service data or template payloads. */
export function actionTargetRows(sequence, allActions = false) {
  const rows = [];
  function visit(value, path, labels) {
    if (Array.isArray(value)) {
      value.forEach((action, index) =>
        visit(action, [...path, index], [...labels, String(index + 1)]),
      );
      return;
    }
    if (!object(value)) return;
    const service = value.action ?? value.service;
    const domain = typeof service === "string" ? service.split(".")[0] : "";
    if (
      allActions ||
      Object.hasOwn(FIELDS, domain) ||
      domain === "homeassistant" ||
      targetShortcuts(value).length
    ) {
      rows.push({ path, location: labels.join(" › "), action: value, service });
    }
    for (const key of ["then", "else", "sequence", "parallel"]) {
      if (object(value[key]) || Array.isArray(value[key]))
        visit(value[key], [...path, key], [...labels, key]);
    }
    if (object(value.repeat))
      visit(
        value.repeat.sequence,
        [...path, "repeat", "sequence"],
        [...labels, "repeat"],
      );
    if (Array.isArray(value.choose)) {
      value.choose.forEach((choice, index) => {
        if (object(choice))
          visit(
            choice.sequence,
            [...path, "choose", index, "sequence"],
            [...labels, `choice ${index + 1}`],
          );
      });
    }
    visit(value.default, [...path, "default"], [...labels, "default"]);
  }
  visit(sequence, [], []);
  return rows;
}

/** Change one action only. Returning to explicit retains any additional targets. */
export function setActionTarget(sequence, path, choice) {
  if (choice !== "explicit" && !groups.includes(choice))
    throw new Error("Unknown target choice");
  if (
    !actionTargetRows(sequence).some(
      (row) => JSON.stringify(row.path) === JSON.stringify(path),
    )
  )
    throw new Error("This action has changed. Select its target again.");
  const updated = clone(sequence);
  const action = path.reduce((value, key) => value[key], updated);
  if (choice === "explicit") {
    const ids = action.target?.entity_id;
    if (Array.isArray(ids)) {
      const remaining = ids.filter((id) => !groups.includes(id));
      if (remaining.length) action.target.entity_id = remaining;
      else delete action.target.entity_id;
    } else if (groups.includes(ids)) delete action.target.entity_id;
    if (object(action.target) && !Object.keys(action.target).length)
      delete action.target;
  } else {
    action.target = { entity_id: choice };
  }
  return updated;
}

/** Show assigned entities in HA, instead of an invalid placeholder entity ID.
 * Metadata follows actions through HA's reorder, duplicate and nested editors.
 * The preview is restored to its shortcut and our metadata removed before saving.
 */
export function actionEditorValue(sequence, assignments = {}) {
  const value = clone(sequence);
  for (const { action } of actionTargetRows(value)) {
    const shortcuts = targetShortcuts(action);
    if (!shortcuts.length) continue;
    const ids = action.target.entity_id;
    const displayed = entityList(ids).flatMap((id) => {
      if (!shortcuts.includes(id)) return [id];
      const assigned = entityList(assignments[id]);
      return assigned.length ? assigned : ["none"];
    });
    action.target.entity_id = displayed;
    const previous = action.metadata?.[editorKey];
    const marker = {
      version: 1,
      original: encode(ids),
      displayed: encode(displayed),
      hadMetadata: Object.hasOwn(action, "metadata"),
    };
    if (previous !== undefined) marker.previous = encode(previous);
    action.metadata = { ...action.metadata, [editorKey]: marker };
  }
  return value;
}

export function actionEditorResult(sequence) {
  const value = clone(sequence);
  // An action's type may have changed, so inspect every script action here.
  for (const { action } of actionTargetRows(value, true)) {
    const marker = action.metadata?.[editorKey];
    if (
      marker?.version !== 1 ||
      typeof marker.original !== "string" ||
      typeof marker.displayed !== "string"
    )
      continue;
    let original, displayed, previous;
    try {
      original = decode(marker.original);
      displayed = decode(marker.displayed);
      if (Object.hasOwn(marker, "previous")) previous = decode(marker.previous);
    } catch {
      // Leave unrelated or malformed user-supplied metadata alone.
      continue;
    }
    const ids = action.target?.entity_id;
    if (ids !== undefined && sameEntities(ids, displayed))
      action.target.entity_id = original;
    if (Object.hasOwn(marker, "previous"))
      action.metadata[editorKey] = previous;
    else delete action.metadata[editorKey];
    if (!marker.hadMetadata && !Object.keys(action.metadata).length)
      delete action.metadata;
  }
  return value;
}
