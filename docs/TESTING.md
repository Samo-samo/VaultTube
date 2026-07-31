# Testing

## Overview

VaultTube follows a practical testing approach focused on reliability and maintainability.

The project's testing strategy prioritizes core functionality over excessive test coverage or complex testing pipelines.

---

## Testing Priorities

The following systems should be tested whenever changes are made:

* Browser Extension functionality
* Native Messaging communication
* Python backend operations
* Download Engine workflows
* Queue management
* Database operations
* UI interactions
* Localization support

---

## Manual Testing

Manual testing is expected to be the primary testing method during early development.

Common manual test scenarios include:

* Downloading video, audio, and subtitles
* Verifying Native Messaging communication
* Testing download progress updates
* Testing queue operations
* Verifying database records
* Testing settings persistence
* Checking UI behavior
* Validating localization strings

---

## Functional Testing

Before major releases, the following functionality should be verified:

### Download System

* Media information retrieval
* Format selection
* Download execution
* Download cancellation
* Download completion handling

### Queue System

* Adding queue items
* Pausing downloads
* Resuming downloads
* Removing queue items
* Retry operations

### Database System

* Settings storage
* Download history
* Queue storage
* Database initialization

### Native Messaging

* Request handling
* Response handling
* Error handling
* Dependency checks

---

## UI Testing

UI testing should verify:

* Popup functionality
* Dashboard functionality
* Settings interface behavior
* YouTube page integration
* Notification behavior

The UI should remain responsive and easy to use across supported browsers.

---

## Localization Testing

Localization testing should ensure:

* No hardcoded user-facing strings.
* Proper language switching.
* Consistent translations.
* Correct text rendering within the UI.

Initial languages:

* English
* Turkish

---

## Error Handling Tests

The following situations should be tested whenever applicable:

* Missing FFmpeg installation
* Missing yt-dlp installation
* Native Messaging failures
* Invalid download requests
* Database failures
* Invalid settings values
* Unsupported media formats

Meaningful error messages should always be provided to users.

---

## Release Testing Checklist

Before creating a public release, verify:

* Core downloads work correctly.
* Native Messaging is functioning.
* The database initializes correctly.
* Queue operations behave as expected.
* Settings are properly saved.
* Localization is working.
* Documentation is up to date.
* No critical bugs are present.

---

## Testing Philosophy

VaultTube favors:

* Practical testing
* Reliable functionality
* Maintainable workflows

The project intentionally avoids unnecessarily complex testing requirements during early development.

The primary goal of testing is to ensure that core functionality remains stable and predictable throughout development.
