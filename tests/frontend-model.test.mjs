import test from "node:test";
import assert from "node:assert/strict";
import {
  BUTTONS,
  TYPES,
  deviceMeta,
  gestureValue,
  setGesture,
  behavior,
  assignment,
  assignEntities,
  listRows,
  clone,
  colorPalette,
  selectPalette,
  setPalette,
  movePaletteColor,
} from "../custom_components/pico_link/frontend/model.js";
import {
  actionEditorResult,
  actionEditorValue,
  actionTargetRows,
} from "../custom_components/pico_link/frontend/action-targets.js";

test("cycling is explicit and does not change old gesture meanings", () => {
  assert.equal(behavior("color_cycle"), "color_cycle");
  assert.equal(behavior("color_cycle", true), "color_cycle");
  assert.equal(behavior(undefined), "normal");
  assert.equal(behavior("default"), "shared");
  const raw = { middle_button: "default", stop_hold: [{ delay: 4 }] };
  setGesture(raw, "stop_tap", "color_cycle");
  assert.deepEqual(raw, { stop_tap: "color_cycle", stop_hold: [{ delay: 4 }] });
});

test("shared palettes follow edits while custom copies remain independent", () => {
  const key = "stop_tap";
  const starter = [{ color_temp_kelvin: 2800 }];
  const defaults = {};
  const shared = {};
  const custom = {};
  selectPalette(custom, true, defaults, starter, key);
  custom.color_palettes[key].push({ rgb_color: [0, 0, 255] });
  setPalette(defaults, key, [{ rgb_color: [255, 0, 0] }]);
  assert.deepEqual(
    colorPalette(shared, defaults, starter, key),
    defaults.color_palettes[key],
  );
  assert.deepEqual(colorPalette(custom, defaults, starter, key), [
    starter[0],
    { rgb_color: [0, 0, 255] },
  ]);
  assert.equal(starter.length, 1);
  selectPalette(custom, false, defaults, starter, key);
  assert.equal(custom.color_palettes[key], undefined);
  assert.deepEqual(
    colorPalette(custom, defaults, starter, key),
    defaults.color_palettes[key],
  );
});

test("palette reordering preserves colors without mutating shared definitions", () => {
  const original = [{ color_temp_kelvin: 2800 }, { rgb_color: [255, 0, 0] }];
  assert.deepEqual(movePaletteColor(original, 0, 1), [
    original[1],
    original[0],
  ]);
  assert.deepEqual(movePaletteColor(original, 0, -1), original);
  const copy = colorPalette({}, {}, original, "stop_tap");
  copy[1].rgb_color[0] = 1;
  assert.equal(original[1].rgb_color[0], 255);
});

test("gesture edits, restore, and inheritance do not change sibling palettes", () => {
  const keys = ["stop_tap", "stop_hold", "stop_double_tap"];
  const starter = [{ color_temp_kelvin: 2800 }];
  const saved = { defaults: {}, devices: [{}] };
  for (const [i, key] of keys.entries()) {
    setPalette(saved.defaults, key, [{ color_temp_kelvin: 3000 + i * 1000 }]);
  }
  const draft = clone(saved);
  const pico = draft.devices[0];
  for (const [i, key] of keys.entries()) {
    assert.deepEqual(colorPalette(pico, draft.defaults, starter, key), [
      { color_temp_kelvin: 3000 + i * 1000 },
    ]);
    selectPalette(pico, true, draft.defaults, starter, key);
  }
  setPalette(pico, "stop_tap", [{ color_temp_kelvin: 3200 }]);
  assert.deepEqual(pico.color_palettes.stop_hold, [
    { color_temp_kelvin: 4000 },
  ]);
  assert.deepEqual(pico.color_palettes.stop_double_tap, [
    { color_temp_kelvin: 5000 },
  ]);
  // Restore touches only the selected gesture and only the draft.
  setPalette(pico, "stop_hold", starter);
  assert.deepEqual(pico.color_palettes.stop_tap, [{ color_temp_kelvin: 3200 }]);
  assert.deepEqual(pico.color_palettes.stop_double_tap, [
    { color_temp_kelvin: 5000 },
  ]);
  assert.deepEqual(saved.devices, [{}]);
  assert.deepEqual(starter, [{ color_temp_kelvin: 2800 }]);
  // Returning Tap to shared follows Tap alone; custom siblings stay fixed.
  selectPalette(pico, false, draft.defaults, starter, "stop_tap");
  setPalette(draft.defaults, "stop_tap", [{ color_temp_kelvin: 3500 }]);
  assert.deepEqual(colorPalette(pico, draft.defaults, starter, "stop_tap"), [
    { color_temp_kelvin: 3500 },
  ]);
  assert.deepEqual(
    colorPalette(pico, draft.defaults, starter, "stop_hold"),
    starter,
  );
  assert.deepEqual(
    colorPalette(pico, draft.defaults, starter, "stop_double_tap"),
    [{ color_temp_kelvin: 5000 }],
  );
  // Restoring a shared gesture leaves its siblings and Pico custom lists alone.
  setPalette(draft.defaults, "stop_hold", starter);
  assert.deepEqual(draft.defaults.color_palettes.stop_tap, [
    { color_temp_kelvin: 3500 },
  ]);
  assert.deepEqual(draft.defaults.color_palettes.stop_double_tap, [
    { color_temp_kelvin: 5000 },
  ]);
  assert.deepEqual(saved.defaults.color_palettes.stop_hold, [
    { color_temp_kelvin: 4000 },
  ]);
});

test("2BRL uses its detected layout and keeps explicit layout precedence", () => {
  const catalog = [{ id: "dimmer", name: "Hall Pico", type: "2BRL" }];
  const raw = { device_id: "dimmer" };
  assert.equal(deviceMeta(raw, catalog).type, "2BRL");
  assert.deepEqual(BUTTONS[deviceMeta(raw, catalog).type], [
    "on",
    "raise",
    "lower",
    "off",
  ]);
  assert.equal(TYPES["2BRL"], "Four-button Raise/Lower Pico");
  assert.equal(deviceMeta({ ...raw, type: "3BRL" }, catalog).type, "3BRL");
  assert.equal(
    listRows({ devices: [raw] }, catalog, "2brl")[0].name,
    "Hall Pico",
  );
});

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
test("shared gestures default to Do nothing while individual gestures stay normal", () => {
  for (const key of ["stop_tap", "stop_hold", "stop_double_tap"]) {
    assert.equal(behavior(gestureValue({}, key), true), "disabled");
    assert.equal(behavior(gestureValue({}, key)), "normal");
    assert.equal(behavior(gestureValue({ [key]: [] }, key), true), "disabled");
    assert.equal(
      behavior(gestureValue({ [key]: [{ delay: 1 }] }, key), true),
      "custom",
    );
    assert.equal(behavior(gestureValue({ [key]: "default" }, key)), "shared");
  }
  assert.equal(
    behavior(gestureValue({ middle_button: [{ delay: 1 }] }, "stop_tap"), true),
    "custom",
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
