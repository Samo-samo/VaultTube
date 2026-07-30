# VaultTube - Architecture Document

## Overview

VaultTube is a modular, local-first media management platform whose first user interface is a browser extension for Chromium-based browsers. The project is designed to be scalable, lightweight, privacy-friendly, and easily extendable.

VaultTube is NOT designed as a simple YouTube downloader extension. Instead, it consists of a local core system and multiple user interface layers.

---

## Project Philosophy

VaultTube follows the following principles:

* Local-first architecture.
* Privacy-first design.
* Modular and scalable development.
* Performance-oriented implementation.
* No telemetry.
* No advertisements.
* No paid or locked features.
* User-controlled configuration.
* Browser-independent core architecture.
* Future-proof design for new interfaces and modules.

---

## High-Level Architecture

VaultTube consists of three major layers:

1. User Interface Layer
2. Core Layer
3. Data Layer

### User Interface Layer

Responsible for:

* Browser extension UI.
* Popup window.
* Dashboard.
* YouTube integration.
* Context menu integration.
* Localization.
* Settings pages.

Current targets:

* Google Chrome
* Brave Browser

Future targets:

* Firefox
* Microsoft Edge
* Desktop GUI
* CLI

---

### Core Layer

Responsible for:

* Media processing.
* Download management.
* Queue management.
* System checks.
* Storage management.
* Settings management.
* Update management.
* Plugin support.
* Native messaging communication.

The Core layer is completely independent from the browser.

The browser extension acts only as a client.

---

### Data Layer

Responsible for:

* SQLite database.
* Backups.
* Configuration storage.
* Logs.
* User profiles.
* Import and export functionality.

SQLite is the primary data source.

JSON files are reserved for:

* Backup.
* Import.
* Export.
* Portable mode support.

---

## Core Architecture

VaultTube Core will follow a manager-based architecture.

Examples:

* Download Manager
* Queue Manager
* Storage Manager
* History Manager
* Database Manager
* Settings Manager
* Update Manager
* System Manager
* Localization Manager
* Protocol Manager
* Plugin Manager

Each manager has only one responsibility.

Managers should communicate through events and interfaces whenever possible.

---

## Browser Extension Architecture

The extension is responsible only for:

* User interaction.
* YouTube integration.
* Displaying download options.
* Sending requests to VaultTube Core.

The extension MUST NOT perform heavy operations.

Heavy operations belong to:

* yt-dlp
* ffmpeg
* SQLite
* Queue management
* Storage operations

All heavy tasks are delegated to VaultTube Core.

---

## Native Messaging Architecture

Communication flow:

Browser Extension

↓

Native Messaging Bridge

↓

VaultTube Core

↓

Managers

↓

Database / Download Engines

All communication uses JSON messages.

Future protocol versions must remain backward compatible whenever possible.

---

## Database Architecture

SQLite is the primary database engine.

The database stores:

* Download history.
* Settings.
* Notes.
* Timestamps.
* Profiles.
* Queue information.
* Metadata.
* Storage information.
* Other future module data.

Database schemas are documented separately.

---

## Modular Design

VaultTube modules must:

* Be independent.
* Be disableable whenever possible.
* Not require unrelated modules.

Examples:

* Notes System can be disabled.
* Queue System can be disabled.
* Disk Analyzer can be disabled.
* Plugin System can be disabled.

Users should be able to use VaultTube as:

* A lightweight downloader.
* A complete media management platform.

---

## Event-Driven Philosophy

VaultTube follows an event-driven architecture.

Examples:

* Download Started
* Download Finished
* Queue Paused
* Media Deleted
* Backup Completed
* Database Updated

Managers react to events instead of tightly coupling themselves to each other.

This improves:

* Scalability.
* Plugin support.
* Maintainability.
* Performance.

---

## Performance Goals

VaultTube must be:

* Lightweight.
* Fast.
* Resource efficient.

VaultTube should never remain active unless necessary.

Modules should:

* Execute their tasks.
* Release resources.
* Return to an idle state.

Performance always has priority over unnecessary complexity.

---

## Security Goals

VaultTube must:

* Validate all incoming requests.
* Validate file paths.
* Validate JSON protocol messages.
* Never execute arbitrary commands.
* Require confirmation for destructive actions.

User files must never be modified or deleted without explicit permission.

---

## Versioning Strategy

Development order:

* Documentation
* Core architecture
* Native messaging
* Database
* Browser extension
* User interfaces
* Download system
* Alpha releases
* Stable release

Future versions may introduce:

* Desktop GUI
* CLI
* Advanced workflows
* Plugin ecosystem
* Additional platform support

---

## Current v1.0 Scope

Planned features include:

* Video download.
* Audio download.
* Subtitle download.
* Queue management.
* History management.
* Notes and timestamps.
* SQLite integration.
* Native Messaging.
* System Checker.
* Setup Wizard.
* Popup UI.
* Dashboard UI.
* Localization support.
* Storage profiles.
* Backup system.
* Update system.
* Chrome and Brave support.

---

## Final Notes

VaultTube is designed as a media management platform rather than a traditional downloader extension.

The architecture prioritizes:

* User freedom.
* Modularity.
* Local execution.
* Performance.
* Scalability.
* Long-term maintainability.

All future development decisions must respect the architectural principles defined in this document.
