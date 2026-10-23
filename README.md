# Deku Profiles

Declarative system and desktop profiles for Deku Linux.

## Status

Bootstrap stage. No profile is a supported release yet. The initial target is a minimal x86_64 UEFI profile; KDE Plasma is the intended desktop direction, but it must not be added to the first image until the minimal boot path is tested.

## Responsibilities

- Declare package selections, services, locale defaults, boot parameters and system configuration.
- Pin profile schema versions and upstream inputs.
- Keep profile data declarative; never execute arbitrary profile-provided shell as root.
- Include license/provenance references for selected components.

## Non-goals

This repository does not implement the package manager, package build sandbox, kernel, installer or ISO builder. Those remain in the component repositories and use reviewed upstream tooling.

## Acceptance

Every profile must validate, resolve to a complete manifest, name exact package versions/revisions, and pass the integration boot tests before it is described as supported.
