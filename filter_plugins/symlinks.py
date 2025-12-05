def to_symlink_map(devices, cloud_id, virtualization_engine):
    if cloud_id == "nocloud" and virtualization_engine == "kvm":
        symlink_map = {
            device.get("serial"): device.get("path")
            for device in devices.get("blockdevices")
            if device.get("type") == "disk"
        }
        return symlink_map


class FilterModule(object):
    def filters(self):
        return {"to_symlink_map": to_symlink_map}
