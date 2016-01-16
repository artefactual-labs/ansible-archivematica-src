archivematica-src
=================

Full Archivematica installation from its source code repositories.

Note that the role currently does not handle database migrations completely.
Do not use to upgrade production systems with old versions of Archivematica or
the Storage Service (unless you know what you are doing).

Requirements
------------

N/A yet.

Role Variables
--------------

- `archivematica_src_dir`: location where the source code repositories are cloned (default: user home)

- `archivematica_src_install_am`: install pipeline code (default: "yes")
- `archivematica_src_install_ss`: install storage service (default: "yes")
- `archivematica_src_install_sample_data`: copy sample data (default: "yes")
- `archivematica_src_install_devtools`: install archivematica-devtools (default: "no")
- `archivematica_src_install_automationtools`: install automation-tools (default: "no")
- `archivematica_src_install_appraisaltab`: install appraisal-tab (default: "no") (WIP)

- `archivematica_src_am_version`: AM branch (tag or commit) to install
- `archivematica_src_ss_version`: SS branch (tag or commit) to install
- `archivematica_src_devtools_version`: archivematica-devtools branch (tag or commit) to install (default: master)
- `archivematica_src_automationtools_version`: automation-tools branch (tag or commit) to install (default: master)

- `archivematica_src_reset_mcpdb`: set to true to re-create the MCP database (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_shareddir`: set to true to re-create the shared directory (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_am_all`: set to true to re-create the MCP db and shared directory (normally at runtime using `ansible-playbook` `--extra-vars` switch). If true, it overrides the two vars above.
- `archivematica_src_reset_ss_db`: set to true to re-create the SS database (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_am_pre_migration`: set to true to load the mysql seed file and run mysql_dev scripts instead of Django migrations

- `archivematica_src_ss_run_syncdb`: run SS manage.py syncdb before migrate (for stable/0.7.x and previous branches that use Django 1.5.x) (default: false)
- `archivematica_src_ss_pip_missing_deps`:  workaround to install missing SS pip dependencies in old SS branches (default: false)

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
