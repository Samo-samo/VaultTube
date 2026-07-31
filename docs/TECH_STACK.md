# Tech Stack

## Overview

VaultTube is intentionally built using a minimal and dependency-light technology stack.

The project prioritizes simplicity, maintainability, and long-term sustainability over adopting unnecessary frameworks or third-party libraries.

---

## Browser Extension

The browser extension is built using:

* HTML
* CSS
* JavaScript
* Manifest V3

Responsibilities include:

* User interface
* YouTube page integration
* Popup interface
* Dashboard interface
* Settings pages
* Localization support
* Communication with the Python backend

No frontend frameworks are used.

---

## Native Backend

The native backend is built using:

* Python

Responsibilities include:

* Native Messaging communication
* Download management
* Queue management
* Database operations
* Media processing
* File management
* System checks

Python serves as the primary backend layer of the project.

---

## Database

VaultTube uses:

* SQLite

Responsibilities include:

* Application settings
* Download history
* Queue information
* Metadata storage
* Notes and timestamps
* Database version tracking

SQLite was selected because it is lightweight, fast, portable, and requires no external database server.

---

## Media Processing Tools

VaultTube uses:

* yt-dlp
* FFmpeg

yt-dlp is responsible for:

* Media extraction
* Format discovery
* Download handling

FFmpeg is responsible for:

* Media processing
* Audio and video merging
* Format conversion when required

These tools are considered core project dependencies.

---

## Localization System

Localization is implemented using:

* JSON files

Initial supported languages:

* English
* Turkish

The localization system should remain simple and easily extendable for future language support.

---

## Development Environment

Recommended development tools include:

* Visual Studio Code
* Git
* GitHub

The project does not require a complex development environment or additional tooling.

---

## Browser Support

Current development targets:

* Google Chrome
* Chromium-based browsers
* Brave Browser (testing)

Future browser support may be considered if it provides meaningful value.

Support for non-Chromium browsers is outside the project's initial scope.

---

## Dependencies Philosophy

VaultTube follows a minimal dependency philosophy.

The project intentionally avoids:

* Frontend frameworks
* CSS frameworks
* JavaScript frameworks
* Large third-party libraries
* Cloud-based services

New dependencies should only be added when they:

* Solve a real problem.
* Significantly improve maintainability.
* Provide clear benefits that justify their inclusion.

---

## Versioning Strategy

Technology versions should remain flexible unless a specific version requirement becomes necessary.

Examples include:

* Modern Python releases.
* Modern Chromium browser versions.
* Current stable releases of yt-dlp and FFmpeg.

Hard version requirements should only be introduced when compatibility issues make them necessary.

---

## Design Philosophy

The technology stack is guided by the following principles:

* Minimalism
* Performance
* Maintainability
* Transparency
* Ease of contribution
* Long-term sustainability

VaultTube intentionally favors simple and well-established technologies over complex and trendy solutions whenever possible.
