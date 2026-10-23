# Minimal x86_64 Profile

Status: profile specification only; not yet a buildable profile.

## Purpose
The smallest boot target for the first Deku technology-preview ISO. The acceptance target is UEFI boot to a usable text console, not a complete desktop.

## Required profile fields
- Schema version.
- Architecture: x86_64.
- Firmware target: UEFI.
- Upstream base and immutable repository snapshot.
- Exact package set and package versions.
- Kernel, initramfs and bootloader selection.
- Locale, timezone policy and console configuration.
- Build tool version and all input digests.
- Test expectations and known limitations.

## Scope boundaries
Do not list fictitious Deku packages or package versions. Until deku-pkg can install packages and deku-recipes/deku-build can produce them, use an explicitly declared upstream base for the technology-preview build. Do not claim this profile is an independent Deku root filesystem.

## Acceptance
The profile must validate and resolve deterministically; build an image from pinned inputs; boot in disposable x86_64 UEFI QEMU; reach the declared userspace target; and preserve logs, input manifest and artifact digest.
