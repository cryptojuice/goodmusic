import multiprocessing

workers = 3
bind = '127.0.0.1:8000'
proc_name = 'gunicorn'
pidfile = '/tmp/gunicorn.pid'
logfile = '/tmp/gunicorn.log'
worker_class = 'gevent'
debug = False
