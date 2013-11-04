#!/bin/bash
watchmedo shell-command --patterns="*.py;*.html;*.css;*.js" --recursive --command='echo "${watch_src_path}" && sudo kill -HUP `cat /tmp/gunicorn.pid`' /vagrant/.
