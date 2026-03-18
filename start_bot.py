import subprocess
import os
import sys

env = os.environ.copy()
env['PYTHONPATH'] = r'd:\jonlitaxi'

python_exe = sys.executable

subprocess.Popen([python_exe, r'd:\jonlitaxi\bot\main.py'], env=env)
print("Bot started in background")
