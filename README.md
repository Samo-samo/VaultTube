# VaultTube

VaultTube is a local-first, open-source YouTube media management and advanced download browser extension powered by Native Messaging, Python, yt-dlp, FFmpeg, and SQLite.

The project is designed to provide a modern and lightweight media management experience while keeping all data and downloads on the user's local machine.

## Features

Current and planned core features include:

* Advanced YouTube video and audio downloading
* Native Messaging integration
* Python-powered backend architecture
* yt-dlp and FFmpeg support
* Download queue management
* SQLite-based local database
* Download history management
* Media metadata support
* Notes and timestamp support
* JSON export and import
* Multi-language support (English and Turkish)
* Popup and dashboard interfaces
* Local-first architecture
* Open-source and dependency-light design

## Project Goals

VaultTube focuses on:

* Simplicity
* Performance
* Maintainability
* Modularity
* Minimal external dependencies
* Long-term sustainability

The project intentionally avoids unnecessary frameworks and overly complex architectures.

## Technology Stack

### Browser Extension

* HTML
* CSS
* JavaScript
* Manifest V3

### Native Backend

* Python

### Database

* SQLite

### Media Tools

* yt-dlp
* FFmpeg

## Architecture Overview

VaultTube uses a thin-client architecture:

Browser Extension → Native Messaging → Python Backend → Download Engine → SQLite / yt-dlp / FFmpeg

The browser extension is responsible for user interaction and UI, while the Python backend handles all heavy operations such as downloads, queue management, database operations, and media processing.

## Documentation

Detailed project documentation can be found in the `docs/` directory.

Documentation includes:

* Project Vision
* Roadmap
* Architecture
* Tech Stack
* File Structure
* Native Messaging
* Database Schema
* Download Engine
* UI/UX Rules
* Testing
* Release Plan
* Contribution Guidelines

## Development Philosophy

VaultTube follows a documentation-driven development workflow.

Every major feature or architectural decision should be documented before implementation.

The project prioritizes:

* Clean architecture
* Minimal dependencies
* Local-first design
* Open-source best practices
* Sustainable development

## Current Status

VaultTube is currently under active development and has not reached its first public release.

## License

This project is licensed under the MIT License.

## Disclaimer

VaultTube is an independent open-source project and is not affiliated with or endorsed by YouTube or Google.

Users are responsible for complying with the terms of service and copyright laws applicable in their jurisdiction when downloading or managing media.
