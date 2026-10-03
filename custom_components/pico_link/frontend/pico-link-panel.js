// Keep imported modules and styles on the same release as the panel itself.
function asset(path) {
  const url = new URL(path, import.meta.url);
  url.search = new URL(import.meta.url).search;
  return url.href;
}
const {
  clone,
  FIELDS,
  BUTTONS,
  LABELS,
  TYPES,
  gestureValue,
  setGesture,
  behavior,
  assignment,
  assignEntities,
  deviceMeta,
  listRows,
  colorPalette,
  selectPalette,
  movePaletteColor,
} = await import(asset("./model.js"));
const {
  actionEditorResult,
  actionEditorValue,
  actionTargetRows,
  targetShortcuts,
} = await import(asset("./action-targets.js"));

const esc = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
const numberLabels = {
  hold_time_ms: "Hold threshold",
  double_tap_time_ms: "Double-tap window",
  step_time_ms: "Dimming step interval",
  light_on_pct: "Turn-on brightness",
  light_low_pct: "Minimum brightness",
  light_step_pct: "Brightness step",
  light_transition_on: "Turn-on transition",
  light_transition_off: "Turn-off transition",
  cover_open_pos: "Open position",
  cover_step_pct: "Position step",
  fan_on_pct: "Turn-on speed",
  media_player_vol_step: "Volume step",
};
const modeLabels = {
  single: "Single — ignore while busy",
  restart: "Restart — newest press takes over",
  queued: "Queued — run in order",
  parallel: "Parallel — run together",
};
const paddlePicoButtons =
  '<rect x="5" y="5" width="10" height="11" rx="1"/><rect x="5" y="18" width="10" height="11" rx="1"/>';
const miniPicoButtons = {
  P2B: paddlePicoButtons,
  "2B": paddlePicoButtons,
  "2BRL":
    '<rect x="5" y="5" width="10" height="6" rx="1"/><path d="M5 13h9.1L5 20.2zm10 .8V21H5.9z"/><rect x="5" y="23" width="10" height="6" rx="1"/>',
  "3BRL":
    '<rect x="5" y="5" width="10" height="6" rx="1"/><path d="M5 13h9.1l-2.9 2.3a2.1 2.1 0 0 0-3 2.4L5 20.2zm10 .8V21H5.9l2.9-2.3a2.1 2.1 0 0 0 3-2.4z"/><circle cx="10" cy="17" r="1.1"/><rect x="5" y="23" width="10" height="6" rx="1"/>',
  "4B": '<rect x="5" y="5" width="10" height="4.5" rx="1"/><rect x="5" y="11.5" width="10" height="4.5" rx="1"/><rect x="5" y="18" width="10" height="4.5" rx="1"/><rect x="5" y="24.5" width="10" height="4.5" rx="1"/>',
};
function miniPico(type) {
  const buttons =
    miniPicoButtons[type] ||
    '<circle cx="10" cy="13" r="1.5"/><circle cx="10" cy="21" r="1.5"/>';
  return `<svg class="mini-pico" viewBox="0 0 20 34" aria-hidden="true" focusable="false"><rect x="1" y="1" width="18" height="32" rx="3" fill="none" stroke="currentColor" stroke-width="1.2"/><g fill="currentColor">${buttons}</g></svg>`;
}
const stylesheet = asset("./panel.css");
let componentsReady;

async function loadEditors() {
  if (!componentsReady)
    componentsReady = (async () => {
      if (!customElements.get("ha-form")) {
        // Ask HA's own card editor loader to register its forms and selectors.
        // No external libraries, hashed frontend paths, or copied HA components.
        const helpers = await window.loadCardHelpers();
        const card = helpers.createCardElement({
          type: "entities",
          entities: [],
        });
        await card.constructor.getConfigElement();
      }
      if (!customElements.get("ha-form"))
        throw new Error(
          "Home Assistant's form editor did not load. Refresh the browser and reopen Pico Link.",
        );
    })().catch((err) => {
      componentsReady = undefined;
      throw err;
    });
  return componentsReady;
}

class PicoLinkPanel extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({ mode: "open" });
    this._selected = null;
    this._tab = "buttons";
    this._button = "on";
    this._gesture = "tap";
    this._search = "";
    this._busy = false;
    this._beforeUnload = (e) => {
      if (this.dirty) {
        e.preventDefault();
        e.returnValue = "";
      }
    };
  }
  set hass(value) {
    this._hass = value;
    this.shadowRoot
      .querySelectorAll("ha-form, ha-menu-button")
      .forEach((el) => {
        el.hass = el.dataset.picoActionEditor
          ? this._actionEditorHass()
          : value;
      });
    if (this.isConnected && !this._loading && !this._state) this._load();
  }
  get hass() {
    return this._hass;
  }
  connectedCallback() {
    window.addEventListener("beforeunload", this._beforeUnload);
    if (this.hass && !this._state) this._load();
  }
  disconnectedCallback() {
    window.removeEventListener("beforeunload", this._beforeUnload);
  }
  get dirty() {
    return !!this._draft && JSON.stringify(this._draft) !== this._saved;
  }
  get shared() {
    return this._selected === "defaults";
  }
  get remote() {
    return this.shared
      ? this._draft.defaults
      : this._draft.devices[this._selected];
  }

  async _load() {
    this._loading = true;
    try {
      const state = await this.hass.callWS({ type: "pico_link/config" });
      this._accept(state);
      this._render();
      await Promise.all([
        loadEditors(),
        this.hass.loadFragmentTranslation("config"),
      ]);
      this._renderDetail();
    } catch (err) {
      this._error = err.message || String(err);
      if (!this._state)
        this.shadowRoot.innerHTML = `<link rel="stylesheet" href="${stylesheet}"><main class="failure"><h1>Pico Link</h1><p role="alert">${esc(this._error)}</p><button id="retry">Try again</button></main>`;
      this.shadowRoot
        .querySelector("#retry")
        ?.addEventListener("click", () => this._load());
      this._status();
    } finally {
      this._loading = false;
    }
  }
  _accept(state) {
    this._state = state;
    this._draft = clone(state.document);
    this._draft.defaults ||= {};
    this._saved = JSON.stringify(this._draft);
    this._selected = this._draft.devices.length ? 0 : null;
    this._error = "";
  }
  _render() {
    this.shadowRoot.innerHTML = `<link rel="stylesheet" href="${stylesheet}">
      <header class="topbar"><button id="menu" class="quiet" aria-label="Sidebar toggle">☰</button><span class="wordmark">Pico Link</span><span class="badge">${this._state.read_only ? "Read only" : "Configuration"}</span><div class="spacer"></div><a href="https://github.com/smartqasa/pico-link#choose-your-configuration-method" target="_blank" rel="noopener noreferrer">Help</a></header>
      <main><div class="page-heading"><div><h1>Lutron Picos</h1></div><div class="heading-actions"><button id="defaults">Shared defaults</button><button class="primary" id="add">＋ Add Pico</button></div></div>
      <div id="notice"></div><div id="status" aria-live="polite"></div>
      <div class="workspace"><aside class="library"><label class="search"><span aria-hidden="true">⌕</span><input id="search" type="search" aria-label="Search Picos" placeholder="Search name or room"></label><div class="list-caption" id="count"></div><div id="list" class="remote-list"></div></aside><section id="detail" class="detail" aria-label="Pico settings"></section></div>
      </main><footer class="savebar"><div><strong id="save-state"></strong><span>Settings apply when you save. Button previews do not operate devices.</span></div><div><button id="discard">Discard changes</button><button id="save" class="primary">Save changes</button></div></footer>`;
    this._on("#menu", "click", () =>
      this.dispatchEvent(
        new Event("hass-toggle-menu", { bubbles: true, composed: true }),
      ),
    );
    this._on("#search", "input", (e) => {
      this._search = e.target.value;
      this._renderList();
    });
    this._on("#defaults", "click", () => {
      this._selected = "defaults";
      this._button = "stop";
      this._tab = "buttons";
      this._renderList();
      this._renderDetail();
    });
    this._on("#add", "click", () => this._add());
    this._on("#save", "click", () => this._save());
    this._on("#discard", "click", () => {
      this._confirm(
        "Discard unsaved changes?",
        "Your saved Pico settings will stay as they are.",
        "Discard changes",
        () => {
          this._accept(this._state);
          this._render();
        },
      );
    });
    if (this._state.read_only) {
      this.shadowRoot.querySelector("#notice").innerHTML =
        `<div class="notice">${this._state.reason === "yaml" ? "YAML is the active configuration method. This panel cannot change your running remotes. To switch, select UI in your YAML configuration, restart, then import your settings here." : "Pico Link is disabled. Enable it in Devices & services before editing."}</div>`;
    } else if (!this._state.configured && this._state.yaml_available) {
      this.shadowRoot.querySelector("#notice").innerHTML =
        `<div class="notice"><div><strong>Bring your existing Picos with you</strong><p>Import your YAML into a draft. Your current remotes keep working until you save.</p></div><button id="import">Import YAML</button></div>`;
      this._on("#import", "click", async () => {
        try {
          const result = await this.hass.callWS({ type: "pico_link/import" });
          this._draft = result.document;
          this._draft.defaults ||= {};
          this._selected = this._draft.devices.length ? 0 : null;
          this._renderList();
          this._renderDetail();
          this._status();
        } catch (err) {
          this._error = err.message;
          this._status();
        }
      });
    }
    this._renderList();
    this._renderDetail();
    this._status();
  }
  _on(query, event, fn, parent = this.shadowRoot) {
    parent.querySelector(query)?.addEventListener(event, fn);
  }
  _status() {
    const root = this.shadowRoot;
    const status = root.querySelector("#status");
    if (!status) return;
    status.innerHTML = this._error
      ? `<div class="error" role="alert">${esc(this._error)}${this._conflict ? '<button id="reload">Reload saved settings</button>' : ""}</div>`
      : this._message
        ? `<div class="success">${esc(this._message)}</div>`
        : "";
    this._on("#reload", "click", () =>
      this._confirm(
        "Reload saved settings?",
        "Your unsaved draft will be discarded. The newer saved configuration will be loaded.",
        "Reload settings",
        () => this._load(),
      ),
    );
    root.querySelector("#save-state").textContent = this._busy
      ? "Saving…"
      : this.dirty
        ? "Unsaved changes"
        : "All changes saved";
    root.querySelector("#save").disabled =
      this._state.read_only ||
      this._busy ||
      (!this.dirty && this._state.configured);
    root.querySelector("#discard").disabled = this._busy || !this.dirty;
    root.querySelector("#add").disabled = this._state.read_only || this._busy;
  }
  _changed() {
    this._error = "";
    this._message = "";
    this._status();
    this._renderList();
  }
  _renderList() {
    const rows = listRows(this._draft, this._state.catalog, this._search);
    this.shadowRoot.querySelector("#count").textContent =
      `${rows.length} ${rows.length === 1 ? "remote" : "remotes"}${this._search ? ` of ${this._draft.devices.length}` : ""}`;
    this.shadowRoot.querySelector("#list").innerHTML =
      rows
        .map(
          (row) =>
            `<button class="remote-row ${this._selected === row.index ? "selected" : ""}" data-index="${row.index}" aria-pressed="${this._selected === row.index}">${miniPico(row.type)}<span class="remote-copy"><strong>${esc(row.name)}</strong><small>${esc(row.area || TYPES[row.type] || "Check remote identity")}</small></span><span class="chevron" aria-hidden="true">›</span></button>`,
        )
        .join("") || '<p class="empty-list">No Picos found.</p>';
    this.shadowRoot.querySelectorAll(".remote-row").forEach((button) =>
      button.addEventListener("click", () => {
        this._selected = Number(button.dataset.index);
        this._tab = "buttons";
        this._button = "on";
        this._gesture = "tap";
        this._renderList();
        this._renderDetail();
        if (window.innerWidth < 850)
          this.shadowRoot
            .querySelector("#detail")
            .scrollIntoView({ behavior: "smooth", block: "start" });
      }),
    );
  }
  _renderDetail() {
    const detail = this.shadowRoot.querySelector("#detail");
    if (!detail) return;
    if (this._selected === null) {
      detail.innerHTML =
        '<div class="welcome"><h2>No Picos configured</h2><p>Add a Pico to configure its targets, button actions, and settings.</p><button class="primary" id="first-add">Add Pico</button></div>';
      this._on("#first-add", "click", () => this._add());
      detail.querySelector("button").disabled = this._state.read_only;
      return;
    }
    const meta = this.shared
      ? {
          name: "Shared defaults",
          type: "3BRL",
          area: "Settings your Picos can inherit",
        }
      : deviceMeta(this.remote, this._state.catalog);
    const tabs = this.shared
      ? ["buttons", "palette", "timing", "device", "run"]
      : ["buttons", "assignment", "timing", "device", "run"];
    const tabNames = {
      buttons: "Button actions",
      palette: "Color palette",
      assignment: "Remote & targets",
      timing: "Timing",
      device: "Device settings",
      run: "Run behavior",
    };
    detail.innerHTML = `<div class="detail-heading"><div><div class="eyebrow">${this.shared ? "SHARED SETTINGS" : esc(meta.area || TYPES[meta.type] || "REMOTE")}</div><h2>${esc(meta.name)}</h2><p>${this.shared ? "Defaults for Pico settings and shared Stop actions." : `${esc(meta.model || "Device unavailable")}${this.remote.type ? " · Explicit layout" : " · Automatic layout"}`}</p></div>${!this.shared ? '<button class="quiet danger" id="remove" aria-label="Remove this Pico">Remove</button>' : ""}</div><nav class="tabs" role="tablist" aria-label="Pico settings">${tabs.map((tab) => `<button role="tab" aria-selected="${tab === this._tab}" id="tab-${tab}" data-tab="${tab}">${tabNames[tab]}</button>`).join("")}</nav><div id="tab-content" role="tabpanel" aria-labelledby="tab-${this._tab}"></div>`;
    detail.querySelectorAll("[data-tab]").forEach((button) =>
      button.addEventListener("click", () => {
        this._tab = button.dataset.tab;
        this._renderDetail();
      }),
    );
    this._on("#remove", "click", () =>
      this._confirm(
        `Remove ${meta.name}?`,
        "This removes the Pico from Pico Link when you save. The Lutron device itself is unaffected.",
        "Remove Pico",
        () => {
          this._draft.devices.splice(this._selected, 1);
          this._selected = this._draft.devices.length ? 0 : null;
          this._renderDetail();
          this._changed();
        },
      ),
    );
    if (detail.querySelector("#remove"))
      detail.querySelector("#remove").disabled = this._state.read_only;
    const body = detail.querySelector("#tab-content");
    if (this._tab === "buttons") this._buttons(body, meta.type);
    if (this._tab === "palette")
      this._palette(body, this._draft.defaults, true);
    if (this._tab === "assignment") this._assignment(body);
    if (this._tab === "timing")
      this._numbers(
        body,
        ["hold_time_ms", "double_tap_time_ms", "step_time_ms"],
        "A natural response",
        "Double-tap timing applies only to buttons with double tap configured. Custom holds run once.",
      );
    if (this._tab === "device") {
      const domain = assignment(this.remote, this._draft.defaults);
      const keys = this.shared
        ? Object.keys(this._state.numbers).filter(
            (k) => !k.endsWith("_time_ms"),
          )
        : this._state.device_settings[domain];
      if (!this.shared && meta.type === "4B")
        body.innerHTML =
          '<div class="section"><h3>Scene Pico</h3><p>Choose targets inside each button action. Shared device-control settings do not apply.</p></div>';
      else
        this._numbers(
          body,
          keys,
          "Built-in controls",
          "These settings apply to normal button behavior. Custom actions use the values in their own sequence.",
          this.shared || domain === "cover",
        );
    }
    if (this._tab === "run") this._run(body);
  }
  _buttons(body, type) {
    const buttons = this.shared ? ["stop"] : BUTTONS[type];
    if (!buttons) {
      body.innerHTML =
        '<div class="section"><h3>Choose a remote layout</h3><p>Use Remote & targets to repair the identity or select a supported layout.</p></div>';
      return;
    }
    if (!buttons.includes(this._button)) this._button = buttons[0];
    const physicalButton = (button) =>
      `<button class="physical-button button-${button} ${button === this._button ? "active" : ""} ${button === "stop" ? "middle" : ""}" data-button="${button}" aria-label="Configure ${LABELS[button]}" aria-pressed="${button === this._button}"><span>${button === "raise" ? "△" : button === "lower" ? "▽" : button === "stop" ? "●" : LABELS[button]}</span></button>`;
    const dimmer = ["2BRL", "3BRL"].includes(type) && !this.shared;
    const face = dimmer
      ? `${physicalButton("on")}<div class="dimmer-pad">${buttons
          .filter((button) => ["raise", "stop", "lower"].includes(button))
          .map(physicalButton)
          .join("")}</div>${physicalButton("off")}`
      : type === "P2B" && !this.shared
        ? `<div class="paddle-rocker">${buttons.map(physicalButton).join("")}</div>`
        : buttons.map(physicalButton).join("");
    body.innerHTML = `<div class="button-workspace ${this.shared ? "shared-actions" : ""}">${this.shared ? "" : `<div class="remote-preview"><div class="pico-body ${type === "P2B" ? "paddle" : dimmer ? "three-brl" : ""}">${face}</div><p>Select a button to configure</p></div>`}<div class="gesture-editor"><div class="section-heading"><h3>${this.shared ? "Shared Stop actions" : esc(LABELS[this._button])}</h3>${this.shared ? '<span class="subtle">Explicit opt-in per Pico</span>' : ""}</div><div class="gestures" role="tablist" aria-label="Gesture">${["tap", "hold", "double_tap"].map((gesture) => `<button role="tab" aria-selected="${gesture === this._gesture}" data-gesture="${gesture}">${LABELS[gesture]}</button>`).join("")}</div><div id="behavior"></div><div id="actions"></div></div></div>`;
    body.querySelectorAll("[data-button]").forEach((button) =>
      button.addEventListener("click", () => {
        this._button = button.dataset.button;
        this._buttons(body, type);
        body.querySelector(`[data-button="${this._button}"]`).focus();
      }),
    );
    body.querySelectorAll("[data-gesture]").forEach((button) =>
      button.addEventListener("click", () => {
        this._gesture = button.dataset.gesture;
        this._buttons(body, type);
      }),
    );
    const key = `${this._button}_${this._gesture}`;
    const target = this.remote;
    const value = gestureValue(target, key);
    const choices = this.shared
      ? {
          disabled: "Do nothing",
          custom: "Shared actions",
        }
      : {
          normal: "Normal / inherited behavior",
          custom: "Custom actions",
          disabled: "Do nothing",
          ...(this._button === "stop"
            ? { shared: "Use shared Stop action" }
            : {}),
        };
    const selected = behavior(value, this.shared);
    if (
      this._button === "stop" &&
      (this.shared ||
        assignment(target, this._draft.defaults) === "light" ||
        selected === "color_cycle")
    )
      choices.color_cycle = "Cycle light colors";
    const behaviorBox = body.querySelector("#behavior");
    behaviorBox.innerHTML = `<label class="field">Behavior<select id="behavior-select">${Object.entries(
      choices,
    )
      .map(
        ([v, label]) =>
          `<option value="${v}" ${v === selected ? "selected" : ""}>${esc(label)}</option>`,
      )
      .join("")}</select></label>`;
    this._on(
      "#behavior-select",
      "change",
      (e) => {
        const newValue = e.target.value;
        setGesture(
          target,
          key,
          newValue === "normal"
            ? undefined
            : newValue === "shared"
              ? "default"
              : newValue === "color_cycle"
                ? "color_cycle"
                : [],
        );
        this._changed();
        this._renderActions(
          body.querySelector("#actions"),
          target,
          key,
          newValue,
        );
      },
      body,
    );
    behaviorBox.querySelector("select").disabled = this._state.read_only;
    this._renderActions(body.querySelector("#actions"), target, key, selected);
  }
  _renderActions(host, target, key, selected) {
    const value = gestureValue(target, key);
    if (selected === "color_cycle") {
      host.innerHTML =
        '<div class="behavior-note">Each gesture advances one color for all lights assigned to the triggering Pico. The position belongs to that Pico and survives restarts. Brightness is left to the lights; this action turns them on if needed.</div><div class="cycle-palette"></div>';
      this._palette(host.querySelector(".cycle-palette"), target, this.shared);
      return;
    }
    if (selected === "custom") {
      const placeholder = this._state.light_placeholder;
      const placeholderState = this.hass.states[placeholder?.entity_id];
      const placeholderName =
        placeholderState?.attributes.friendly_name || placeholder?.name;
      const instruction = placeholder?.entity_id
        ? `Select <strong>${esc(placeholderName)}</strong> (<code>${esc(placeholder.entity_id)}</code>) to use the lights assigned to the triggering Pico.`
        : "The light placeholder is not available yet. Reopen the workspace after Pico Link finishes loading.";
      host.innerHTML = `<p class="hint">Build a sequence with actions, delays, conditions, or scripts. ${this.shared ? "Each Pico chooses whether to use this shared sequence." : "Releasing a custom hold lets its sequence finish."}</p><p class="hint placeholder-help">${instruction}</p><div class="action-form"></div>`;
      this._form(
        host.querySelector(".action-form"),
        [{ name: "actions", selector: { action: {} } }],
        { actions: Array.isArray(value) ? this._editorActions(value) : [] },
        (data) => {
          setGesture(
            target,
            key,
            actionEditorResult(
              data.actions || [],
              this._state.light_placeholder?.entity_id,
            ),
          );
          this._changed();
        },
        { actions: "Action sequence" },
      );
    } else {
      let text;
      if (selected === "shared") {
        const actions = gestureValue(this._draft.defaults, key);
        if (actions === "color_cycle") {
          host.innerHTML =
            '<div class="behavior-note">The shared Stop action cycles the lights assigned to this Pico. Each Pico keeps its own position.</div><div class="cycle-palette"></div>';
          this._palette(host.querySelector(".cycle-palette"), target, false);
          return;
        }
        text = actions?.length
          ? `Uses the shared ${LABELS[this._gesture].toLowerCase()} sequence (${actions.length} ${actions.length === 1 ? "action" : "actions"}). Edit it in Shared defaults.`
          : "The shared action is set to Do nothing. This gesture does nothing on this Pico. Change it in Shared defaults to use an action sequence.";
      } else if (selected === "disabled")
        text = this.shared
          ? "Picos that select this shared Stop action do nothing for this gesture. Picos using normal behavior are unchanged."
          : "This gesture does nothing. Other gestures keep their own behavior.";
      else
        text =
          "Uses the normal behavior or an applicable shared default. No local action override is set.";
      host.innerHTML = `<div class="behavior-note">${esc(text)}</div>`;
    }
  }
  _palette(host, target, shared) {
    const starter = this._state.default_color_palette;
    const palette = colorPalette(target, this._draft.defaults, starter);
    const custom = Array.isArray(target.color_palette);
    const editable = shared || custom;
    const rgbHex = (rgb) =>
      `#${rgb.map((v) => v.toString(16).padStart(2, "0")).join("")}`;
    host.innerHTML = `<section class="section palette"><h3>${shared ? "Shared color palette" : "Color palette"}</h3><p class="hint">Colors run in this order. Existing button actions are unchanged until you choose Cycle light colors. After an edit, cycling continues after the last chosen color if it is still present; otherwise it starts at the first color.</p>${shared ? "" : `<label class="field">Palette<select class="palette-source"><option value="default" ${!custom ? "selected" : ""}>Use shared palette</option><option value="custom" ${custom ? "selected" : ""}>Use custom palette</option></select><small>${custom ? "This copy can be edited independently." : "Follows changes in Shared defaults. Choose custom to copy these colors."}</small></label>`}<div class="palette-colors">${palette.map((color, index) => `<div class="palette-row" data-color="${index}"><span class="palette-number">${index + 1}</span><label class="field"><span class="sr-only">Color ${index + 1} type</span><select class="color-type" aria-label="Color ${index + 1} type" ${!editable ? "disabled" : ""}><option value="rgb" ${color.rgb_color ? "selected" : ""}>Color</option><option value="white" ${color.color_temp_kelvin ? "selected" : ""}>White temperature</option></select></label>${color.rgb_color ? `<input class="color-value" aria-label="Color ${index + 1}" type="color" value="${rgbHex(color.rgb_color)}" ${!editable ? "disabled" : ""}>` : `<label class="field"><span class="sr-only">Temperature ${index + 1}</span><input class="color-value" aria-label="Temperature ${index + 1} in Kelvin" type="number" min="1000" max="10000" step="1" value="${color.color_temp_kelvin}" ${!editable ? "disabled" : ""}><small>Kelvin</small></label>`}${editable ? `<div class="palette-tools"><button data-move="-1" aria-label="Move color ${index + 1} up" ${index === 0 ? "disabled" : ""}>↑</button><button data-move="1" aria-label="Move color ${index + 1} down" ${index === palette.length - 1 ? "disabled" : ""}>↓</button><button class="danger" data-delete aria-label="Remove color ${index + 1}" ${palette.length === 1 ? "disabled" : ""}>×</button></div>` : ""}</div>`).join("")}</div>${editable ? `<button class="add-color" ${palette.length >= 32 ? "disabled" : ""}>＋ Add color</button>` : ""}<p class="hint">Real lights must support the chosen colors or white temperatures. Up to 32 entries.</p></section>`;
    const changed = (next) => {
      target.color_palette = next;
      this._changed();
      this._palette(host, target, shared);
    };
    host
      .querySelector(".palette-source")
      ?.addEventListener("change", (event) => {
        selectPalette(
          target,
          event.target.value === "custom",
          this._draft.defaults,
          starter,
        );
        this._changed();
        this._palette(host, target, shared);
      });
    host
      .querySelector(".add-color")
      ?.addEventListener("click", () =>
        changed([...palette, { rgb_color: [255, 255, 255] }]),
      );
    host.querySelectorAll("[data-color]").forEach((row) => {
      const index = Number(row.dataset.color);
      row.querySelector(".color-type").addEventListener("change", (event) => {
        palette[index] =
          event.target.value === "white"
            ? { color_temp_kelvin: 2800 }
            : { rgb_color: [255, 0, 0] };
        changed(palette);
      });
      row.querySelector(".color-value").addEventListener("input", (event) => {
        palette[index] =
          event.target.type === "color"
            ? {
                rgb_color: event.target.value
                  .slice(1)
                  .match(/../g)
                  .map((v) => parseInt(v, 16)),
              }
            : { color_temp_kelvin: Number(event.target.value) };
        // Commit typing to the draft immediately without replacing the focused
        // input. Save validates its range; blur is not required to capture it.
        target.color_palette = clone(palette);
        this._changed();
      });
      row
        .querySelectorAll("[data-move]")
        .forEach((button) =>
          button.addEventListener("click", () =>
            changed(
              movePaletteColor(palette, index, Number(button.dataset.move)),
            ),
          ),
        );
      row
        .querySelector("[data-delete]")
        ?.addEventListener("click", () =>
          changed(palette.filter((_, i) => i !== index)),
        );
    });
    if (this._state.read_only)
      host
        .querySelectorAll("input,select,button")
        .forEach((element) => (element.disabled = true));
  }
  _editorActions(sequence) {
    return actionEditorValue(
      sequence,
      this._state.light_placeholder?.entity_id,
    );
  }
  _actionEditorHass() {
    const hass = this.hass;
    return {
      ...hass,
      callWS: (message) => {
        if (message.type === "execute_script") {
          const sequence = actionEditorResult(
            message.sequence,
            this._state.light_placeholder?.entity_id,
          );
          if (
            actionTargetRows(sequence).some(
              ({ action }) => targetShortcuts(action).length,
            )
          )
            return Promise.reject(
              new Error(
                "Save changes and test with the remote. This placeholder needs a triggering Pico; Run action cannot determine its assigned lights.",
              ),
            );
          return hass.callWS({ ...message, sequence });
        }
        return hass.callWS(message);
      },
    };
  }
  async _form(host, schema, data, onchange, labels = {}) {
    host.innerHTML = '<p class="hint">Loading editor…</p>';
    try {
      await loadEditors();
      if (!host.isConnected) return;
      const form = document.createElement("ha-form");
      const actionEditor = schema.some((field) => field.selector?.action);
      if (actionEditor) form.dataset.picoActionEditor = "true";
      form.hass = actionEditor ? this._actionEditorHass() : this.hass;
      form.schema = schema;
      form.data = data;
      form.disabled = this._state.read_only;
      form.computeLabel = (field) => labels[field.name] || field.name;
      form.addEventListener("value-changed", (e) => {
        e.stopPropagation();
        if (!this._state.read_only && !this._busy) onchange(e.detail.value);
      });
      host.replaceChildren(form);
    } catch (err) {
      if (host.isConnected)
        host.innerHTML = `<p class="error">${esc(err.message)}</p>`;
    }
  }
  _assignment(body) {
    const raw = this.remote;
    const meta = deviceMeta(raw, this._state.catalog);
    body.innerHTML = `<div class="section"><h3>Remote identity</h3><div id="identity"></div><details class="device-details" id="advanced"><summary>Advanced</summary><label class="field" for="device-id">Home Assistant device ID</label><div class="device-id-row"><input id="device-id" type="text" value="${esc(raw.device_id)}" readonly spellcheck="false"><button id="copy-device-id" ${raw.device_id ? "" : "disabled"}>Copy</button></div><small id="copy-status" role="status"></small><div id="layout"></div><p class="hint">Automatic uses the model stored by Lutron. Select a layout only when needed.</p></details><div id="targets"></div></div>`;
    this._on(
      "#copy-device-id",
      "click",
      async () => {
        const input = body.querySelector("#device-id");
        const status = body.querySelector("#copy-status");
        const button = body.querySelector("#copy-device-id");
        let copied = false;
        if (navigator.clipboard?.writeText) {
          try {
            await navigator.clipboard.writeText(input.value);
            copied = true;
          } catch {
            // Local HTTP installations may not expose or allow the clipboard API.
          }
        }
        if (!copied) {
          input.focus();
          input.select();
          try {
            copied = document.execCommand("copy");
          } catch {
            // Keep the ID selected for manual copying if the browser blocks it.
          }
        }
        status.textContent = copied
          ? "Device ID copied."
          : "Select and copy the device ID manually; the browser blocked copying.";
        if (copied) button.focus();
      },
      body,
    );
    this._form(
      body.querySelector("#identity"),
      [
        {
          name: "device_id",
          required: true,
          selector: { device: { integration: "lutron_caseta" } },
        },
      ],
      { device_id: raw.device_id },
      (data) => {
        raw.device_id = data.device_id;
        this._changed();
        this._renderDetail();
      },
      { device_id: "Lutron remote" },
    );
    this._form(
      body.querySelector("#layout"),
      [
        {
          name: "layout",
          selector: {
            select: {
              options: [
                { value: "automatic", label: "Automatic" },
                ...Object.entries(TYPES).map(([value, label]) => ({
                  value,
                  label,
                })),
              ],
              mode: "dropdown",
            },
          },
        },
      ],
      { layout: raw.type || "automatic" },
      (data) => {
        if (data.layout === "automatic") delete raw.type;
        else raw.type = data.layout;
        this._changed();
        this._renderDetail();
        this.shadowRoot.querySelector("#advanced").open = true;
      },
      { layout: "Pico layout" },
    );
    const targets = body.querySelector("#targets");
    if (meta.type === "4B") {
      targets.innerHTML =
        "<h3>Targets are set per action</h3><p>For scene Picos, choose explicit targets inside each button action.</p>";
      return;
    }
    const domain = assignment(raw, this._draft.defaults);
    const value =
      raw[FIELDS[domain]] ?? this._draft.defaults[FIELDS[domain]] ?? [];
    targets.innerHTML = `<h3>What does this Pico control?</h3><div class="domain-buttons">${Object.keys(
      FIELDS,
    )
      .map(
        (d) =>
          `<button data-domain="${d}" aria-pressed="${d === domain}">${LABELS[d]}</button>`,
      )
      .join(
        "",
      )}</div><div id="entities"></div><p class="hint">Assign one kind of device here. Custom actions can target other devices.</p>`;
    targets.querySelectorAll("[data-domain]").forEach((button) => {
      button.disabled = this._state.read_only;
      button.addEventListener("click", () => {
        this._chosenDomain = button.dataset.domain;
        this._entityPicker(targets, raw, this._chosenDomain, []);
        targets
          .querySelectorAll("[data-domain]")
          .forEach((b) => b.setAttribute("aria-pressed", b === button));
      });
    });
    this._entityPicker(
      targets,
      raw,
      domain,
      typeof value === "string" ? [value] : value,
    );
  }
  _entityPicker(host, raw, domain, value) {
    this._form(
      host.querySelector("#entities"),
      [
        {
          name: "entities",
          required: true,
          selector: { entity: { domain, multiple: true } },
        },
      ],
      { entities: value },
      (data) => {
        assignEntities(raw, domain, data.entities || []);
        this._changed();
      },
      { entities: LABELS[domain] },
    );
  }
  _numbers(body, keys, heading, description, cover = false) {
    const target = this.remote;
    body.innerHTML = `<div class="section"><h3>${esc(heading)}</h3><p>${esc(description)}</p><div class="settings-grid">${keys
      .map((key) => {
        const [min, max, fallback, unit] = this._state.numbers[key];
        const inherited = this.shared
          ? fallback
          : (this._draft.defaults[key] ?? fallback);
        return `<label class="field number-field">${esc(numberLabels[key])}<div><input data-key="${key}" type="number" min="${min}" max="${max}" step="1" value="${esc(target[key] ?? "")}" placeholder="${esc(inherited)}" aria-label="${esc(numberLabels[key])}"><span>${unit}</span></div><small>${this.shared ? "Built-in" : "Inherited"}: ${inherited} ${unit} · Leave blank to use it</small></label>`;
      })
      .join(
        "",
      )}</div>${cover ? '<label class="field">Reverse shade direction<select id="inverted"><option value="inherit">Use default</option><option value="yes">Yes</option><option value="no">No</option></select></label>' : ""}${!keys.length && !cover ? "<p>No additional settings for this device type.</p>" : ""}</div>`;
    body.querySelectorAll("input[data-key]").forEach((input) => {
      input.disabled = this._state.read_only;
      input.addEventListener("input", () => {
        if (input.value === "") delete target[input.dataset.key];
        else target[input.dataset.key] = Number(input.value);
        this._changed();
      });
    });
    if (cover) {
      const select = body.querySelector("#inverted");
      select.value =
        target.cover_inverted === undefined
          ? "inherit"
          : target.cover_inverted
            ? "yes"
            : "no";
      select.disabled = this._state.read_only;
      select.addEventListener("change", () => {
        if (select.value === "inherit") delete target.cover_inverted;
        else target.cover_inverted = select.value === "yes";
        this._changed();
      });
    }
  }
  _run(body) {
    const target = this.remote;
    const inherited = this.shared ? {} : this._draft.defaults;
    body.innerHTML = `<div class="section"><h3>When another button is pressed</h3><p>One execution policy covers all custom actions on ${this.shared ? "each Pico that inherits it" : "this Pico"}. Other Picos run independently.</p><label class="field">Run mode<select id="mode"><option value="inherit">Use default — ${esc(inherited.mode || "single")}</option>${Object.entries(
      modeLabels,
    )
      .map(([value, label]) => `<option value="${value}">${label}</option>`)
      .join(
        "",
      )}</select></label><div class="behavior-note" id="mode-help"></div><div class="settings-grid"><label class="field">Maximum runs<input id="max" type="number" min="1" step="1" value="${esc(target.max ?? "")}" placeholder="${inherited.max || 10}"><small>For queued or parallel; queued includes the active run. Blank inherits ${inherited.max || 10}.</small></label><label class="field">When a run is rejected<select id="max-exceeded"><option value="inherit">Use default — ${esc(inherited.max_exceeded || "warning")}</option>${["silent", "debug", "info", "warning", "error", "critical"].map((v) => `<option value="${v}">${v[0].toUpperCase() + v.slice(1)}</option>`).join("")}</select><small>Silent suppresses the log message; the extra run is still rejected.</small></label></div><p class="hint">Continue on error is chosen on individual actions in the action editor.</p></div>`;
    const help = {
      single: "New custom gestures are ignored while a sequence is running.",
      restart:
        "A new custom gesture cancels the earlier sequence. Normal device commands also cancel that Pico's unfinished sequence.",
      queued: "New sequences wait their turn, up to the limit.",
      parallel:
        "Sequences run at the same time, up to the limit. They can send competing commands.",
    };
    const mode = body.querySelector("#mode");
    mode.value = target.mode || "inherit";
    const showHelp = () => {
      body.querySelector("#mode-help").textContent =
        help[target.mode || inherited.mode || "single"];
    };
    showHelp();
    mode.addEventListener("change", () => {
      if (mode.value === "inherit") delete target.mode;
      else target.mode = mode.value;
      showHelp();
      this._changed();
    });
    const max = body.querySelector("#max");
    max.addEventListener("input", () => {
      if (!max.value) delete target.max;
      else target.max = Number(max.value);
      this._changed();
    });
    const severity = body.querySelector("#max-exceeded");
    severity.value = target.max_exceeded?.toLowerCase() || "inherit";
    severity.addEventListener("change", () => {
      if (severity.value === "inherit") delete target.max_exceeded;
      else target.max_exceeded = severity.value;
      this._changed();
    });
    body.querySelectorAll("input, select").forEach((el) => {
      el.disabled = this._state.read_only;
    });
  }
  _dialog(content) {
    const dialog = document.createElement("dialog");
    dialog.innerHTML = content;
    this.shadowRoot.append(dialog);
    dialog.addEventListener("close", () => dialog.remove());
    dialog.showModal();
    return dialog;
  }
  _confirm(title, message, label, action) {
    const dialog = this._dialog(
      `<h2>${esc(title)}</h2><p>${esc(message)}</p><div class="dialog-actions"><button id="cancel">Cancel</button><button id="confirm" class="primary">${esc(label)}</button></div>`,
    );
    dialog
      .querySelector("#cancel")
      .addEventListener("click", () => dialog.close());
    dialog.querySelector("#confirm").addEventListener("click", () => {
      dialog.close();
      action();
    });
  }
  _add() {
    if (this._state.read_only || this._busy) return;
    const used = new Set(this._draft.devices.map((d) => d.device_id));
    const available = this._state.catalog.filter((d) => !used.has(d.id));
    const dialog = this._dialog(
      '<h2>Add a Pico</h2><p>Choose a remote from your Lutron Caséta integration.</p><label class="field">Find a remote<input id="find" type="search" placeholder="Search name or room"></label><label class="check"><input id="unknown" type="checkbox">Show unrecognized Lutron devices</label><div id="available" class="available"></div><div class="dialog-actions"><button id="cancel">Cancel</button></div>',
    );
    const render = () => {
      const query = dialog.querySelector("#find").value.toLowerCase();
      const rows = available.filter(
        (d) =>
          (d.type || dialog.querySelector("#unknown").checked) &&
          `${d.name} ${d.area}`.toLowerCase().includes(query),
      );
      dialog.querySelector("#available").innerHTML =
        rows
          .map(
            (d) =>
              `<button class="available-row" data-id="${esc(d.id)}"><strong>${esc(d.name)}</strong><small>${esc(d.area || TYPES[d.type] || "Choose a layout after adding")}</small><span>＋</span></button>`,
          )
          .join("") ||
        "<p>No available Picos match. Check that the remote is in the Lutron Caséta integration.</p>";
      dialog.querySelectorAll("[data-id]").forEach((button) =>
        button.addEventListener("click", () => {
          const device = available.find((d) => d.id === button.dataset.id);
          const raw = { device_id: device.id };
          // Mask inherited assignments for scene remotes without changing defaults.
          if (device.type === "4B")
            for (const field of Object.values(FIELDS)) raw[field] = [];
          this._draft.devices.push(raw);
          this._selected = this._draft.devices.length - 1;
          this._tab = device.type === "4B" ? "buttons" : "assignment";
          this._button = "on";
          this._gesture = "tap";
          dialog.close();
          this._renderDetail();
          this._changed();
        }),
      );
    };
    dialog.querySelector("#find").addEventListener("input", render);
    dialog.querySelector("#unknown").addEventListener("change", render);
    dialog
      .querySelector("#cancel")
      .addEventListener("click", () => dialog.close());
    render();
  }
  async _save() {
    if (this._state.read_only || this._busy) return;
    for (const input of this.shadowRoot.querySelectorAll("input"))
      if (!input.reportValidity()) return;
    this._busy = true;
    this._error = "";
    this._message = "";
    this._status();
    // Capture the whole document so action edits cannot race a pending save.
    const document = clone(this._draft);
    this.shadowRoot.querySelector(".workspace").inert = true;
    try {
      const state = await this.hass.callWS({
        type: "pico_link/save",
        document,
        revision: this._state.revision,
      });
      const selected = this._selected;
      this._accept(state);
      this._selected = selected;
      this._message =
        "Settings saved. Pico Link is reloading its remotes; no Home Assistant restart is needed.";
      this._conflict = false;
    } catch (err) {
      this._error = err.message || String(err);
      this._conflict = err.code === "conflict";
    } finally {
      this._busy = false;
      this.shadowRoot.querySelector(".workspace").inert = false;
      this._renderList();
      this._renderDetail();
      this._status();
    }
  }
}
if (!customElements.get("pico-link-panel"))
  customElements.define("pico-link-panel", PicoLinkPanel);
