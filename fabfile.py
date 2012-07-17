from fabric.api import *

# TODO: change this to proper domain name
env.hosts = ['adam@176.58.115.169']

def deploy():
	code_dir = "/var/www/tgwizard.com"
	with cd(code_dir):
		run("git pull -f")
