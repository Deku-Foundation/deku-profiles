import json
import unittest
from pathlib import Path

PROFILE = Path(__file__).parents[1] / "profiles" / "minimal-x86_64" / "profile.json"


class ProfileContractTests(unittest.TestCase):
    def setUp(self):
        self.profile = json.loads(PROFILE.read_text(encoding="utf-8"))

    def test_profile_is_explicitly_experimental(self):
        self.assertEqual(self.profile["schema_version"], 1)
        self.assertEqual(self.profile["status"], "experimental-specification")
        self.assertFalse(self.profile["bootstrap"]["independent_deku_rootfs"])

    def test_bootstrap_stays_on_the_last_verified_fedora_baseline(self):
        self.assertEqual(self.profile["bootstrap"]["distribution"], "fedora")
        self.assertEqual(self.profile["bootstrap"]["release"], "44")
        self.assertEqual(self.profile["bootstrap"]["package_manager"], "dnf")
        self.assertFalse(self.profile["bootstrap"]["independent_deku_rootfs"])

    def test_initial_target_is_single_architecture_and_uefi(self):
        self.assertEqual(self.profile["target"]["architecture"], "x86_64")
        self.assertEqual(self.profile["target"]["firmware"], ["uefi"])
        self.assertEqual(self.profile["target"]["libc"], "glibc")

    def test_boot_target_defers_desktop(self):
        self.assertEqual(self.profile["boot_target"]["stage"], "console")
        self.assertEqual(self.profile["boot_target"]["desktop"], "deferred-until-console-boot-passes")

    def test_packages_are_unique_and_nonempty(self):
        packages = self.profile["package_selection"]
        self.assertTrue(packages)
        self.assertEqual(len(packages), len(set(packages)))
        self.assertTrue(all(isinstance(name, str) and name.strip() for name in packages))
        self.assertIn("livesys-scripts", packages)
        self.assertIn("tar", packages)

    def test_live_bootloader_stack_is_declared(self):
        packages = set(self.profile["package_selection"])
        self.assertTrue({
            "grub2-pc",
            "grub2-pc-modules",
            "grub2-tools",
            "grub2-tools-extra",
            "grub2-efi-x64",
            "grub2-efi-x64-cdboot",
            "grub2-efi-x64-modules",
            "efibootmgr",
        } <= packages)

    def test_integrity_evidence_is_required(self):
        integrity = self.profile["integrity"]
        self.assertTrue(integrity["require_immutable_inputs"])
        self.assertTrue(integrity["record_artifact_sha256"])
        self.assertTrue(integrity["require_vm_boot_evidence"])

    def test_limits_are_documented(self):
        limitations = " ".join(self.profile["limitations"]).lower()
        self.assertIn("not an independent deku distribution", limitations)
        self.assertIn("repositories are not frozen snapshots", limitations)
        self.assertIn("does not produce an iso", limitations)
        self.assertIn("does not prove that deku-pkg", limitations)


if __name__ == "__main__":
    unittest.main()
