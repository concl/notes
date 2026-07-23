
vscode-python-env has a bug where it tries to use shell integration to run a source command
- The bug may be in the source code for vscode.

Title: shellIntegration.executeCommand() times out when command modifies PS1 (e.g. `source activate`)

---

**Describe the bug**

When VS Code's shell integration is active, `shellIntegration.executeCommand()` reports a "Shell execution timed out" error for commands that source scripts which modify `PS1`. The command itself succeeds — the timeout is a false positive caused by shell integration losing its completion-tracking markers.

**To Reproduce**

1. Open a Python project with a selected venv (so the Python Environments extension auto-activates it in new terminals)
2. Open a new integrated terminal
3. Observe in the extension host output:
```

[error] Shell execution timed out: source /Users/.../.venv/bin/activate [info] Terminal is activated: /Users/.../.venv/bin/python

```

The terminal IS correctly activated — `which python` confirms the venv path. But the error fires because the command took ~3 seconds to "complete" from shell integration's perspective, even though the actual activation was near-instant.

**Root cause**

Shell integration detects command completion by watching for OSC 633 escape sequences that are embedded in `PS1`. When a command runs `source activate` (or `nvm use`, `conda activate`, `fnm use`, etc.), the sourced script rewrites `PS1` to add an environment indicator. This new `PS1` string does not contain the shell integration markers, so the "command finished" signal never arrives. Shell integration waits until its configurable timeout, then reports the error.

**Affected scenarios**

Any command sourced from a `.sh`/`.bash`/`.zsh` script that modifies `PS1`:
- `source .venv/bin/activate` (Python venv)
- `nvm use` (Node version manager)
- `conda activate <env>`
- `fnm use` (Fast Node Manager)
- Custom shell functions or hooks in `.zshrc`/`.bashrc`

**Suggested fix**

Shell integration should snapshot the OSC 633 prompt markers **before** executing a command, and use the snapshot for completion detection rather than reading `PS1` live during execution. The markers are only needed to recognize the end-of-command boundary — they don't need to survive the command itself.

Alternatively, if snapshotting is infeasible, the `executeCommand` API could accept an option to disable completion tracking (opt-in `sendText`-style behavior), so callers that don't need output capture can avoid the timeout.

**Symptom in the wild**

The Python Environments extension (`ms-python.vscode-python-envs`) works around this unintentionally: it has a fallback codepath (`activateLegacy`) that uses raw `sendText()` when shell integration is unavailable. When shell integration IS available, it takes the "preferred" `executeCommand()` path and hits this bug. The extension's activation succeeds either way because the command ran — it's purely a detection failure in shell integration.