import test from "node:test";
import assert from "node:assert/strict";
import {
  gestureValue,
  setGesture,
  behavior,
  assignment,
  assignEntities,
  listRows,
  clone,
} from "../custom_components/pico_link/frontend/model.js";

test("legacy Stop alias is preserved until that gesture changes", () => {
  const raw = { middle_button: "default", stop_hold: [{ delay: 3 }] };
  assert.equal(gestureValue(raw, "stop_tap"), "default");
  assert.equal(behavior(gestureValue(raw, "stop_tap")), "shared");
  setGesture(raw, "stop_tap", []);
  assert.deepEqual(raw, { stop_tap: [], stop_hold: [{ delay: 3 }] });
  setGesture(raw, "stop_tap", undefined);
  assert.deepEqual(raw, { stop_hold: [{ delay: 3 }] });
});
test("scene double tap does not overwrite the legacy tap sequence", () => {
  const raw = { buttons: { button_1: [{ action: "light.turn_on" }], off: [] } };
  setGesture(raw, "button_1_double_tap", [{ delay: 1 }]);
  assert.deepEqual(gestureValue(raw, "button_1_tap"), [
    { action: "light.turn_on" },
  ]);
  setGesture(raw, "button_1_tap", []);
  assert.deepEqual(raw.buttons, { off: [] });
  assert.deepEqual(raw.button_1_double_tap, [{ delay: 1 }]);
});
test("explicit empty Stop tap wins over the legacy alias", () => {
  assert.deepEqual(
    gestureValue({ stop_tap: [], middle_button: [{ delay: 1 }] }, "stop_tap"),
    [],
  );
});
test("switching domains masks shared assignments without modifying defaults", () => {
  const defaults = { lights: ["light.a"] };
  const raw = { on_hold: [{ delay: 4 }] };
  assert.equal(assignment(raw, defaults), "light");
  assignEntities(raw, "cover", ["cover.b"]);
  assert.equal(assignment(raw, defaults), "cover");
  assert.deepEqual(defaults, { lights: ["light.a"] });
  assert.deepEqual(raw.on_hold, [{ delay: 4 }]);
});
test("filtered and sorted rows retain correct device indexes with duplicate names", () => {
  const doc = {
    devices: [{ device_id: "b" }, { device_id: "a" }, { device_id: "c" }],
  };
  const snapshot = clone(doc);
  const catalog = [
    { id: "a", name: "Bedroom", area: "Upstairs" },
    { id: "b", name: "Office" },
    { id: "c", name: "Bedroom", area: "Downstairs" },
  ];
  assert.deepEqual(
    listRows(doc, catalog).map((r) => r.index),
    [1, 2, 0],
  );
  assert.deepEqual(
    listRows(doc, catalog, "upstairs").map((r) => r.index),
    [1],
  );
  assert.deepEqual(doc, snapshot);
});
test("missing remote stays selectable for repair or removal", () => {
  const rows = listRows(
    { devices: [{ device_id: "missing", name: "Old Pico" }] },
    [],
  );
  assert.equal(rows[0].name, "Old Pico");
  assert.equal(rows[0].available, false);
});
