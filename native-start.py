from sys import platform, executable, argv
import subprocess


if platform == "win64":
    subprocess.run([executable, "main.py"] + argv[1:])

if platform.startswith("windows"):
    subprocess.run([executable, "main.py"] + argv[1:])
