# Coding Standards

## Overview

VaultTube follows a simplicity-first approach to coding standards.

Code should prioritize:

* Readability
* Maintainability
* Consistency
* Simplicity
* Modularity

Readable code is always preferred over clever or overly optimized code.

---

## General Rules

The following rules apply to all source code:

* Write self-explanatory code whenever possible.
* Avoid unnecessary abstractions.
* Prefer simple and maintainable solutions.
* Keep functions and modules focused on a single responsibility.
* Do not introduce unnecessary dependencies.
* Document complex logic when necessary.
* Maintain consistency throughout the codebase.

---

## Language Standards

### JavaScript

Requirements:

* Use modern JavaScript features when appropriate.
* Prefer native browser APIs over third-party libraries.
* Avoid unnecessary polyfills.
* Keep extension-related logic lightweight.

Avoid:

* Large utility libraries.
* JavaScript frameworks.
* Overly complex patterns.

---

### Python

Requirements:

* Follow modern Python best practices.
* Keep backend modules independent and modular.
* Prefer standard library solutions whenever possible.
* Use clear and descriptive naming conventions.

Avoid:

* Unnecessary packages.
* Over-engineered implementations.
* Hidden or overly complex backend logic.

---

## Naming Conventions

### Files

Use:

```text
download_manager.py
queue_manager.py

settings_page.js
popup_manager.js
```

Rules:

* Use lowercase characters.
* Use snake_case for filenames.
* Avoid spaces and special characters.
* Use descriptive names.

---

## Variables

Use descriptive names.

Good examples:

```text
download_directory
selected_format
queue_item
database_version
```

Avoid:

```text
x
tmp
data1
test123
```

---

## Functions

Function names should clearly describe their purpose.

Examples:

```text
start_download()
pause_download()
save_settings()
load_history()
```

Functions should:

* Perform a single task.
* Be easy to understand.
* Avoid unnecessary side effects.

---

## Modules

Each module should have a clearly defined responsibility.

Examples:

* Queue Manager
* Download Engine
* Database Manager
* Localization Manager
* Settings Manager

Avoid combining unrelated responsibilities into a single module.

---

## Comments

Comments should explain:

* Why something exists.
* Why a specific implementation was chosen.
* Non-obvious behavior.

Comments should not explain what the code already makes obvious.

Prefer:

```text
# FFmpeg merging is performed here because yt-dlp does not provide
# the desired output format in this workflow.
```

Avoid:

```text
# Creates a variable called x.
```

---

## Code Organization

Prefer:

```text
Small modules
Small functions
Clear responsibilities
```

Avoid:

```text
Large files
Large functions
Mixed responsibilities
```

When a file becomes difficult to understand or maintain, consider splitting it into smaller modules.

---

## Dependency Rules

Before adding a new dependency, ask:

* Is it truly necessary?
* Can the standard library solve the problem?
* Does it significantly improve maintainability?
* Does it justify the additional complexity?

New dependencies should be introduced only when there is a clear benefit.

---

## UI Standards

The user interface should remain:

* Lightweight
* Responsive
* Consistent
* Accessible
* Easy to maintain

Avoid:

* UI frameworks
* CSS frameworks
* Heavy component libraries

VaultTube intentionally uses:

* HTML
* CSS
* JavaScript

for all extension interfaces.

---

## Error Handling

Requirements:

* Handle expected failures gracefully.
* Provide meaningful error messages.
* Avoid silent failures whenever possible.
* Keep error handling consistent.

Examples include:

* Missing FFmpeg installation.
* Native Messaging failures.
* Download errors.
* Database errors.
* Invalid user settings.

---

## AI-Assisted Development Rules

AI-generated code should:

* Follow all project coding standards.
* Respect the documented architecture.
* Avoid introducing undocumented systems.
* Avoid unnecessary complexity.
* Preserve existing file structures whenever possible.

AI-assisted tools must not:

* Add dependencies without approval.
* Modify documentation unless requested.
* Make architectural decisions.
* Introduce frameworks or libraries without justification.

---

## Performance Guidelines

Prioritize:

* Simplicity
* Stability
* Maintainability

Do not sacrifice readability for minor performance improvements unless a measurable performance issue exists.

Premature optimization should be avoided.

---

## Final Principles

VaultTube follows the following development philosophy:

> Simple code is better than clever code.

Whenever multiple implementations are possible, prefer the one that is:

* Easier to understand.
* Easier to maintain.
* Easier to document.
* Easier for contributors and AI tools to work with.

Long-term maintainability is always more important than short-term convenience.
