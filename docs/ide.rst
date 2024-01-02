Visual Studio Code
==================

Visual Studio Code is the recommended Integrated Development Environment for Python.

It comes with the following integrations

- Git and GitLab
- Code Testing
- Debugging Configurations
- Terminal
- Outline Views
- Refactoring and Reformatting Code
- and lots more

Download and Install
--------------------

1. Visit https://code.visualstudio.com/
2. Click "Download for Windows Stable Build" button to initiate download.
3. Run the downloaded **VSCodeUserSetup.exe**
4. Click next till you complete the installation.

Installing Extensions
---------------------

Once VS Code is installed, we need to perform an One Time installation of
Extensions.

Click on the Extension menu from the sidebar or press **Ctrl + Shift + X**

Search for an extension and click install button

Productivity Extensions
-----------------------

1. `GitHub Copilot (by GitHub) <https://marketplace.visualstudio.com/items?itemName=GitHub.copilot>`_
2. `GitLens (by GitKraken) <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_
3. `Gitlab Workflow (by GitLab) <https://marketplace.visualstudio.com/items?itemName=GitLab.gitlab-workflow>`_
4. `Remote Explorer (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-explorer>`_
5. `Powershell (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-vscode.PowerShell>`_
6. `Docker (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker>`_
7. `WSL (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl>`_
8. `Bookmarks (by Alessandro Fragnani) <https://marketplace.visualstudio.com/items?itemName=alefragnani.Bookmarks>`_

Python Related Extensions
-------------------------

1. `Python (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`_
2. `isort (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-python.isort>`_
3. `Black Formatter (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>`_
4. `Pylance (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance>`_
5. `Jupyter (by Microsoft) <https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter>`_
6. `autoDocstring (by Nils Werner) <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_

Configuring Visual Studio Code
------------------------------

Open the file "**%appdata%\\code\\user\\settings.json**" and paste the
following recommended settings (use **Copy button** instead of manual select)::

    {
        "editor.rulers": [
            79, 88
        ],
        "files.trimFinalNewlines": true,
        "files.trimTrailingWhitespace": true,
        "python.defaultInterpreterPath": "%localappdata%\\Programs\\Python\\Python310\\python.exe",
        "workbench.colorCustomizations": {
            "editorRuler.foreground": "#817f80"
        },
        "workbench.editorAssociations": {
            "*.ipynb": "jupyter-notebook"
        },
        "editor.multiCursorModifier": "ctrlCmd",
        "python.linting.pylintArgs": [
            "--generated-members",
            "from_json,query"
        ],
        "editor.minimap.enabled": false,
        "notebook.cellToolbarLocation": {
            "default": "right",
            "jupyter-notebook": "left"
        },
        "security.workspace.trust.untrustedFiles": "open",
        "editor.inlineSuggest.enabled": true,
        "html.format.wrapLineLength": 88,
        "editor.wordWrap": "bounded",
        "editor.wordWrapColumn": 88,
        "editor.wrappingIndent": "indent",
        "vscode-edge-devtools.mirrorEdits": true,
        "outline.showVariables": false,
        "terminal.integrated.enableMultiLinePasteWarning": false,
        "python.venvFolders": [
            "%userprofile%\\.pyenvs\\Python39",
            "%userprofile%\\.pyenvs\\Python310"
        ],
        "gitlens.integrations.enabled": true,
        "telemetry.telemetryLevel": "error",
        "editor.fontSize": 16,
        "python.analysis.autoImportCompletions": false,
        "git.suggestSmartCommit": false,
        "liveServer.settings.donotShowInfoMsg": true,
        "python.venvPath": "%userprofile%/.pyenvs/Python39,%userprofile%/.pyenvs/Python310",
        "python.disableInstallationCheck": true,
        "editor.unicodeHighlight.nonBasicASCII": false,
        "redhat.telemetry.enabled": true,
        "editor.minimap.renderCharacters": false,
        "editor.minimap.enabled": false,
        "gitlens.views.remotes.branches.layout": "list",
        "git.ignoreRebaseWarning": true,
        "diffEditor.ignoreTrimWhitespace": false,
        "workbench.colorTheme": "Default Dark+",
        "vscode-edge-devtools.webhint": false,
        "gitlens.gitCommands.skipConfirmations": [
            "fetch:command",
            "switch:command",
            "push:command"
        ],
        "terminal.integrated.profiles.windows": {
            "PowerShell": {
                "source": "PowerShell",
                "overrideName": true,
                "icon": "terminal-powershell",
                "args": [
                    "-ExecutionPolicy",
                    "Bypass"
                ]
            }
        },
        "terminal.integrated.defaultProfile.windows": "Command Prompt",
    }
