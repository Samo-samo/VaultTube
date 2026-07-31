# File Structure

## Overview

VaultTube follows a simple and modular project structure.

The project's directory layout is intentionally kept lightweight and easy to understand. New files and subdirectories may be introduced when they provide clear architectural or organizational benefits.

The root structure should remain stable unless there is a justified architectural reason to modify it.

---

## Root Directory Structure

```text
VaultTube/

├── AI/
├── assets/
├── docs/
├── src/
├── .gitignore
├── LICENSE
└── README.md
```

---

## Root Directory Responsibilities

### AI/

Contains AI-related working files and instructions used during development.

Examples:

* AI instructions
* Project context files
* Prompt templates
* Current development tasks

Notes:

* This directory is intended for local development use.
* The entire directory should be excluded from version control.

---

### assets/

Contains project assets.

Examples:

* Icons
* Images
* Screenshots
* Future graphical resources

The assets directory should remain organized and avoid storing unrelated files.

---

### docs/

Contains all official project documentation.

Examples:

* Project vision
* Architecture documentation
* Roadmap
* Coding standards
* Technical documentation

Documentation files are considered the primary source of truth for architectural and development decisions.

---

### src/

Contains all source code used by the project.

The source directory is expected to grow as development progresses.

Suggested structure:

```text
src/

├── extension/
├── native/
└── shared/
```

---

## Source Directory Responsibilities

### extension/

Contains browser extension source files.

Examples:

* Popup UI
* Dashboard UI
* Background scripts
* Content scripts
* Settings pages
* Localization files
* Manifest configuration

The extension layer should remain lightweight and focused on user interaction.

---

### native/

Contains the Python backend implementation.

Examples:

* Native Messaging
* Download engine
* Queue manager
* Database operations
* File management
* System utilities

The native layer is responsible for the application's business logic.

---

### shared/

Contains resources shared across different components when necessary.

Examples:

* JSON schemas
* Constants
* Shared configuration files
* Common utilities

This directory should only contain resources that are genuinely shared between multiple systems.

---

## Documentation Rules

The following rules apply to the project's file structure:

* Keep the root directory clean and minimal.
* Avoid unnecessary nesting.
* Create new directories only when they improve maintainability.
* Prefer modular organization over feature duplication.
* Keep related files together.
* Avoid introducing temporary or experimental files into the repository.

---

## AI-Assisted Development Rules

AI-assisted tools may:

* Create files inside existing modules when requested.
* Create supporting files related to an approved feature.
* Refactor existing structures when necessary.

AI-assisted tools should not:

* Modify the root project structure without approval.
* Introduce new architectural layers.
* Create undocumented systems or modules.
* Modify official documentation unless explicitly requested.

Architectural decisions are always made through project documentation before implementation.

---

## Future Expansion

The project structure is intentionally designed to support future growth without unnecessary complexity.

Additional files or directories may be introduced if they:

* Improve maintainability.
* Support modular development.
* Provide clear organizational benefits.

Future additions should remain consistent with the project's development philosophy and architectural principles.

---

## Final Notes

VaultTube favors a simple and maintainable file structure.

The project's organization should remain easy to understand for:

* Contributors
* AI-assisted development tools
* Future maintainers
* New developers joining the project

Clarity and simplicity should always take priority over excessive directory organization.
