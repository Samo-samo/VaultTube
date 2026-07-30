# VaultTube - Modules Document

## Overview

This document defines all core modules planned for VaultTube v1.0 and the responsibilities of each module.

Every module must follow the Single Responsibility Principle and remain as independent as possible.

---

## Core Modules

### Download Manager

Responsible for:

* Video downloads.
* Audio downloads.
* Subtitle downloads.
* Download option handling.
* yt-dlp integration.
* ffmpeg processing.

The Download Manager must not handle:

* Queue logic.
* Database operations.
* UI operations.

---

### Queue Manager

Responsible for:

* Download queue management.
* Pause and resume functionality.
* Concurrent download limits.
* Download prioritization.
* Queue status tracking.

The Queue Manager should remain independent from the Download Manager implementation details.

---

### Storage Manager

Responsible for:

* Download locations.
* Storage profiles.
* Folder organization.
* Storage calculations.
* Disk usage information.

Supports:

* Single-folder mode.
* Multi-folder mode.
* Future portable mode.

---

### History Manager

Responsible for:

* Download history.
* Search and filtering.
* Media status tracking.
* History cleanup operations.

Supports:

* Channel filtering.
* File size filtering.
* Media type filtering.

---

### Notes Manager

Responsible for:

* Media notes.
* User comments.
* Timestamp entries.
* Future annotation support.

The Notes system must be optional and fully independent.

---

### Database Manager

Responsible for:

* SQLite communication.
* Database initialization.
* Database migrations.
* Database validation.

The Database Manager acts as the only layer allowed to directly communicate with SQLite.

---

### Settings Manager

Responsible for:

* User settings.
* Feature flags.
* UI preferences.
* Download preferences.
* Localization preferences.

Settings should be fully exportable and importable.

---

### System Manager

Responsible for:

* System checks.
* Dependency checks.
* Health diagnostics.
* Repair operations.

Checks include:

* Python
* yt-dlp
* ffmpeg
* Native Messaging Host
* Database availability
* File permissions

---

### Update Manager

Responsible for:

* yt-dlp updates.
* Python package updates.
* Future VaultTube updates.
* Version checks.

The update system must always require user approval before applying updates.

---

### Localization Manager

Responsible for:

* Language management.
* Translation handling.
* Locale configuration.

Initial languages:

* English
* Turkish

Future languages may be added without changing module logic.

---

### Protocol Manager

Responsible for:

* JSON message handling.
* Protocol version validation.
* Native Messaging packet validation.
* Communication security.

All browser-to-core communication must pass through this manager.

---

### Plugin Manager

Responsible for:

* Plugin registration.
* Plugin loading.
* Plugin validation.
* Plugin lifecycle management.

Plugin support is planned as a future-proof architecture component.

The plugin system does NOT have to be fully implemented in v1.0.

---

### Backup Manager

Responsible for:

* Database backups.
* Settings export.
* JSON export.
* JSON import.
* Restore operations.

Supports:

* Full backups.
* Partial backups.
* Future portable mode.

---

### Logging Manager

Responsible for:

* Error logs.
* Debug logs.
* Diagnostic information.
* System event logs.

Logging must remain lightweight and configurable.

---

## Browser Extension Modules

The browser extension will contain separate UI-oriented modules.

### Popup Module

Responsible for:

* Quick downloads.
* Current tab operations.
* Shortcut actions.

---

### Dashboard Module

Responsible for:

* Media management.
* History management.
* Settings management.
* System information.
* Download queue visualization.

---

### Content Script Module

Responsible for:

* YouTube page integration.
* Download button injection.
* Video information requests.

The Content Script must remain lightweight.

---

### Context Menu Module

Responsible for:

* Right-click integrations.
* Quick download actions.
* Future URL-based actions.

---

### Localization Module

Responsible for:

* Browser-side translations.
* chrome.i18n integration.

---

## Future Modules (Not v1.0)

Planned future modules include:

* Workflow Engine
* Desktop GUI Module
* CLI Module
* Plugin Marketplace
* Advanced Scheduler System
* Portable Mode Manager
* Additional Platform Managers

These modules are intentionally excluded from the initial v1.0 scope.

---

## Design Principles

All modules must:

* Have a single responsibility.
* Remain loosely coupled.
* Be independently maintainable.
* Be scalable.
* Prefer event-based communication.
* Respect user privacy.
* Minimize resource usage.

No module should become mandatory unless required by the application's core functionality.

---

## Final Notes

VaultTube is designed around modularity and extensibility.

Every new feature added to the project should belong to an existing module or justify the creation of a new one.

Module complexity should always be minimized in favor of maintainability and long-term scalability.
