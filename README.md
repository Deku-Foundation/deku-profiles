# Deku Profiles

Deku Profiles stores declarative metadata for the system and desktop configurations planned for Deku Linux.

## Status

The canonical `minimal-x86_64` profile remains on **Fedora 44** because this is the baseline for which the project has a completed ISO-build plus UEFI/QEMU console-boot test. A separate attempt to fetch Fedora 45 Anaconda media returned HTTP 404 on 2026-10-23, so Fedora 45 is not the default build target until its official release media and repository state are verified.

The prior pinned Fedora 44 profile revision `2924c0eabe745542f61985062ad164133e5e006f` produced a technology-preview ISO with SHA-256 `a5d604ea3964a8a05c7a42b0c515586204e0f5c23a1a5e412fa585649eca5a58`, and the UEFI boot harness observed `DEKU_BOOT_OK:minimal-x86_64`. The new profile revision must pass the same pipeline before it is treated as accepted evidence.

## Independent native profile

The separate `profiles/native-minimal-x86_64/profile.json` is the proposed target architecture for Deku's own package closure and root filesystem. It deliberately has no locked packages yet and cannot build an ISO. It is not based on Fedora, Void or NixOS at runtime. The existing `minimal-x86_64` Fedora 44 profile remains only as a labelled technology-preview/boot-harness fixture and must not be promoted as the native profile.

The native profile schema is in `schema/native-profile-v1.schema.json`; the native profile contract is checked by `deku-build validate-native-profile`. The command validates metadata only; it does not build packages, authenticate a repository, assemble a root filesystem or generate an ISO.

## Responsibilities

- Declare package selections, services, locale defaults, boot parameters and system configuration.
- Keep the profile schema and upstream selection explicit; do not confuse a versioned release with an immutable package snapshot.
- Keep profile data declarative; never execute arbitrary profile-provided shell as root.
- Include license/provenance references for selected components.
- Keep exact source revisions, toolchain/container identity, package inventory and output digests in each build's evidence.

## Non-goals

This repository does not implement the package manager, package build sandbox, kernel, installer or ISO builder. Those remain in the component repositories and use reviewed upstream tooling.

## Release selection policy

1. Keep the last verified baseline as the canonical default.
2. Try a newer Fedora release only on an explicit experimental path after checking official media URL availability and release status.
3. Do not update the canonical profile based on a successful metadata check alone: the image must build, pass UEFI boot tests, and preserve logs and hashes.
4. Fedora release repositories are rolling inputs; until repository snapshots or exact resolved RPM artifacts are locked, builds are traceable but not guaranteed to be reproducible.

## Acceptance

Every profile must validate, resolve to a complete manifest, declare its upstream package set, and pass the integration boot tests before it is described as supported. The initial profile is an upstream-based technology preview, not a complete independent Deku root filesystem.
