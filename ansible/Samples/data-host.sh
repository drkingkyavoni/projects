#!/bin/bash

: <<'EOF'
	Create a shell script called host_data.sh under ~/playbooks/ directory and make it executable.

	The shell script should:

	Set ANSIBLE_GATHERING to False

	Run an ad-hoc command to print the uptime of all managed nodes in the inventory file ~/playbooks/inventory

	Create and run a playbook ~/playbooks/playbook.yml to cat the file /etc/redhat-release on all managed nodes in the inventory file ~/playbooks/inventory. Also please make sure to run this playbook in verbose mode i.e just add -vv at the end of your ansible-playbook command.
EOF

export ANSIBLE_GATHERING=False

ansible all -a uptime -i ~/playbooks/inventory

cat <<EOF > ~/playbooks/playbook.yml
---
- hosts: all
  tasks:
    - command: cat /etc/redhat-release
EOF

ansible-playbook -vv -i ~/playbooks/inventory ~/playbooks/playbook.yml