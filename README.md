# stephrobert.openscap

[![Maintainer](https://img.shields.io/badge/maintained%20by-stephrobert-e00000?style=flat-square)](https://github.com/stephrobert)
[![License](https://img.shields.io/github/license/stephrobert/ansible-role-openscap?style=flat-square)](https://github.com/stephrobert/ansible-role-openscap/blob/main/LICENSE)
[![Release](https://img.shields.io/github/v/release/stephrobert/ansible-role-openscap?style=flat-square)](https://github.com/stephrobert/ansible-role-openscap/releases)
[![Status](https://img.shields.io/github/workflow/status/stephrobert/ansible-role-openscap/Ansible%20Molecule?style=flat-square&label=tests)](https://github.com/stephrobert/ansible-role-openscap/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/stephrobert/openscap)[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)

⭐ Star us on GitHub — it motivates us a lot!

Install Oscap

**Platforms Supported**:

| Platform | Versions |
|----------|----------|
| Debian | bullseye |
| Ubuntu | jammy |

## ⚠️ Requirements

Ansible >= 2.11.

### Ansible role dependencies

None.

## ⚡ Installation

### Install with Ansible Galaxy

```shell
ansible-galaxy install stephrobert.openscap
```

### Install with git

If you do not want a global installation, clone it into your `roles_path`.

```bash
git clone git@github.com:stephrobert/ansible-role-openscap.git  stephrobert.openscap
```

But I often add it as a submodule in a given `playbook_dir` repository.

```bash
git submodule add git@github.com:stephrobert/ansible-role-openscap.git roles/stephrobert.openscap
```

As the role is not managed by Ansible Galaxy, you do not have to specify the
github user account.

### ✏️ Example Playbook

Basic usage is:

```yaml
- hosts: all
  roles:
    - role: stephrobert.openscap
      vars:
        content_version: 0.1.71
        install_content: false
        install_oscap: true
        oscap_version: 1.3.9
        reports_folder: /opt/openscap-reports
        scan: false
        
```

## ⚙️ Role Variables

Variables are divided in three types.

The **default vars** section shows you which variables you may
override in your ansible inventory. As a matter of fact, all variables should
be defined there for explicitness, ease of documentation as well as overall
role manageability.

The **context variables** are shown in section below hint you
on how runtime context may affects role execution.

### Default variables
Role default variables from `defaults/main.yml`.

| Variable Name | Value |
|---------------|-------|
| install_content | False |
| install_oscap | True |
| oscap_version | 1.3.9 |
| content_version | 0.1.71 |
| scan | False |
| reports_folder | /opt/openscap-reports |

### Context variables

Those variables from `vars/*.{yml,json}` are loaded dynamically during task
runtime using the `include_vars` module.

Variables loaded from `vars/main.yml`.




## Author Information

none