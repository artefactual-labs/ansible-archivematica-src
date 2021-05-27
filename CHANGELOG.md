# CHANGELOG

This document describes important changes in this role.

Most recent changes first:

- Variables `archivematica_src_pip_version`,
  `archivematica_src_setuptools_version` and `archivematica_src_wheel_version`
  are abandoned since we don't need them in the Python 3 environment.

- Variables `archivematica_src_install_devtools` and
  `archivematica_src_devtools_version` are abandoned since Archivematica v1.13
  deprecated the archivematica-devtools repository. Users should rely on
  existing Archivematica management commands.
