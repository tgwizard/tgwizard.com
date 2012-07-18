from fabric.api import *

# TODO: change this to proper domain name
env.hosts = ['tgwizard.com']

def deploy():
	local("git push")

	code_dir = "/var/www/tgwizard.com"
	with cd(code_dir):
		run("git pull -f")
