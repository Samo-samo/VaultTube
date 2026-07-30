# VaultTube - Protocol Document

## Overview

VaultTube uses a JSON-based communication protocol between the browser extension and the local Native Messaging host.

The protocol is designed to be:

* Lightweight
* Human-readable
* Versioned
* Secure
* Extensible
* Platform-independent

All communication must follow the protocol specifications defined in this document.

---

## Communication Flow

Communication architecture:

Browser Extension

↓

Native Messaging Host

↓

VaultTube Core

↓

Managers

↓

SQLite / yt-dlp / ffmpeg / System Tools

The browser extension must never communicate directly with yt-dlp, ffmpeg or SQLite.

---

## Protocol Philosophy

The protocol is intentionally designed to be independent from:

* Browsers
* User interfaces
* Operating systems
* Future VaultTube clients

This allows future support for:

* Desktop GUI
* CLI
* Firefox
* Edge
* Other interfaces

without changing the Core communication logic.

---

## JSON Message Structure

All messages must use the following base structure:

```json
{
    "protocol_version": "1.0",
    "request_id": "",
    "action": "",
    "payload": {},
    "timestamp": ""
}
```

Field descriptions:

* protocol_version -> Current protocol version.
* request_id -> Unique request identifier.
* action -> Requested operation.
* payload -> Action-specific data.
* timestamp -> Request timestamp.

---

## Response Structure

All responses must use the following structure:

```json
{
    "protocol_version": "1.0",
    "request_id": "",
    "success": true,
    "message": "",
    "payload": {},
    "timestamp": ""
}
```

Field descriptions:

* success -> Indicates whether the operation succeeded.
* message -> Human-readable status message.
* payload -> Response-specific data.

---

## Error Structure

All errors must follow the same structure.

Example:

```json
{
    "protocol_version": "1.0",
    "request_id": "",
    "success": false,
    "error_code": "",
    "message": "",
    "payload": {},
    "timestamp": ""
}
```

Examples:

* INVALID_REQUEST
* INVALID_URL
* SYSTEM_ERROR
* DOWNLOAD_FAILED
* DATABASE_ERROR
* DEPENDENCY_MISSING
* PERMISSION_DENIED

---

## Supported Action Categories

The protocol is divided into action categories.

Examples:

* System
* Downloads
* Queue
* History
* Settings
* Storage
* Notes
* Timestamps
* Updates
* Backups
* Plugins
* Diagnostics
* Localization

---

## System Actions

Examples:

```text
system.check

system.health_check

system.get_info

system.dependencies
```

---

## Download Actions

Examples:

```text
download.start

download.pause

download.resume

download.cancel

download.remove

download.get_formats
```

---

## Queue Actions

Examples:

```text
queue.add

queue.pause

queue.resume

queue.clear

queue.status
```

---

## History Actions

Examples:

```text
history.list

history.delete

history.search

history.export
```

---

## Notes Actions

Examples:

```text
notes.create

notes.update

notes.delete

notes.list
```

---

## Timestamp Actions

Examples:

```text
timestamps.create

timestamps.update

timestamps.delete
```

---

## Storage Actions

Examples:

```text
storage.list

storage.statistics

storage.profile.list

storage.profile.update
```

---

## Settings Actions

Examples:

```text
settings.get

settings.update

settings.reset
```

---

## Backup Actions

Examples:

```text
backup.create

backup.restore

backup.export

backup.import
```

---

## Update Actions

Examples:

```text
update.check

update.yt_dlp

update.python_packages
```

---

## Diagnostic Actions

Examples:

```text
diagnostics.run

diagnostics.export

diagnostics.system
```

---

## Plugin Actions

Reserved for future versions.

Examples:

```text
plugin.install

plugin.enable

plugin.disable

plugin.remove
```

---

## Download Example

Download request:

```json
{
    "protocol_version": "1.0",
    "request_id": "REQ-0001",
    "action": "download.start",
    "payload": {
        "url": "https://youtube.com/example",
        "profile": "default"
    },
    "timestamp": "..."
}
```

Response:

```json
{
    "protocol_version": "1.0",
    "request_id": "REQ-0001",
    "success": true,
    "message": "Download queued successfully.",
    "payload": {
        "queue_id": "QUEUE-001"
    },
    "timestamp": "..."
}
```

---

## Security Requirements

The protocol must:

* Validate all incoming messages.
* Validate URLs.
* Validate file paths.
* Reject malformed JSON.
* Reject unsupported actions.
* Validate protocol versions.

No request should be processed before validation.

---

## Protocol Versioning

Examples:

* Protocol 1.0
* Protocol 1.1
* Protocol 2.0

Backward compatibility should be maintained whenever possible.

Major versions may introduce breaking changes.

---

## Event Support

Future versions may introduce event-based communication.

Examples:

```text
download.started

download.finished

download.failed

queue.paused

backup.completed

system.updated
```

The protocol architecture must remain compatible with event-driven communication.

---

## Performance Goals

The protocol must:

* Minimize unnecessary communication.
* Remain lightweight.
* Support future scalability.
* Support asynchronous operations.

Heavy processing must always be delegated to VaultTube Core.

---

## Final Notes

The VaultTube Protocol is the communication backbone of the entire project.

Every VaultTube component must communicate through this protocol whenever possible.

Future interfaces, plugins and modules must respect the protocol specifications defined in this document.
