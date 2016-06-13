archivematica-src
=================

Archivematica installation from its source code repositories.

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
- `archivematica_src_reset_es`: set to true to delete the ElasticSearch indexes (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_am_all`: set to true to re-create the MCP db, clear the shared directory and reset ElasticSearch indexes (normally at runtime using `ansible-playbook` `--extra-vars` switch). If true, it overrides the two vars above.
- `archivematica_src_reset_ss_db`: set to true to re-create the SS database (normally at runtime using `ansible-playbook` `--extra-vars` switch)

- `archivematica_src_ss_run_syncdb`: run SS manage.py syncdb before migrate (for stable/0.7.x and previous branches that use Django 1.5.x) (default: false)
- `archivematica_src_ss_pip_missing_deps`:  workaround to install missing SS pip dependencies in old SS branches (default: false)

- archivematica_src_am_repo: AM repository (default: "https://github.com/artefactual/archivematica.git")
- archivematica_src_ss_repo: SS repository (default: "https://github.com/artefactual/archivematica-storage-service.git")

Dependencies
------------

N/A yet.

Example Playbooks
----------------

Please note that a complete Archivematica installation includes software not installed by this role. See https://github.com/artefactual/deploy-pub/tree/master/playbooks/archivematica for a more complete example.

It is also recommended to take backups of you system (Archivematica and Storage Service databases, AIPS, DIPS, etc) prior to running an upgrade.

1) For installing AM v1.4 (with SS v0.7):

```yaml
---
- hosts: "myserver"
  roles:
     - role: "archivematica-src"
  vars:
       archivematica_src_dir: "/opt/archivematica"
       archivematica_src_am_version: "stable/1.4.x"
       archivematica_src_ss_version: "stable/0.7.x"
       archivematica_src_ss_env_django_secret_key: "mysecretkey"
       archivematica_src_ss_run_syncdb: "true"
       archivematica_src_ss_pip_missing_deps: "true"
  become: "yes"
```

2) For installing AM v1.5 (with SS v0.8) using gunicorn/nginx:

```yaml
---
- hosts: "myserver"
  roles:
     - role: "archivematica-src"
  vars:
       archivematica_src_dir: "/opt/archivematica"
       archivematica_src_am_version: "stable/1.5.x"
       archivematica_src_ss_version: "stable/0.8.x"
       archivematica_src_ss_env_django_secret_key: "mysecretkey"
       archivematica_src_ss_gunicorn: "true"
       archivematica_src_am_dashboard_gunicorn: "true"
  become: "yes"
```

3) To upgrade a source-based AM v1.4 installation to v1.5 (SS v0.7 to v0.8) :

```yaml
---
- hosts: "myserver"
  roles:
     - role: "archivematica-src"
  vars:
       archivematica_src_dir: "/opt/archivematica"
       archivematica_src_am_version: "stable/1.5.x"
       archivematica_src_ss_version: "stable/0.8.x"
       archivematica_src_ss_env_django_secret_key: "mysecretkey"
       archivematica_src_ss_gunicorn: "true"
       archivematica_src_am_dashboard_gunicorn: "true"
       archivematica_src_am_migrate_from_v1_4: "true"
       archivematica_src_ss_migrate_from_v0_7: "true"

  become: "yes"
```

Please note that this last playbook is not idempotent, and it will throw an error if run twice. The two migrate related variables should be removed after a successful migration (an alternative could be to specify the `archivematica_src_am_migrate_from_v1_4` and `archivematica_src_ss_migrate_from_v0_7` at run time using `--extra-vars` instead of putting the variables in the playbook). 

License
-------

AGPLv3

Author Information
------------------

Artefactual Systems Inc.
http://www.artefactual.com
