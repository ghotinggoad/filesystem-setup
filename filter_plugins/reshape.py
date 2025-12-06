def to_symlink_map(ansible_facts):
    virtualization_type = ansible_facts.get("virtualization_type")
    system_vendor = ansible_facts.get("system_vendor")
    if virtualization_type == "kvm" and system_vendor == "QEMU":
        symlink_map = {
            device.get("links").get("ids")[0][-5:]: "/dev/" + device_key
            for device_key, device in ansible_facts.get("devices").items()
            if device.get("model") == "QEMU HARDDISK"
        }
        return symlink_map


def to_lvs(vdisks):
    lvs = {
        persistent_mount_name: {**persistent_mount, "vdisk_name": vdisk_name}
        for vdisk_name, vdisk in vdisks.items()
        for persistent_mount_name, persistent_mount in vdisk.get(
            "persistent_mounts"
        ).items()
    }
    return lvs


class FilterModule(object):
    def filters(self):
        return {"to_symlink_map": to_symlink_map, "to_lvs": to_lvs}
