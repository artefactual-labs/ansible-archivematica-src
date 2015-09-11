archivematica-src
=================

Full Archivematica installation from its source code repositories.

Requirements
------------

N/A yet.

Role Variables
--------------

N/A yet.

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
       amdev_branch: "remotes/origin/qa/1.x"
       ssdev_version: "remotes/origin/qa/0.x"
  sudo: "yes"
```

License
-------

N/A yet.

Author Information
------------------

Artefactual Systems Inc.
http://www.artefactual.com