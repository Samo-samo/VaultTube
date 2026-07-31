# Native Messaging

## Overview

VaultTube uses Native Messaging to establish communication between the browser extension and the Python backend.

The browser extension acts as a lightweight client responsible for user interaction, while the Python backend is responsible for business logic and resource-intensive operations.

Native Messaging is the communication bridge between these two layers.

---

## Architecture

The communication flow is designed as follows:

Browser Extension

↓

Native Messaging

↓

Python Backend

↓

Download Engine / Database / Queue Manager

The browser extension should never perform operations that belong to the backend.

---

## Responsibilities

### Browser Extension

Responsibilities include:

* Sending requests to the backend
* Receiving responses from the backend
* Updating the user interface
* Collecting user input
* Displaying status information

The extension should not:

* Manage downloads directly
* Access the database directly
* Perform media processing
* Implement queue logic
* Execute system-level operations

---

### Native Messaging Layer

Responsibilities include:

* Sending requests
* Receiving responses
* Message validation
* Error handling
* Communication management

The Native Messaging layer should remain lightweight and predictable.

---

### Python Backend

Responsibilities include:

* Download operations
* Queue management
* Database operations
* Metadata handling
* File management
* System checks
* Media processing

The Python backend is considered the primary application backend.

---

## Communication Philosophy

VaultTube follows a request-response communication model.

Examples of requests include:

* Start download
* Pause download
* Resume download
* Retrieve download history
* Save settings
* Fetch available formats
* Retrieve queue information
* Perform system checks

The extension sends requests and waits for responses from the Python backend.

---

## Message Design

Messages should remain:

* Small
* Predictable
* Structured
* Easy to validate

All communication should use a consistent message format throughout the project.

Future message schemas should be documented if necessary.

---

## System Checks

The Python backend may perform startup checks when required.

Examples include:

* Python availability
* yt-dlp availability
* FFmpeg availability
* Database accessibility
* Required directory checks

System checks should provide meaningful responses to the extension.

---

## Queue Management

Queue management belongs entirely to the Python backend.

The extension is responsible only for:

* Displaying queue information
* Sending queue-related commands

Examples:

* Pause item
* Resume item
* Remove item
* Reorder item
* Retry failed item

Queue state management should never be implemented in the browser extension.

---

## Database Access

SQLite access is handled exclusively by the Python backend.

The browser extension must never:

* Read database files directly
* Modify database records directly

All database operations should be performed through Native Messaging requests.

---

## Download Operations

The browser extension may request:

* Download information
* Available formats
* Estimated file sizes
* Download progress

The Python backend performs:

* yt-dlp operations
* FFmpeg operations
* File handling
* Progress reporting

---

## Error Handling

Native Messaging communication should provide meaningful error responses whenever possible.

Examples include:

* Native host unavailable
* Invalid requests
* Database failures
* Missing dependencies
* Download failures
* Queue failures

Errors should be communicated clearly to the extension so that appropriate user feedback can be displayed.

---

## Security Considerations

The Native Messaging layer should:

* Validate incoming requests.
* Reject malformed messages.
* Restrict operations to supported commands.
* Avoid executing arbitrary user-provided commands.

The backend should expose only the functionality required by the browser extension.

---

## Future Compatibility

The Native Messaging architecture should remain flexible enough to support future enhancements without introducing unnecessary complexity.

Potential future additions may include:

* Installation helpers
* Update checks
* Additional media-related features

Such additions should integrate with the existing architecture rather than introducing separate communication systems.

---

## Development Rules

The following rules apply throughout development:

* Keep Native Messaging simple.
* Keep the browser extension lightweight.
* Keep business logic inside the Python backend.
* Maintain a clear separation of responsibilities.
* Prefer predictable request-response workflows.
* Validate all communication between components.

---

## Final Notes

Native Messaging is the backbone of communication within VaultTube.

Its primary goal is to provide a simple, reliable, and maintainable bridge between the browser extension and the Python backend while preserving the project's local-first and modular architecture.
