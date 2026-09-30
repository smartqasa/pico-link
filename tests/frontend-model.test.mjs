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
  allowedTargetGroups,
  setActionTarget,
  targetChoice,
  targetGroups,
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

test("assigned target follows the Pico group and explicit empty overrides", () => {
  assert.deepEqual(targetGroups({}, { lights: ["light.desk"] }), ["lights"]);
  assert.deepEqual(
    targetGroups({ lights: [] }, { lights: ["light.desk"] }),
    [],
  );
  assert.deepEqual(
    targetGroups({}, { lights: ["light.desk"] }, false, "4B"),
    [],
  );
  assert.deepEqual(targetGroups({}, {}, true), [
    "lights",
    "covers",
    "fans",
    "media_players",
    "switches",
  ]);
});

test("target choices match the service domain and generic Home Assistant actions", () => {
  const available = targetGroups({}, {}, true);
  for (const [domain, group] of Object.entries({
    light: "lights",
    cover: "covers",
    fan: "fans",
    media_player: "media_players",
    switch: "switches",
  })) {
    assert.deepEqual(
      allowedTargetGroups({ action: `${domain}.turn_on` }, available),
      [group],
    );
    assert.deepEqual(
      allowedTargetGroups({ service: `${domain}.turn_on` }, available),
      [group],
    );
  }
  assert.deepEqual(
    allowedTargetGroups({ action: "homeassistant.turn_off" }, available),
    available,
  );
  assert.deepEqual(
    allowedTargetGroups({ action: "scene.turn_on" }, available),
    [],
  );
  assert.deepEqual(
    allowedTargetGroups({ action: "light.turn_on" }, ["covers"]),
    [],
  );
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

test("changing one nested target preserves action options and every other action", () => {
  const sequence = [
    {
      choose: [
        {
          conditions: [],
          sequence: [
            {
              action: "light.turn_on",
              alias: "Evening",
              target: {
                entity_id: "light.old",
                area_id: "office",
                device_id: "old",
              },
              data: { brightness_pct: 50 },
              continue_on_error: true,
            },
            {
              action: "cover.close_cover",
              target: { entity_id: "cover.shade" },
            },
          ],
        },
      ],
    },
  ];
  const original = clone(sequence);
  const path = [0, "choose", 0, "sequence", 0];
  const updated = setActionTarget(sequence, path, "lights");
  assert.deepEqual(updated[0].choose[0].sequence[0], {
    ...original[0].choose[0].sequence[0],
    target: { entity_id: "lights" },
  });
  assert.deepEqual(
    updated[0].choose[0].sequence[1],
    original[0].choose[0].sequence[1],
  );
  assert.deepEqual(sequence, original);
});

test("existing shortcuts, explicit targets, templates and mixed targets are distinguished", () => {
  for (const entity_id of ["lights", ["lights"]])
    assert.equal(targetChoice({ target: { entity_id } }), "lights");
  for (const target of [
    undefined,
    { area_id: "office" },
    { entity_id: "{{ targets }}" },
    { entity_id: ["light.a", "light.b"] },
  ])
    assert.equal(targetChoice({ target }), "explicit");
  assert.equal(
    targetChoice({ target: { entity_id: ["lights", "light.a"] } }),
    "mixed",
  );
  assert.equal(
    targetChoice({ target: { entity_id: "lights", area_id: "office" } }),
    "mixed",
  );
});

test("returning to specific targets removes shortcuts but preserves extra selections", () => {
  const sequence = [
    {
      action: "light.turn_on",
      target: {
        entity_id: ["lights", "light.a", "{{ extra }}"],
        area_id: "office",
      },
      data: { brightness_pct: 42 },
    },
  ];
  const updated = setActionTarget(sequence, [0], "explicit");
  assert.deepEqual(updated[0].target, {
    entity_id: ["light.a", "{{ extra }}"],
    area_id: "office",
  });
  const assigned = setActionTarget(sequence, [0], "lights");
  assert.equal(setActionTarget(assigned, [0], "explicit")[0].target, undefined);
  const explicit = [
    { service: "light.turn_on", target: { entity_id: "light.a" } },
  ];
  assert.deepEqual(setActionTarget(explicit, [0], "explicit"), explicit);
});

test("reordering or deleting actions produces fresh target paths without stale matches", () => {
  const first = { action: "light.turn_on", alias: "First" };
  const second = { service: "cover.close_cover", alias: "Second" };
  assert.deepEqual(
    actionTargetRows([second, first]).map((r) => [r.path, r.action.alias]),
    [
      [[0], "Second"],
      [[1], "First"],
    ],
  );
  assert.throws(() => setActionTarget([first], [1], "lights"), /changed/);
  assert.throws(() => setActionTarget([first], [0], "unknown"), /Unknown/);
  assert.throws(
    () =>
      setActionTarget(
        [{ variables: { nested: first } }],
        [0, "variables", "nested"],
        "lights",
      ),
    /changed/,
  );
});

test("native editor display round-trips shortcuts, mixed targets and metadata", () => {
  const sequence = [
    {
      action: "light.turn_on",
      target: {
        entity_id: ["lights", "light.extra", "{{ existing_template }}"],
        area_id: "office",
      },
      metadata: { note: "keep", pico_link_target_editor: { user_data: 2 } },
      data: { brightness_pct: 50 },
    },
    {
      repeat: {
        count: 2,
        sequence: [
          { service: "cover.close_cover", target: { entity_id: "covers" } },
        ],
      },
    },
  ];
  const original = clone(sequence);
  const display = actionEditorValue(sequence, {
    lights: ["light.assigned"],
    covers: ["cover.assigned"],
  });
  assert.deepEqual(display[0].target.entity_id, [
    "light.assigned",
    "light.extra",
    "{{ existing_template }}",
  ]);
  assert.deepEqual(actionEditorResult(display), original);
  assert.deepEqual(sequence, original);
  assert.deepEqual(actionEditorResult(clone(display)), original);
});

test("native editor edits, duplication and reordering retain the correct shortcuts", () => {
  const sequence = [
    {
      action: "light.turn_on",
      target: { entity_id: "lights" },
      data: { brightness_pct: 20 },
    },
    { action: "cover.close_cover", target: { entity_id: "covers" } },
  ];
  const display = actionEditorValue(sequence);
  display[0].data.brightness_pct = 80;
  const edited = actionEditorResult([
    display[1],
    clone(display[0]),
    display[0],
  ]);
  assert.deepEqual(
    edited.map((a) => a.target.entity_id),
    ["covers", "lights", "lights"],
  );
  assert.equal(edited[1].data.brightness_pct, 80);
  assert.ok(edited.every((a) => !a.metadata));
});

test("explicit target changes in the native editor win and arbitrary templates stay literal", () => {
  const display = actionEditorValue([
    { action: "light.turn_on", target: { entity_id: "lights" } },
  ]);
  display[0].target = { entity_id: "light.selected" };
  assert.deepEqual(actionEditorResult(display), [
    { action: "light.turn_on", target: { entity_id: "light.selected" } },
  ]);
  const explicit = [
    {
      action: "light.turn_on",
      target: { entity_id: "{{ pico_link_assigned_lights }}" },
    },
  ];
  assert.deepEqual(actionEditorResult(actionEditorValue(explicit)), explicit);
});

test("editor decoration is removed if a service or target field is removed", () => {
  const display = actionEditorValue([
    { action: "light.turn_on", target: { entity_id: "lights" }, metadata: {} },
  ]);
  display[0].action = "script.turn_on";
  delete display[0].target;
  assert.deepEqual(actionEditorResult(display), [
    { action: "script.turn_on", metadata: {} },
  ]);
  delete display[0].action;
  display[0].delay = 1;
  assert.deepEqual(actionEditorResult(display), [{ delay: 1, metadata: {} }]);
});

test("empty shared previews never turn into saved none targets", () => {
  const sequence = [
    { action: "light.turn_on", target: { entity_id: "lights" } },
  ];
  const display = actionEditorValue(sequence);
  assert.deepEqual(display[0].target, { entity_id: ["none"] });
  assert.deepEqual(actionEditorResult(display), sequence);
});

test("native target normalization preserves the logical assignment", () => {
  const sequence = [
    { action: "light.turn_on", target: { entity_id: "lights" } },
  ];
  const display = actionEditorValue(sequence, {
    lights: ["light.a", "light.b"],
  });
  display[0].target.entity_id.reverse();
  assert.deepEqual(actionEditorResult(display), sequence);
  const single = actionEditorValue(sequence, { lights: "light.a" });
  single[0].target.entity_id = "light.a";
  assert.deepEqual(actionEditorResult(single), sequence);
});

test("malformed unrelated editor metadata and existing metadata are preserved", () => {
  const action = {
    action: "light.turn_on",
    target: { entity_id: "light.a" },
    metadata: {
      pico_link_target_editor: {
        version: 1,
        original: "%bad",
        displayed: "bad",
      },
    },
  };
  assert.deepEqual(actionEditorResult([action]), [action]);
});
