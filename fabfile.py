from fabric.api import run, env, cd
from fabric.operations import put

env.hosts = ['clebikes.com']
env.forward_agent = True

def test():
    run("uname -s")

def upgrade():
    
    with cd("/home/matt/srv/clebikes/"):
        run("git pull")
        put("clebikes/prod-settings.py", "clebikes/settings.py")
        run("killall gunicorn")
        run("../env/bin/gunicorn clebikes.wsgi:application -D -w 4 --log-file gunicorn.log")
        run("uname -s")


