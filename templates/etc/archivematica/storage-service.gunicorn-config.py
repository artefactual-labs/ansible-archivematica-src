# {{ ansible_managed }}
# Documentation: http://docs.gunicorn.org/en/stable/configure.html
# Example: https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py

# http://docs.gunicorn.org/en/stable/settings.html#user
user = "{{ archivematica_user }}"

# http://docs.gunicorn.org/en/stable/settings.html#group
group = "{{ archivematica_group }}"

# http://docs.gunicorn.org/en/stable/settings.html#bind
bind = "{{ archivematica_src_ss_bind }}"

# http://docs.gunicorn.org/en/stable/settings.html#workers
workers = 1

# http://docs.gunicorn.org/en/stable/settings.html#timeout
timeout = 120

# http://docs.gunicorn.org/en/stable/settings.html#reload
reload = {{ 'True' if is_dev else 'False' }}

# http://docs.gunicorn.org/en/stable/settings.html#chdir
chdir = "{{ archivematica_src_ss_app_dir }}"

# http://docs.gunicorn.org/en/stable/settings.html#raw-env
raw_env = [
{% for key, value in archivematica_src_ss_environment.iteritems() %}
    "{{ key }}={{ value }}",
{% endfor %}
]

# http://docs.gunicorn.org/en/stable/settings.html#accesslog
accesslog = "/var/log/archivematica/storage-service/gunicorn.access_log"

# http://docs.gunicorn.org/en/stable/settings.html#errorlog
errorlog = "/var/log/archivematica/storage-service/gunicorn.error_log"

# http://docs.gunicorn.org/en/stable/settings.html#loglevel
loglevel = "{{ 'debug' if is_dev else 'info' }}"

# http://docs.gunicorn.org/en/stable/settings.html#proc-name
proc_name = "archivematica-storage-service"
