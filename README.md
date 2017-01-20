archivematica-src
=================

Archivematica installation from its source code repositories.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Role Variables](#role-variables)
  - [General](#general)
  - [Projects](#projects)
  - [Version](#version)
  - [Reset](#reset)
  - [Legacy support](#legacy-support)
  - [Remote repository](#remote-repository)
  - [External package dependencies repository](#external-package-dependencies-repository)
  - [Web server](#web-server)
    - [SSL (when using gunicorn/nginx)](#ssl-when-using-gunicornnginx)
- [Tags](#tags)
- [Dependencies](#dependencies)
- [Example Playbooks](#example-playbooks)
- [License](#license)
- [Author Information](#author-information)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


Role Variables
--------------

### General

- `archivematica_src_dir`: location where the source code repositories are cloned (default: user home)

### Projects

- `archivematica_src_install_am`: install pipeline code (default: "yes")
- `archivematica_src_install_ss`: install storage service (default: "yes")
- `archivematica_src_install_sample_data`: copy sample data (default: "yes")
- `archivematica_src_install_devtools`: install archivematica-devtools (default: "no")
- `archivematica_src_install_automationtools`: install automation-tools (default: "no")
- `archivematica_src_install_appraisaltab`: install appraisal-tab (default: "no") (WIP)

### Version

- `archivematica_src_am_version`: AM branch (tag or commit) to install
- `archivematica_src_ss_version`: SS branch (tag or commit) to install
- `archivematica_src_devtools_version`: archivematica-devtools branch (tag or commit) to install (default: master)
- `archivematica_src_automationtools_version`: automation-tools branch (tag or commit) to install (default: master)

### Reset

- `archivematica_src_reset_mcpdb`: set to true to re-create the MCP database (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_shareddir`: set to true to re-create the shared directory (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_es`: set to true to delete the ElasticSearch indexes (normally at runtime using `ansible-playbook` `--extra-vars` switch)
- `archivematica_src_reset_am_all`: set to true to re-create the MCP db, clear the shared directory and reset ElasticSearch indexes (normally at runtime using `ansible-playbook` `--extra-vars` switch). If true, it overrides the two vars above.
- `archivematica_src_reset_ss_db`: set to true to re-create the SS database (normally at runtime using `ansible-playbook` `--extra-vars` switch)

### Legacy support

- `archivematica_src_ss_run_syncdb`: run SS manage.py syncdb before migrate (for stable/0.7.x and previous branches that use Django 1.5.x) (default: false)
- `archivematica_src_ss_pip_missing_deps`:  workaround to install missing SS pip dependencies in old SS branches (default: false)
- `archivematica_src_am_migrate_from_v1_4`: Migrate AM database from v1.4 to v1.5 (default: false)
- `archivematica_src_ss_migrate_from_v0_7`: Migrate SS database from v0.7 to v0.8 (default: false)

### Remote repository

- `archivematica_src_am_repo`: AM repository (default: `"https://github.com/artefactual/archivematica.git"`)
- `archivematica_src_ss_repo`: SS repository (default: `"https://github.com/artefactual/archivematica-storage-service.git"`)

### External package dependencies repository
- `archivematica_src_externals_repo`: externals package server url or ppa (`http://<server>/<repository>` or `ppa:<name>`) (default: `"http://packages.archivematica.org/1.5.x/ubuntu-externals"`) 
- `archivematica_src_externals_repo_key_id`: repository key id  (ignored for ppa) (default: `"0x5236CA08"`)
- `archivematica_src_externals_repo_key_url`: repository key url (ignored for ppa) (default: `"https://packages.archivematica.org/GPG-KEY-archivematica"`)

### Web server

- `archivematica_src_ss_gunicorn`: use gunicorn/nginx instead of uwsgi/nginx for the Storage Service. For Storage Service branch stable/0.8.x or newer (default:`false`)
- `archivematica_src_am_dashboard_gunicorn`: use gunicorn/nginx instead of apache/mod_wsgi for Archivematica Dashboard. For Archivematica branch stable/1.5.x or newer (default:`false`)

#### SSL (when using gunicorn/nginx)

- `archivematica_src_ssl`: configure Storage Service and Dashboard to use SSL (default:`false`)
- `archivematica_src_ssl_include_acme_chlg_loc`: Include ACME challenge location file (`acmetool-location.conf`) in nginx configuration file, provided by role https://github.com/artefactual-labs/ansible-acmetool (default:`false`)
- `archivematica_src_ssl_fullchain`:  (no default provided, shall be defined in the playbook or host_vars if SSL enabled)
- `archivematica_src_ssl_privkey`: (no default provided, shall be defined in the playbook or host_vars if SSL enabled)



Tags
----

Tags can be used to control which parts of the playbook to run, especially on updates.
Note that if something is disabled with the [role variables](#role-variables), it won't be run even if the tag is enabled.

- `amsrc-ss`: Storage service install
    - `amsrc-ss-clone`: Checkout source code
    - `amsrc-ss-osdep`: Install operating system dependencies
    - `amsrc-ss-pydep`: Install Python dependencies (with pip)
    - `amsrc-ss-osconf`: Configure operating system
    - `amsrc-ss-code`: Install source code
        - `amsrc-ss-code-collectstatic`: Run Django's collectstatic
    - `amsrc-ss-db`: Configure database
    - `amsrc-ss-websrv`: Configure webserver
- `amsrc-pipeline`: Archivematica pipeline install
    - `amsrc-pipeline-clonecode`: Checkout source code
    - `amsrc-pipeline-deps`: Install & configure operating system & Python dependencies
    - `amsrc-pipeline-osconf`: Configure operating system
    - `amsrc-pipeline-instcode`: Install source code
    - `amsrc-pipeline-dbconf`: Configure database
        - `amsrc-pipeline-dbconf-syncdb`: Only run Django's syncdb/migrations
    - `amsrc-pipeline-websrv`: Configure webserver
- `amsrc-devtools`: Archivematica devtools install
- `amsrc-automationtools`: Automation tools install
- `amsrc-appraisaltab`: Appraisal tab install

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
       archivematica_src_externals_repo: "ppa:archivematica/1.4" 

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

3) For installing AM v1.5 (with SS v0.8) using gunicorn/nginx, with SSL:

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
       archivematica_src_ssl: "true"
       archivematica_src_ssl_fullchain: "/location/of/fullchain/file"
       archivematica_src_ssl_privkey: "/location/of/private/key/file"       
       # if using LE SSL certs configured with artefactual-labs/ansible-acmetool, also include the next line (uncomment)
       #archivematica_src_ssl_include_acme_chlg_loc: True  
  become: "yes"
```


4) To upgrade a source-based AM v1.4 installation to v1.5 (SS v0.7 to v0.8) :

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
