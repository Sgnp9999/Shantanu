import subprocess

subprocess.run(['cd', '/home/ec2-user/git_demo'])
# subprocess.run(['aws', 's3', 'cp', 'README.md', 's3://snowflake-lld-tcs-logo'])
subprocess.run(['git', 'add', 'README.md'])
subprocess.run(['git', 'commit', '-m', '"add"'])
subprocess.run(['git', 'push'])