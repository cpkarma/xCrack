import subprocess
import sys

modules = [
    "requests",
    "colorama",
    "beautifulsoup4",
    "paramiko",
    "urllib3"
]

def install_modules():
    for module in modules:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"[+] Successfully installed: {module}")
        except subprocess.CalledProcessError:
            print(f"[-] Failed to install: {module}")

if __name__ == "__main__":
    install_modules()
