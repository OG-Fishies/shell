import subprocess
import os

while True:
    
    q = input(f"{os.getcwd()}>")

    subprocess.run(q, shell=True)