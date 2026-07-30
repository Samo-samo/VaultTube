# VaultTube - Database Document

## Overview

VaultTube uses SQLite as its primary local database engine.

The database is responsible for storing all user-related, media-related and application-related information locally.

VaultTube follows a local-first philosophy. No user data is transmitted externally.

---

## Database Goals

The database must be:

* Lightweight
* Fast
* Scalable
* Modular
* Easily maintainable
* Suitable for future migrations

All data stored by VaultTube should be accessible through the Database Manager.

Modules must never communicate directly with SQLite.

---

## Database Philosophy

SQLite is the single source of truth for VaultTube.

JSON files are reserved only for:

* Backups
* Imports
* Exports
* Portable mode support

SQLite will store:

* Application settings
* Download history
* Media information
* Notes and timestamps
* Queue data
* Profiles
* System information
* Plugin data
* Future module data

---

## Planned Tables

The initial database architecture includes the following tables.

### Settings

Stores:

* User preferences
* Feature flags
* UI preferences
* Download preferences
* Localization preferences

Examples:

* Default download location
* Default language
* Queue limits
* Update preferences

---

### Downloads

Stores:

* Download records
* Download dates
* Media types
* File sizes
* Download status

Examples:

* Completed
* Failed
* Paused
* Queued
* Cancelled

---

### Media

Stores:

* Media metadata
* Channel information
* Titles
* URLs
* Duration
* Available formats

Media entries should remain reusable across multiple modules.

---

### Queue

Stores:

* Queue items
* Queue order
* Queue status
* Resume information
* Queue configuration

Supports:

* Pause
* Resume
* Manual continuation
* Future concurrent download support

---

### Notes

Stores:

* User notes
* Media notes
* General comments

Notes are completely optional.

---

### Timestamps

Stores:

* Timestamp entries
* Timestamp descriptions
* Timestamp positions

Examples:

* 01:25 - Useful explanation.
* 05:47 - Important section.

The timestamp system is independent from subtitles.

---

### Profiles

Stores:

* Download profiles
* Storage profiles
* Future workflow profiles

Examples:

* Music Collector
* Movie Collector
* Lightweight User

Profiles allow users to quickly switch configurations.

---

### Storage

Stores:

* Storage locations
* Storage profiles
* Folder information
* Storage statistics

Supports:

* Single-folder mode
* Multi-folder mode

Future support:

* Portable mode

---

### History

Stores:

* Download history
* Media actions
* Rename operations
* Delete operations

The History system should provide filtering capabilities.

Examples:

* Channel filter
* File size filter
* Media type filter

---

### System

Stores:

* System health information
* Installed dependency versions
* System checks

Examples:

* Python version
* yt-dlp version
* ffmpeg version
* Native Messaging status

This information is intended for diagnostics and maintenance purposes.

---

### Updates

Stores:

* Last update checks
* Update preferences
* Update history

Supports:

* Automatic checks
* Manual checks
* Future VaultTube update support

---

### Plugins

Stores:

* Installed plugins
* Plugin states
* Plugin configurations

Plugin support is reserved for future versions.

The database architecture remains ready for plugin integration.

---

### Logs

Stores:

* Error logs
* Warning logs
* Diagnostic logs

Logging must remain configurable.

Users should be able to:

* Disable certain logs
* Export logs
* Clear logs

---

## Relationships

Examples of table relationships:

* Media ↔ Downloads
* Media ↔ Notes
* Media ↔ Timestamps
* Downloads ↔ History
* Profiles ↔ Settings
* Storage ↔ Downloads
* Queue ↔ Downloads

The final schema will be documented separately when implementation begins.

---

## Future Migration Strategy

VaultTube will support database versioning.

Examples:

* Database Version 1
* Database Version 2
* Database Version 3

Database migrations must:

* Preserve user data.
* Validate schema integrity.
* Support future upgrades.

Users should never lose their data during upgrades.

---

## Backup Strategy

The Backup Manager should support:

* Full database backup
* Partial database backup
* JSON export
* JSON import
* Selective data export

Examples:

* Export only Settings
* Export only Notes
* Export only Profiles
* Export everything

---

## Performance Goals

The database must:

* Load quickly.
* Minimize unnecessary queries.
* Avoid duplicate information whenever possible.
* Remain lightweight for typical users.

Database access should always go through the Database Manager.

---

## Security Goals

VaultTube must:

* Validate all database operations.
* Prevent invalid records.
* Protect against corrupted imports.
* Validate JSON backup files before importing.

Destructive operations must always require user confirmation.

---

## Final Notes

SQLite is one of the most important components of VaultTube.

The database architecture is intentionally designed to remain scalable and independent from the browser extension and user interface layers.

All future VaultTube modules must integrate with the Database Manager rather than directly accessing SQLite.
