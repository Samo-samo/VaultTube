# VaultTube - Development Document

## Overview

This document defines the development philosophy, coding standards, documentation rules and Git workflow used throughout the VaultTube project.

All contributors are expected to follow the rules defined in this document.

---

## Development Philosophy

VaultTube follows the following principles:

* Documentation first.
* Architecture first.
* Core first.
* User experience first.
* Performance first.
* Local-first design.
* Modular development.
* Future-proof architecture.

No feature should be implemented before its architecture is documented and approved.

---

## Development Workflow

Every feature must follow the same workflow:

1. Design.
2. Documentation.
3. Architecture review.
4. Implementation.
5. Testing.
6. Commit.
7. Push.

Workflow example:

Feature Idea

↓

Documentation

↓

Implementation

↓

Testing

↓

Git Commit

↓

Git Push

---

## Documentation Policy

All important decisions must be documented.

Examples:

* Architectural decisions.
* Module responsibilities.
* Database changes.
* Protocol changes.
* New features.
* Breaking changes.
* Future plans.

Conversations must never become the single source of truth.

The repository documentation is always considered authoritative.

---

## Feature Freeze Policy

VaultTube actively avoids feature creep.

Before implementing any feature, ask:

"Is this required for v1.0?"

If the answer is:

* Yes -> Implement.
* No -> Add to ROADMAP.md.

Future ideas should not delay the current milestone.

---

## Git Workflow

Current branch strategy:

* main

VaultTube currently uses a simplified workflow suitable for early development.

Future versions may introduce:

* develop
* release
* experimental

The project should remain lightweight during the early stages of development.

---

## Commit Policy

Commits should remain small and meaningful.

Examples:

* Add Protocol documentation
* Implement Database Manager
* Add Native Messaging host
* Create Queue Manager
* Implement Setup Wizard

Avoid commits such as:

* Update stuff
* Fix things
* Changes
* Misc improvements

Commit messages must clearly describe what changed.

---

## Push Policy

Recommended workflow:

* Complete a small milestone.
* Commit changes.
* Push to GitHub.

Examples:

Good milestones:

* One documentation file completed.
* One manager completed.
* One UI component completed.
* One database migration completed.

Avoid pushing unfinished or broken implementations whenever possible.

---

## Coding Standards

General rules:

* Keep modules small.
* Keep functions focused.
* Avoid code duplication.
* Prefer readability over clever code.
* Write maintainable code.

Performance is more important than unnecessary abstractions.

---

## Architecture Rules

Managers must:

* Have a single responsibility.
* Remain loosely coupled.
* Prefer event-driven communication.
* Respect protocol boundaries.

Managers must not:

* Become monolithic.
* Directly manipulate unrelated modules.
* Perform responsibilities outside their scope.

---

## Browser Extension Rules

The browser extension should remain lightweight.

The extension is responsible only for:

* User interfaces.
* Browser integrations.
* Sending protocol requests.

The extension must never perform heavy processing.

Heavy operations belong to:

* VaultTube Core
* yt-dlp
* ffmpeg
* SQLite

---

## Database Rules

SQLite is the primary data source.

Modules must never communicate directly with SQLite.

All database operations must be performed through:

* Database Manager

Database changes must always be documented before implementation.

---

## Native Messaging Rules

All Native Messaging communication must:

* Use JSON.
* Validate requests.
* Validate protocol versions.
* Validate payloads.

No request should bypass protocol validation.

---

## Performance Guidelines

VaultTube must remain:

* Lightweight.
* Fast.
* Resource efficient.

Optimization goals include:

* Minimal memory usage.
* Minimal CPU usage.
* Minimal background activity.

Features should never compromise the overall performance of the application.

---

## Security Guidelines

VaultTube must:

* Respect user privacy.
* Never collect telemetry.
* Never upload user data.
* Never modify user files without permission.

Destructive actions must always require explicit confirmation.

Examples:

* Delete media file.
* Restore backup.
* Reset settings.
* Remove storage profile.

---

## User Experience Guidelines

VaultTube should remain approachable for new users.

The default experience should be:

Install

↓

Setup Wizard

↓

Choose download folder

↓

Download media

↓

Done

Advanced features must remain optional.

Users should never be forced to configure unnecessary settings.

---

## Roadmap Policy

Future features belong in:

* ROADMAP.md

Examples:

* Desktop GUI
* Workflow Engine
* Advanced automation
* Plugin marketplace
* CLI support

The roadmap exists to prevent feature creep during active development.

---

## Testing Policy

All major features should be tested before release.

Examples:

* Download functionality.
* Queue operations.
* Database operations.
* Native Messaging.
* Localization.
* Backup and restore.
* System diagnostics.

Future versions may introduce automated testing pipelines.

---

## Release Philosophy

VaultTube development priorities:

1. Stable architecture.
2. Stable core modules.
3. Stable protocol.
4. Stable database.
5. Stable extension integration.
6. Stable user experience.

Features are secondary to stability.

A smaller and stable release is preferred over a larger and unstable release.

---

## Final Notes

VaultTube is intended to be a long-term, scalable and maintainable open-source project.

The project prioritizes:

* Simplicity
* Stability
* Performance
* Privacy
* Documentation
* Modularity
* User freedom

All contributors should follow the development principles defined in this document.
