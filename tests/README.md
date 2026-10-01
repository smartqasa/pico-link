# Pico Link regression tests

This suite checks Pico Link's documented behavior before changes reach users.
It runs the real configuration parser, setup, event handling, and action code
inside a Home Assistant test instance. The Lutron bridge and device services
are replaced with test doubles that record commands. No physical devices are
operated and no running Home Assistant instance is needed.

## Run locally

Use Python 3.14. From the repository root, create and activate a virtual
environment, then install the pinned test dependencies:

```sh
python3.14 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-test.txt
python -m pytest -q
```

On Windows, create the environment with `py -3.14 -m venv .venv` and activate it
with `.venv\Scripts\Activate.ps1` in PowerShell. The remaining commands are the
same.

Run the same checks as GitHub:

```sh
python -m ruff check custom_components/pico_link tests
python -m pytest -q --cov=custom_components.pico_link --cov-branch --cov-report=term-missing
```

To focus on one area while developing:

```sh
python -m pytest -q tests/test_gestures.py
```

## Coverage areas

| File | Behavior checked |
| --- | --- |
| `test_config_flow.py` | Native setup and options flows, explicit configuration method, YAML import/cancellation, stored action round trips, inherited settings, exclusive controller ownership, options reload, and shutdown cleanup |
| `test_light_placeholder.py` | Registered light capabilities, startup identity reuse, name collisions and renames, per-Pico expansion of shared and custom targets, mixed/nested sequences, invalid assignments, reloads, and direct-use errors |
| `test_light_brightness.py` | Minimum brightness from off, rapid taps with delayed state feedback, upward holds, normal On brightness, and brightness limits |
| `test_configuration.py` | Timing defaults and overrides, normalization, invalid configurations, device-name precedence and ambiguity, entity deduplication, and action placeholders |
| `test_2brl.py` | Four-button Raise/Lower profile, native light commands, ignored Stop events, and rejected Stop configuration |
| `test_type_detection.py` | Supported registry model formats, unknown/missing/non-Lutron models, explicit-type precedence, name/ID resolution, unchanged event checks, isolation of invalid remotes, and metadata changes between setups |
| `test_setup_and_events.py` | Full HA setup, invalid and duplicate entries, event filtering, independent remotes, multiple targets, and shutdown cancellation |
| `test_device_controls.py` | On/Off behavior for all four domain-controlling Pico models; shade position/direction, fan speeds/direction, volume limits/mute, and switches |
| `test_gestures.py` | Tap/hold distinctions, release and direction changes, shade stop ordering, natural ramp limits, and concurrent remotes |
| `test_script_engine.py` | Real HA script syntax, cross-button modes, per-Pico limits, error compatibility, native Off interruption, cancellation, reuse, and cleanup |
| `test_custom_actions.py` | All four scene buttons, middle-button overrides, ordered completion, target/data preservation, service errors, and interrupted sequences |
| `test_button_overrides.py` | Tap/hold overrides on every supported button, native fallback, legacy precedence, empty lists, release timing, cover stop ordering, shutdown, and five concurrent remotes |
| `test_double_tap.py` | Every model/button, single-tap delay and fallback, native/custom holds, timing inheritance, slow/repeated taps, cross-button ordering, duplicate events, shutdown, cover stops, and concurrent remotes |
| `test_stop_defaults.py` | Explicit Stop default opt-ins across mixed models, per-device replacement and disabling, per-remote placeholders, interchangeable legacy tap defaults, name precedence, empty shared gestures and invalid default validation |

The new integration tests enter through Home Assistant's setup interface and
send Pico events through its event bus. Assertions check outgoing service
commands and observable errors rather than private implementation details.
Hold tests use real timers with short configured intervals and wait for recorded
commands; they do not replace the hold or ramp logic with a mock. Each test has
a timeout so a stuck gesture fails instead of hanging the entire run.

The shared `pico` harness and brightness fixture run their behavior tests twice:
once with an explicit type and once with the type omitted and a real Home
Assistant device registry record supplying the model. This checks the same
tap, hold, double-tap, defaults, concurrency, and shutdown behavior through both
configuration paths. Detection-specific tests also cover startup failures and
confirm that button handling no longer needs the registry after setup.

## Automatic GitHub checks

The `Tests` workflow runs on pushes to `beta` and `main`, and on pull requests
targeting either branch. It installs the same dependencies, runs lint checks,
and runs the suite with a coverage report. Review failures in the repository's
Actions tab before promoting a change. The workflow runs tests only; it does
not deploy updates. The `main` ruleset requires the **Pico Link regression
tests** check from GitHub Actions before a promotion pull request can merge.
See the [promotion workflow](#promoting-beta-to-main).

## Promoting beta to main

Use the two existing branches: develop directly on `beta`, then promote tested
changes to `main` through GitHub. Temporary development branches are optional.

1. Commit and push changes to `beta`.
2. Wait for the **Pico Link regression tests** check to pass and test the
   affected behavior on your Home Assistant hardware.
3. [Open the beta-to-main comparison](https://github.com/smartqasa/pico-link/compare/main...beta)
   and create a pull request, or open the existing promotion pull request.
4. Review the changes and wait for the pull request's required check to pass.
   If GitHub asks you to update the branch, use **Update branch** to bring
   `main` into `beta`, then wait for the checks again.
5. Choose **Create a merge commit** and confirm the merge. Keep `beta` for the
   next development cycle; do not delete it.

The `main` ruleset requires a pull request and the GitHub Actions regression
check against the current base branch. No approving review from another person
is required. Force pushes and deletion are blocked, with no bypass actors.
Direct changes to `beta` remain allowed.

The former `promote.sh` script has been retired. GitHub now provides the
promotion review and merge step. Publishing a versioned GitHub release for
HACS remains a separate operation.

## Adding a regression test

1. Describe the expected behavior independently of the implementation.
2. Add a test that reproduces the problem and fails before the fix.
3. Fix the behavior, then run the focused test and the full suite.
4. Keep the test so later changes can be checked against the same expectation.

For event-driven tests, use the `pico` fixture in `conftest.py`. Configure the
remote with `await pico.setup(...)`, send a tap with `pico.tap(...)`, and assert
the recorded `pico.calls`. During an active hold, wait with
`await pico.next_call()` and send release before calling `await pico.drain()`.
Otherwise draining waits for the active ramp to reach its endpoint.

## Limits

The suite runs on Home Assistant 2026.9.1 and the supported minimum, 2026.4.0,
using Python 3.14. To test the minimum locally, create a separate environment
and install `requirements-test-minimum.txt` instead of `requirements-test.txt`.
GitHub runs both environments. Passing these two versions does not prove every
intermediate version; keep checking API changes and physical-device behavior.

The minimum was reviewed for the 1.0 UI beta. Script modes and branching are
older features (HA 0.113, July 2020), and per-action `continue_on_error` arrived
in May 2022. The newer concrete dependency is Paddle Pico support:
`pylutron-caseta` 0.27.0 added `PaddleSwitchPico` button devices, and Home
Assistant 2026.4.0 includes that version. HA 2026.3.1 still includes 0.26.0.
The real setup, options, registry, script validation/execution, and controller
tests are run against April's release rather than inferring compatibility
from the former untested 2023.1.0 declaration.

Sources: [script modes](https://www.home-assistant.io/blog/2020/07/22/release-113/),
[action error handling](https://www.home-assistant.io/blog/2022/05/04/release-20225/),
[Lutron library change](https://github.com/gurumitts/pylutron-caseta/compare/v0.26.0...v0.27.0),
and [HA April Lutron manifest](https://github.com/home-assistant/core/blob/2026.4.0/homeassistant/components/lutron_caseta/manifest.json).

Automated checks do not measure Lutron radio reliability, physical light or
shade response, network latency, or whether dimming feels right. Before release,
also test the affected behavior on real hardware. Coverage reports identify
untested paths; a high percentage alone does not prove correct behavior.

## Testing button overrides on hardware

Compare a remote with no overrides against one with a single override. Confirm
unconfigured buttons retain their response timing. For each configured button,
test a quick tap, release just before the hold threshold, and a long hold.
The custom hold must run once and release must not run the tap as well.

Check that a Raise/Lower tap override retains normal dimming on hold, including
the configured minimum from off. Its first hold step now follows the hold
threshold, since the tap and hold are exclusive. Check release and direction
changes, and test multiple remotes concurrently. On covers, confirm an
interrupted continuous hold stops before the replacement action runs.

The automated concurrency tests use service doubles; they do not establish
bridge throughput, real-world latency, or physical-device acceptance.

For double tap, configure one button and compare it with an unconfigured
button. Check the default 300 ms gap from release to the next press and a
per-Pico timing override. One tap should wait and run once; two quick taps
should run only the double action after the second release. Try slow taps,
three/four rapid taps, and a tap followed by a hold. The hold must not also
trigger tap/double-tap actions. If no hold exists, a long press should run
the single action once at the hold threshold.

Check that default brightness/volume holds still ramp at the hold threshold
and stop on release, that changing buttons does not leave delayed commands
behind, and that separate remotes respond independently. A restart during a
pending tap must cancel it. Radio and network latency can affect the gap
observed by Home Assistant, so physical testing remains necessary.
