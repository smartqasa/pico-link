/** Bridge the legacy lights shortcut to the registered picker entity. */
import { clone, FIELDS } from "./model.js";
const groups = Object.values(FIELDS);
const object = (value) =>
  value && typeof value === "object" && !Array.isArray(value);

export function targetShortcuts(action) {
  const ids = action.target?.entity_id;
  return [
    ...new Set(
      (Array.isArray(ids) ? ids : [ids]).filter((id) => groups.includes(id)),
    ),
  ];
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

function replaceTarget(sequence, from, to) {
  const value = clone(sequence);
  if (!from || !to) return value;
  for (const { action } of actionTargetRows(value)) {
    const ids = action.target?.entity_id;
    if (Array.isArray(ids))
      action.target.entity_id = ids.map((id) => (id === from ? to : id));
    else if (ids === from) action.target.entity_id = to;
  }
  return value;
}

// No sample lamp, synthetic hass state, or temporary action metadata is needed.
export function actionEditorValue(sequence, placeholderId) {
  return replaceTarget(sequence, "lights", placeholderId);
}

// Keep saved UI actions independent of the placeholder's editable entity ID.
export function actionEditorResult(sequence, placeholderId) {
  return replaceTarget(sequence, placeholderId, "lights");
}
