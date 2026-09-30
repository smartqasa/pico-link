/** Pure draft operations shared by the panel and its regression tests. */
export const clone = (value) => JSON.parse(JSON.stringify(value));
export const FIELDS = {
  light: "lights",
  cover: "covers",
  fan: "fans",
  media_player: "media_players",
  switch: "switches",
};
export const BUTTONS = {
  P2B: ["on", "off"],
  "2B": ["on", "off"],
  "3BRL": ["on", "raise", "stop", "lower", "off"],
  "4B": ["button_1", "button_2", "button_3", "off"],
};
export const LABELS = {
  on: "On",
  off: "Off",
  raise: "Raise",
  lower: "Lower",
  stop: "Stop / middle",
  button_1: "Button 1",
  button_2: "Button 2",
  button_3: "Button 3",
  tap: "Tap",
  hold: "Hold",
  double_tap: "Double tap",
  light: "Lights",
  cover: "Shades",
  fan: "Fans",
  media_player: "Media players",
  switch: "Switches",
};
export const TYPES = {
  P2B: "Paddle Pico",
  "2B": "Two-button Pico",
  "3BRL": "Five-button Pico",
  "4B": "Scene Pico",
};

export function gestureValue(raw, key) {
  if (Object.hasOwn(raw, key)) return raw[key];
  if (key === "stop_tap") return raw.middle_button;
  if (key.endsWith("_tap") && !key.endsWith("_double_tap"))
    return raw.buttons?.[key.slice(0, -4)];
  return undefined;
}
export function clearGesture(raw, key) {
  delete raw[key];
  if (key === "stop_tap") delete raw.middle_button;
  if (key.endsWith("_tap") && !key.endsWith("_double_tap") && raw.buttons) {
    delete raw.buttons[key.slice(0, -4)];
    if (!Object.keys(raw.buttons).length) delete raw.buttons;
  }
}
export function setGesture(raw, key, value) {
  clearGesture(raw, key);
  if (value !== undefined) raw[key] = clone(value);
}
export function behavior(value) {
  return value === undefined
    ? "normal"
    : value === "default"
      ? "shared"
      : value.length
        ? "custom"
        : "disabled";
}
export function assignment(raw, defaults = {}) {
  const merged = { ...defaults, ...raw };
  return (
    Object.keys(FIELDS).find((domain) => merged[FIELDS[domain]]?.length) ||
    "light"
  );
}
export function assignEntities(raw, domain, entities) {
  for (const field of Object.values(FIELDS)) raw[field] = [];
  raw[FIELDS[domain]] = clone(entities);
}
export function deviceMeta(raw, catalog) {
  const device = catalog.find((d) => d.id === raw.device_id);
  return {
    name: device?.name || raw.name || "Unavailable Pico",
    area: device?.area || "",
    type: raw.type || device?.type,
    model: device?.model || "",
    available: !!device,
  };
}
export function listRows(document, catalog, search = "") {
  return document.devices
    .map((raw, index) => ({ index, raw, ...deviceMeta(raw, catalog) }))
    .filter((row) =>
      `${row.name} ${row.area} ${row.type || ""}`
        .toLowerCase()
        .includes(search.toLowerCase()),
    )
    .sort(
      (a, b) =>
        a.name.localeCompare(b.name, undefined, {
          numeric: true,
          sensitivity: "base",
        }) || a.index - b.index,
    );
}
