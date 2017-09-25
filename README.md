archivematica-src
=================

Archivematica installation from its source code repositories.

**Table of Contents**

- [Role Variables](#role-variables)
- [Tags](#tags)
- [Dependencies](#dependencies)
- [Example Playbooks](#example-playbooks)
- [License](#license)
- [Author Information](#author-information)


Role Variables
--------------

See [`defaults/main.yml`](defaults/main.yml) for a comprehensive list of variables.


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


Dependencies
------------

This role doesn't have dependencies with other roles.

Please use Ansible 2.3 or newer with this role.


Example Playbooks
-----------------

Please note that a complete Archivematica installation includes software not installed by this role, in particular:

- MySQL compatible database server (MySQL, MariaDB, Percona)
- Elasticsearch
- ClamAV (daemon and client)

See https://github.com/artefactual/deploy-pub/tree/master/playbooks/archivematica to find examples.

It is also recommended to take backups of your system (Archivematica and Storage Service databases, AIPS, DIPS, etc) prior to running an upgrade.


License
-------

AGPLv3


Author Information
------------------

Artefactual Systems Inc.
https://www.artefactual.com
