import subprocess

def check_module(module):
    try:
        __import__(module)
        print(f"{module} est déjà présent sur votre environnement")
    except ImportError:
        print(f"{module} n'est pas sur votre environnement")
        install_module(module)

def install_module(module):
    subprocess.check_call(["pip", "install", module])
    print(f"{module} a été installé")

modules = ["os", "datetime", "sys", "nmap", "fpdf", "pyfiglet", "termcolor", "google", "whois", "shodan", "requests", "beautifulsoup4"]

for module in modules:
    check_module(module)
