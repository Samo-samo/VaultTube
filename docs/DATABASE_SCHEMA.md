# Database Schema

## Overview

VaultTube uses SQLite as its local database solution.

The database is responsible for storing application data that should persist between sessions. All database operations are performed exclusively by the Python backend.

The browser extension must never access the database directly.

---

## Design Principles

The database system is designed around the following principles:

* Local-first storage
* Lightweight architecture
* Maintainability
* Future extensibility
* Minimal complexity

VaultTube intentionally avoids unnecessary database abstractions or external database systems.

---

## Responsibilities

The database is responsible for storing:

* Application settings
* Download history
* Queue information
* Media metadata
* Notes and timestamps
* Folder preferences
* Statistics and usage data
* Database version information

Additional tables may be introduced when justified by future features.

---

## Initial Database Structure

The following logical components are planned for the initial database design:

### Settings

Stores:

* Application settings
* User preferences
* Download settings
* UI preferences
* Localization preferences

---

### Download History

Stores:

* Download records
* Download status
* Media information
* File locations
* Download timestamps

---

### Queue Items

Stores:

* Queue entries
* Queue states
* Queue order information
* Queue metadata

---

### Media Metadata

Stores:

* Media titles
* Media identifiers
* Duration information
* Available metadata required by project features

Only data that provides meaningful value should be stored.

---

### Notes and Timestamps

Stores:

* User-created notes
* Media timestamps
* Optional annotations

This component is intentionally separated from download history to improve maintainability.

---

### Statistics

Stores:

* Optional application statistics
* Download counters
* Other lightweight usage-related information when required

Statistics should remain simple and privacy-friendly.

---

### Database Version

Stores:

* Current database version
* Migration-related information

This component allows future database migrations without introducing unnecessary complexity.

---

## Database Philosophy

The database should:

* Remain lightweight.
* Store only necessary information.
* Avoid duplicate data whenever possible.
* Remain easy to migrate and maintain.

The database is intended to support the application's core functionality rather than becoming a complex data platform.

---

## Access Rules

The following rules apply throughout development:

* SQLite access is exclusive to the Python backend.
* Database operations must never be performed by the browser extension.
* Database schemas should remain documented.
* Future schema changes should be backward compatible whenever practical.
* Major schema changes should be documented before implementation.

---

## Future Expansion

Future additions may include:

* Additional metadata storage.
* Backup-related information.
* Advanced media management features.
* New settings categories.

Future database features should integrate with the existing structure whenever possible instead of introducing unnecessary complexity.

---

## Performance Considerations

The database system should prioritize:

* Reliability
* Simplicity
* Maintainability
* Fast local access

SQLite is expected to provide more than sufficient performance for the project's requirements.

Premature database optimization should be avoided unless real performance issues are identified.

---

## Final Notes

VaultTube's database system is designed to remain simple, reliable, and easy to maintain.

Every database-related decision should support the project's core philosophy:

* Local-first design
* Minimal complexity
* Maintainable architecture
* Sustainable long-term development
