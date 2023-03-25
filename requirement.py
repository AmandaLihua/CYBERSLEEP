import subprocess


def install_module(module):
    subprocess.check_call(["pip", "install", module])
    print(f"{module} a été installé")

modules = ["os", "datetime", "sys", "python-nmap", "fpdf", "pyfiglet", "termcolor", "google", "whois", "shodan", "requests", "beautifulsoup4"]

for module in modules:
    install_module(module)
