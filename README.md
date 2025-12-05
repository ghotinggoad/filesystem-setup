# filesystem-setup
An Ansible playbook that provisions and mount Logical Volumes in Linux VMs given an input filesystem layout.
This project was tested on Rocky9 and Ubuntu Noble Server.
Symlink mapping is currently implemented and tested only on Proxmox VE, support for other clouds can be added by modifying symlinks.py.

## Feature(s)
- Provision and mount Logical Volumes given desired filesystem layout.
- Supports simultaneously configuring VMs of different Linux Distros and inputs.
- Automatically detect device path using disk interface and serial.
- Compatible with Terraform output ansible_inventory from my Terraform projects.
___
## Limitation(s)
- Disk serial must be interface name, symlinks.py need to be modified if udev name changes (i.e. use different cloud providers)
___
## Requirement(s)
- **CHECK LIMITATION(S)**
___
## Instructions
1. Create inventory.json referencing sample_inventory.json
2. Run "ansible-playbook -i inventory.json filesystem_setup.yml"
___
## License
filesystem-setup is licensed under the MIT license, see [LICENSE](LICENSE) for details.
