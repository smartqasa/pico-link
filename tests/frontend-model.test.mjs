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
import {
  actionEditorResult,
  actionEditorValue,
  actionTargetRows,
} from "../custom_components/pico_link/frontend/action-targets.js";

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

test("service action traversal includes nested branches without inspecting payloads", () => {
  const service = { action: "light.turn_on", target: { entity_id: "lights" } };
  const sequence = [
    {
      alias: "Night",
      if: [
        { condition: "state", entity_id: "sun.sun", state: "below_horizon" },
      ],
      then: [service],
      else: service,
    },
    { choose: [{ conditions: [], sequence: [service] }], default: [service] },
    { repeat: { count: 2, sequence: [service] } },
    { parallel: [service, { sequence: [service] }] },
    {
      action: "script.turn_on",
      data: { sequence: [service], then: [service] },
    },
    { variables: { parallel: [service] } },
    { delay: 2 },
  ];
  const snapshot = clone(sequence);
  const rows = actionTargetRows(sequence);
  assert.deepEqual(
    rows.map((row) => row.path),
    [
      [0, "then", 0],
      [0, "else"],
      [1, "choose", 0, "sequence", 0],
      [1, "default", 0],
      [2, "repeat", "sequence", 0],
      [3, "parallel", 0],
      [3, "parallel", 1, "sequence", 0],
    ],
  );
  assert.deepEqual(
    rows.map((row) => row.location),
    [
      "1 › then › 1",
      "1 › else",
      "2 › choice 1 › 1",
      "2 › default › 1",
      "3 › repeat › 1",
      "4 › parallel › 1",
      "4 › parallel › 2 › sequence › 1",
    ],
  );
  assert.deepEqual(sequence, snapshot);
});

const placeholder = "light.pico_link_placeholder";

test("legacy light targets show the real placeholder, never a preview lamp", () => {
  const actions = [
    {
      action: "light.turn_on",
      target: { entity_id: "lights" },
      data: { brightness_pct: 80, color_temp_kelvin: 2800 },
    },
  ];
  const shown = actionEditorValue(actions, placeholder);
  assert.equal(shown[0].target.entity_id, placeholder);
  assert.deepEqual(actionEditorResult(shown, placeholder), actions);
  assert.equal(actions[0].target.entity_id, "lights");
  assert.ok(!shown[0].metadata);
});

test("native picker selection saves a portable light shortcut", () => {
  const actions = [
    { action: "light.turn_on", target: { entity_id: [placeholder] } },
  ];
  assert.deepEqual(
    actionEditorResult(actions, placeholder)[0].target.entity_id,
    ["lights"],
  );
});

test("nested mixed targets and unrelated payloads survive editing", () => {
  const actions = [
    {
      repeat: {
        count: 2,
        sequence: [
          {
            action: "light.turn_on",
            target: { entity_id: ["light.fixed", "lights"], area_id: "office" },
            data: { note: "lights" },
            metadata: { note: "retain" },
          },
        ],
      },
    },
    {
      action: "script.turn_on",
      data: {
        sequence: [
          { action: "light.turn_on", target: { entity_id: "lights" } },
        ],
      },
    },
  ];
  const shown = actionEditorValue(actions, placeholder);
  assert.deepEqual(shown[0].repeat.sequence[0].target.entity_id, [
    "light.fixed",
    placeholder,
  ]);
  assert.equal(shown[1].data.sequence[0].target.entity_id, "lights");
  shown[0].repeat.sequence[0].data.brightness_pct = 80;
  const saved = actionEditorResult(shown, placeholder);
  assert.deepEqual(
    saved[0].repeat.sequence[0].target,
    actions[0].repeat.sequence[0].target,
  );
  assert.equal(saved[0].repeat.sequence[0].data.brightness_pct, 80);
  assert.deepEqual(saved[0].repeat.sequence[0].metadata, { note: "retain" });
});

test("renamed placeholder identity and explicit target edits work", () => {
  const original = [
    { action: "light.turn_on", target: { entity_id: "lights" } },
  ];
  const renamed = "light.my_placeholder";
  const shown = actionEditorValue(original, renamed);
  assert.equal(shown[0].target.entity_id, renamed);
  assert.deepEqual(actionEditorResult(shown, renamed), original);
  shown[0].target.entity_id = "light.selected";
  assert.equal(
    actionEditorResult(shown, renamed)[0].target.entity_id,
    "light.selected",
  );
});

test("other domain shortcuts, template text and missing registry are preserved", () => {
  for (const entity_id of [
    "covers",
    "fans",
    "switches",
    "media_players",
    "{{ targets }}",
    "light.pico_link_placeholder_2",
  ]) {
    const sequence = [
      { action: "homeassistant.turn_off", target: { entity_id } },
    ];
    assert.deepEqual(
      actionEditorResult(actionEditorValue(sequence, placeholder), placeholder),
      sequence,
    );
  }
  const sequence = [
    { action: "light.turn_on", target: { entity_id: "lights" } },
  ];
  assert.deepEqual(actionEditorValue(sequence), sequence);
});

test("native reordering, duplication, and removing targets need no editor metadata", () => {
  const shown = actionEditorValue(
    [
      { action: "light.turn_on", target: { entity_id: "lights" } },
      { action: "light.turn_off", target: { entity_id: "light.fixed" } },
    ],
    placeholder,
  );
  const result = actionEditorResult(
    [shown[1], clone(shown[0]), shown[0]],
    placeholder,
  );
  assert.deepEqual(
    result.map((a) => a.target.entity_id),
    ["light.fixed", "lights", "lights"],
  );
  delete shown[0].target;
  assert.deepEqual(actionEditorResult(shown, placeholder)[0], {
    action: "light.turn_on",
  });
});
