# Download Engine

## Overview

The Download Engine is responsible for all media download and processing operations within VaultTube.

It acts as the core media handling component of the Python backend and is designed to remain modular, lightweight, and maintainable.

The Download Engine is responsible for coordinating:

* Media downloads
* Format handling
* Media processing
* Queue integration
* File management
* Download-related metadata

---

## Design Principles

The Download Engine follows the following principles:

* Reliability over feature quantity
* Clear separation of responsibilities
* Minimal complexity
* Modular design
* Local-first operation

All download-related functionality should remain centralized within this component.

---

## Responsibilities

The Download Engine is responsible for:

* Retrieving media information
* Discovering available formats
* Downloading media files
* Processing downloaded files
* Managing download workflows
* Reporting download progress
* Integrating with the Queue Manager
* Communicating with the database layer

The Download Engine should not be responsible for:

* User interface logic
* Browser extension logic
* Native Messaging implementation
* Database schema management

---

## Core Components

The Download Engine consists of several logical components.

### Media Information

Responsibilities include:

* Retrieving media metadata
* Retrieving available formats
* Retrieving media duration
* Retrieving thumbnails when required

---

### Format Handling

Responsibilities include:

* Detecting available formats
* Providing quality options
* Handling audio and video combinations
* Managing subtitle availability

Only formats supported by the target media should be presented to the user.

Unavailable or unsupported formats should never be displayed.

---

### Download Management

Responsibilities include:

* Starting downloads
* Stopping downloads when required
* Reporting download progress
* Integrating with the Queue Manager

Download operations should remain independent from the user interface.

---

### Media Processing

Responsibilities include:

* Audio and video merging
* File processing operations
* Format-related post-processing when required

Media processing should remain lightweight and rely on FFmpeg when appropriate.

---

## yt-dlp Integration

yt-dlp is responsible for:

* Media extraction
* Format discovery
* Download handling

The project should use yt-dlp whenever possible instead of reimplementing existing functionality.

VaultTube should avoid unnecessary wrappers or custom download implementations that duplicate yt-dlp's capabilities.

---

## FFmpeg Integration

FFmpeg is responsible for:

* Media merging
* Media processing
* Format conversion when required

FFmpeg should only be used when it provides clear benefits to the download workflow.

Unnecessary processing steps should be avoided.

---

## Queue Integration

The Download Engine is fully integrated with the Queue Manager.

Examples include:

* Pending downloads
* Active downloads
* Paused downloads
* Failed downloads
* Completed downloads
* Cancelled downloads

Queue state management belongs to the Queue Manager, while download execution belongs to the Download Engine.

---

## Supported Media Types

Initial support includes:

* Video downloads
* Audio downloads
* Subtitle downloads

Future media-related features may be added if they align with the project's goals.

---

## File Management

The Download Engine is responsible for:

* Creating download directories when necessary
* Managing output files
* Maintaining file naming consistency
* Reporting file locations to the database system

File operations should remain predictable and transparent.

---

## Download Workflow

A typical download operation is expected to follow this workflow:

1. User requests a download.
2. Media information is retrieved.
3. Available formats are identified.
4. The selected item is added to the queue.
5. The download begins when appropriate.
6. Media processing is performed if required.
7. Download records are saved to the database.
8. Progress and completion status are reported to the browser extension.

---

## Error Handling

The Download Engine should gracefully handle:

* Download failures
* Missing dependencies
* Unsupported formats
* Media processing failures
* Invalid download requests
* Network-related issues

Meaningful error messages should always be provided whenever possible.

---

## Performance Guidelines

The Download Engine should prioritize:

* Stability
* Predictable behavior
* Maintainability

Performance optimizations should only be introduced when they provide measurable benefits.

Complex download workflows should be avoided unless they significantly improve the user experience.

---

## Future Expansion

Potential future enhancements may include:

* Advanced queue capabilities
* Additional media processing options
* Improved metadata handling
* Enhanced file management features

Future additions should build upon the existing architecture rather than introducing separate download systems.

---

## Development Rules

The following rules apply throughout development:

* Keep the Download Engine independent from UI logic.
* Prefer existing yt-dlp capabilities over custom implementations.
* Use FFmpeg only when necessary.
* Preserve modularity.
* Avoid unnecessary complexity.
* Maintain predictable download workflows.

---

## Final Notes

The Download Engine is one of VaultTube's core systems.

Its primary goal is to provide a reliable and maintainable media downloading experience while remaining lightweight, modular, and easy to extend as the project evolves.
