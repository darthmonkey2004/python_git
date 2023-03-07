from distutils.core import setup

setup(name='python_git',
	version='1.0',
	description='simple python class that uses subprocess and git.',
	author='Matt McClellan',
	author_email='darthmonkey2004@gmail.com',
	url='http://nplayer.simiantech.biz/',
	packages=['python_git'],
	package_dir={'python_git': 'python_git'},
	scripts=['python_git/git.py', 'python_git_install.sh'],
	)
