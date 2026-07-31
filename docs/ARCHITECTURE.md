# Architecture

## Overview

VaultTube follows a local-first and thin-client architecture.

The browser extension is responsible for user interaction and interface components, while the Python backend handles all resource-intensive operations and business logic.

The architecture is intentionally designed to remain simple, modular, and easy to maintain.

---

## High-Level Architecture

```text
Browser Extension
        |
        v
Native Messaging
        |
        v
Python Backend
        |
        v
Download Engine
        |
        v
SQLite / yt-dlp / FFmpeg
```

Each layer has a clearly defined responsibility and should avoid handling tasks that belong to another layer.

---

## Architectural Principles

VaultTube is built around the following principles:

* Local-first design
* Thin-client architecture
* Minimal dependencies
* Modular development
* Documentation-driven development
* Maintainability over complexity

---

## Core Components

The project consists of five primary components:

### 1. Extension UI

Responsibilities:

* User interface
* User interactions
* YouTube page integration
* Settings pages
* Popup interface
* Dashboard interface
* Localization handling

The extension should remain lightweight and avoid implementing business logic whenever possible.

---

### 2. Native Messaging Layer

Responsibilities:

* Communication between the browser extension and Python backend
* Message validation
* Request and response handling

The Native Messaging layer acts as the bridge between the frontend and backend systems.

---

### 3. Python Backend

Responsibilities:

* Download management
* Queue management
* Database operations
* Media processing
* System checks
* Metadata management
* File management

The Python backend is considered the application's primary backend service.

---

### 4. Download Engine

Responsibilities:

* yt-dlp integration
* FFmpeg integration
* Media processing
* Format selection
* Download workflows

The download engine should remain independent from UI-related logic.

---

### 5. Database System

Responsibilities:

* Settings storage
* Download history
* Queue storage
* Metadata storage
* Notes and timestamps
* Future data migrations

SQLite is used as the project's local database solution.

---

## Communication Flow

A typical download workflow is expected to follow the sequence below:

```text
User Action
      |
      v
Browser Extension
      |
      v
Native Messaging
      |
      v
Python Backend
      |
      v
Queue Manager
      |
      v
Download Engine
      |
      v
yt-dlp and FFmpeg
      |
      v
SQLite Updates
      |
      v
Native Messaging Response
      |
      v
Browser Extension UI Update
```

This design keeps responsibilities clearly separated and improves maintainability.

---

## Thin-Client Approach

The browser extension should never become the primary application layer.

Its responsibilities are limited to:

* Displaying information
* Collecting user input
* Sending requests
* Receiving responses
* Updating the user interface

All heavy operations belong to the Python backend.

---

## Modularity Guidelines

Each system should be developed as an independent module whenever practical.

Examples include:

* Queue System
* Download Engine
* Database System
* Localization System
* Settings System
* Media Management System

Modules should communicate through well-defined interfaces and avoid unnecessary dependencies.

---

## Dependency Philosophy

VaultTube intentionally minimizes the number of dependencies.

The project avoids:

* Frontend frameworks
* Large UI libraries
* Unnecessary third-party services

Preferred technologies are:

* HTML
* CSS
* JavaScript
* Python
* SQLite
* yt-dlp
* FFmpeg

Additional dependencies should only be introduced when they provide clear and significant benefits.

---

## Scalability Strategy

VaultTube is designed as a medium-sized project.

Scalability does not mean adding unnecessary complexity. Instead, scalability is achieved through:

* Modular architecture
* Clear component boundaries
* Maintainable code
* Well-defined documentation

Future features should integrate with existing systems whenever possible instead of introducing entirely new architectural layers.

---

## Architectural Rules

The following rules apply throughout development:

* Keep the browser extension lightweight.
* Keep the Python backend responsible for business logic.
* Prefer simple solutions over complex ones.
* Avoid introducing new dependencies without justification.
* Preserve clear separation of responsibilities.
* Prioritize maintainability over feature count.
* Document major architectural decisions before implementation whenever possible.

---

## Final Notes

VaultTube is intentionally designed to be a lightweight, local-first media management platform rather than a feature-heavy application.

Every architectural decision should support the project's long-term goals:

* Simplicity
* Maintainability
* Performance
* Modularity
* Sustainability
