archivematica-src
=================

Full Archivematica installation from its source code repositories.

Requirements
------------

N/A yet.

Role Variables
--------------

- `archivematica_src_install_am`: install pipeline code (default: "yes")
- `archivematica_src_install_ss`: install storage service (default: "yes")
- `archivematica_src_install_sample_data`: copy sample data (default: "yes")
- `archivematica_src_install_devtools`: install archivematica-devtools (default: "no")

- `archivematica_src_dir`: location where the repos are cloned (default: ansible user home)

- `archivematica_src_am_version`: AM branch (tag or commit) to install
- `archivematica_src_ss_version`: SS branch (tag or commit) to install
- `archivematica_src_reset_mcpdb`: set to true to re-create the MCP database (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_devtools_version`: archivematica-devtools branch (tag or commit) to install (default: master)


Dependencies
------------

N/A yet.

Example Playbook
----------------

```yaml
---
- hosts: "servers"
  roles:
     - role: "archivematica-src"
       archivematica_src_dir: "/opt/archivematica"
       archivematica_src_am_version: "remotes/origin/qa/1.x"
       archivematica_src_ss_version: "remotes/origin/qa/0.x"
  sudo: "yes"
```

License
-------

N/A yet.

Author Information
------------------

Artefactual Systems Inc.
http://www.artefactual.com
