import subprocess

def verifie_module(module):
    try:
        __import__(module)
        print(f"{module} est déjà présent sur votre environnement")
    except ImportError:
        print(f"{module} n'est pas sur votre environnement")
        installe_module(module)

def installe_module(module):
    subprocess.check_call(["pip", "install", module])
    print(f"{module} a été installé sur votre environnement.")

modules = ["os", "datetime", "sys", "python-nmap", "fpdf", "pyfiglet", "termcolor", "google", "python-whois", "shodan", "requests", "beautifulsoup4"]

for module in modules:
    verifie_module(module)

installe_module("google")