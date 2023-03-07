# python_git

"""git python helper class - (python_np.utils.git)
This is a python object intended to help with pushing updating a git repository via the command line.
Capabilities:
	1. uses keystore to securely store token long-term
	2. sets up local repo with credentialStorage key 'plaintext'
		(NOTE: doesn't actually use plaintext, only creates
		token storage file before and deletes after push.
		TOKEN IS STORED IN KEYRING, User authentication will be required.)
	3. tracks current repository state (up to date, commit needed, etc) and
		keeps current with checked out branch/remote origin and other metadata.
	4. TODO: git.clone(repo_url)
	5. TODO: git.init(path)
"""
