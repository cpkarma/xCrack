import subprocess
import sys

a = [
    "requests",
    "colorama",
    "beautifulsoup4",
    "paramiko",
    "urllib3",
    "pyarmor"
]

def b():
    for c in a:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", c])
            print(f"[+] Successfully installed: {c}")
        except subprocess.CalledProcessError:
            print(f"[-] Failed to install: {c}")

if __name__ == "__main__":
    b()