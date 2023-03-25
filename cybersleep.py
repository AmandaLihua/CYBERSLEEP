import os # fournit une interface pour interagir avec le système d'exploitation sous-jacent
import nmap # permet de réaliser des scans de ports et de vulnérabilités réseau
import datetime # fournit des classes pour manipuler des dates et des heures
from fpdf import FPDF # une bibliothèque pour créer des fichiers PDF à partir de Python
import pyfiglet # une bibliothèque pour créer des textes stylisés en ASCII art
import sys # fournit des fonctions et des variables utilisées pour manipuler la structure du système d'exploitation
from termcolor import colored # permet de modifier la couleur du texte dans la console
from googlesearch import search # fournit une interface pour effectuer des recherches Google à partir de Python
import whois # permet de récupérer des informations WHOIS à propos d'un domaine
import shodan # fournit une interface pour interagir avec le moteur de recherche Shodan
import requests # une bibliothèque HTTP Python permettant d'envoyer des requêtes HTTP
from bs4 import BeautifulSoup #une bibliothèque pour extraire des informations à partir de pages web en HTML et XML


# Créer une instance de la classe Figlet en choisissant une police de caractères
custom_fig = pyfiglet.Figlet(font='slant')
# Utiliser la méthode renderText() pour créer une chaîne de caractères ASCII art
ascii_banner = custom_fig.renderText('Amanda SDV')
# Afficher la chaîne ASCII art à l'écran
print(ascii_banner)


# Mes fonctions

def programme_1 () :
    def rapport_pdf(cible, output_file):
        # Génère un rapport PDF à partir des résultats de la numérisation
        # Obtient le nom de fichier du rapport PDF à partir du nom de fichier de sortie de la numérisation
        fichier = os.path.splitext(output_file)[0] + ".pdf"
        
        # Lit le contenu du fichier de sortie de la numérisation
        with open(output_file, "r") as f:
            lines = f.readlines()
        report_text = "".join(lines)
        
        # Crée un objet FPDF et ajoute une page
        pdf = FPDF()
        pdf.add_page()
        
        # Définit la police et la taille du texte pour le titre du rapport
        pdf.set_font("Arial", "B", size=18)
        
        # Ajoute le titre et la cible du rapport au PDF
        pdf.cell(200, 10, txt="Scan de Vunérabilité - NMAP", ln=1, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Cible: " + cible, ln=1, align="L")
        pdf.cell(200, 10, txt="Date: " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), ln=1, align="L")
        pdf.cell(200, 10, txt="", ln=1, align="L")
        
        # Ajoute le contenu du rapport au PDF
        pdf.multi_cell(0, 10, txt=report_text)
        
        # Génère le fichier PDF à partir du contenu et l'enregistre sur le disque
        pdf.output(fichier)
        
        # Affiche un message pour confirmer l'emplacement du fichier de rapport
        print(colored(f"Rapport sauvgardé dans : {fichier}","green"))

    def main():
        # Boucle infinie pour afficher le menu principal
        while True:
            print(" ")
            print(colored("Programme : Scan de port","blue"))
            print("-------------------------")

            # Crée un objet Nmap scanner pour effectuer des scans de port
            scanner = nmap.PortScanner()

            # Affiche le menu pour le choix des options de numérisation
            print("""\nVeuillez choisir votre type de scan :
                1] Scan SYN ACK (TCP)
                2] Scan UDP
                3] Scan de détection de version OS
                4] Scan Intense 
                5] Scan top 20 des ports 
                6] Quitter le programme \n""")
            reponse = input("Votre choix : ")
            print("Vous avez choisi : ", reponse)

            if reponse == "1":
                # Effectue un scan SYN ACK (TCP)
                adresse_ip = input("Entree un adresse IP : ")
                print("Adresse IP cible est : ", adresse_ip)
                output_file = input("Entrez le nom du fichier pdf : ")
                scanner.scan(hosts=adresse_ip, arguments="-sS -T4 -oN " + output_file)
                rapport_pdf(adresse_ip, output_file)
                
                
            elif reponse == "2":
                # Effectue un scan UDP
                adresse_ip = input("Entree un adresse IP : ")
                print("Adresse IP cible est : ", adresse_ip)
                output_file = input("Entrez le nom du fichier pdf : ")
                scanner.scan(hosts=adresse_ip, arguments="-sU -T4 -oN " + output_file)
                rapport_pdf(adresse_ip, output_file)
                
            elif reponse == "3":
                # Effectue un scan pour detecter l'OS
                adresse_ip = input("Entree un adresse IP : ")
                print("Adresse IP cible est : ", adresse_ip)
                output_file = input("Entrez le nom du fichier pdf : ")
                scanner.scan(hosts=adresse_ip, arguments="-O -oN " + output_file)
                rapport_pdf(adresse_ip, output_file)
                
            elif reponse == "4":
                # Effectue un scan Intense
                adresse_ip = input("Entree un adresse IP : ")
                print("Adresse IP cible est : ", adresse_ip)
                output_file = input("Entrez le nom du fichier pdf : ")
                scanner.scan(hosts=adresse_ip, arguments="-T4 -A -v -oN " + output_file)
                rapport_pdf(adresse_ip, output_file)
                
            elif reponse == "5":
                # Effectue un scan sur les 20 ports les plus scannés
                adresse_ip = input("Entree un adresse IP : ")
                print("Adresse IP cible est : ", adresse_ip)
                output_file = input("Entrez le nom du fichier pdf : ")
                scanner.scan(hosts=adresse_ip, arguments="--top-ports 20 -oN " + output_file)
                rapport_pdf(adresse_ip, output_file)
                
            elif reponse == "6":
                print("Vous avez quittez le programme de scan")
                break
            else : 
                print("Entrer un nombre valide 1-2-3-4-5-6")      
    main () 

def programme_2 () :
    # fonction principale
    def main():
        # boucle while pour afficher le menu jusqu'à ce que l'utilisateur quitte le programme
        while True:
            # afficher le titre du programme
            print(" ")
            print(colored("Programme : Recherche OSINT sur un domaine stratégique - Google dorks ", "blue"))
            print("----------------------------------------------------------------------")

            # afficher les options du menu
            print("""\nQue souhaitez vous faire :
                1] Faire une recherche Google dorks
                2] Quitter le programme Google dorks \n""")
            reponse = input("Votre choix : ")
            print("Vous avez choisi : ", reponse)

            # si l'utilisateur choisit l'option 1
            if reponse == "1":

                # demander à l'utilisateur le nom du fichier de sauvegarde des liens
                fichier = input("Saisir le nom du fichier ou seront sauvgarder les liens : ")

                # définir une fonction pour écrire les résultats dans un fichier texte
                def fichier_resultat(data):
                    file = open((fichier) + ".txt", "a")
                    file.write(str(data))
                    file.write("\n")
                    file.close()

                # définir une fonction pour créer un fichier PDF à partir du fichier texte
                def pdf():
                    # obtenir le nom du fichier texte à partir de l'entrée de l'utilisateur
                    txt_file_name = fichier + ".txt"
                    # ouvrir le fichier texte et lire son contenu
                    with open(txt_file_name, "r") as f:
                        text = f.read()
                    # créer un objet PDF
                    pdf = FPDF()
                    pdf.add_page()
                    # ajouter le titre et le contenu au fichier PDF
                    pdf.set_font("Arial", "B", size=18)
                    pdf.cell(200, 10, txt="Recherche OSINT sur un domaine stratégique - Google dorks", ln=1, align="C")
                    pdf.set_font("Arial", size=12)
                    pdf.multi_cell(0, 10, text)
                    # obtenir le nom du fichier PDF à partir de l'entrée de l'utilisateur
                    pdf_file_name = fichier + ".pdf"
                    # enregistrer le fichier PDF
                    pdf.output(pdf_file_name)
                    print(colored("Fichier PDF crée : " + pdf_file_name, "green"))
                    print(" ")

                # afficher des exemples de dorks Google
                print(colored("""\n Exemples : 
                    Restreindre les résultats à ceux d'un certain type de fichier. Par exemple, PDF, DOCX, TXT, PPT -> filetype:pdf exemple
                    Trouver des sites liés à un domaine donné -> related:exemple.com
                    Trouver des pages dont le titre contient un ou plusieurs mots précis -> intitle:exemple
                    Trouver des pages contenant un certain mot (ou des mots) quelque part dans le contenu -> intext:exemple
                    Recherche de pages contenant un ou plusieurs mots dans l'URL -> inurl:exemple
                    Obliger Google à afficher les résultats d'une recherche géographique sur une carte -> map:exemple\n""", "yellow"))

                # demande à l'utilisateur d'entrer le google dork à utiliser
                google_dork = input("Veuillez saisir un google dork : ")
                # demande à l'utilisateur combien de sites il souhaite afficher
                compteur = input("Combien de site souhaitez-vous afficher : ")
                print("\n")

                requetes = 0    # initialisation du nombre de requêtes effectuées
                nombre_resultat = 0 # initialisation du nombre de résultats affichés
                
                # boucle qui effectue la recherche avec le google dork et affiche les résultats
                for resultat in search(google_dork, tld="com", num=int(compteur),start=0, stop=None, pause=2):
                    nombre_resultat=nombre_resultat+1  # incrémente le nombre de résultats affichés
                    print(nombre_resultat , " - " , resultat)  # affiche le numéro du résultat et son URL
                    requetes+=1 # incrémente le nombre de requêtes effectuées

                    data = (nombre_resultat,resultat)
                    fichier_resultat(data)   # enregistre le numéro du résultat et son URL dans un fichier texte

                    # arrête la boucle si le nombre de résultats affichés atteint le nombre demandé par l'utilisateur
                    if requetes >= int(compteur):
                        break
                pdf()
            elif reponse == "2":
                print("Vous avez quittez le programme Google dorks")
                break
            else : 
                print("Entrer un nombre valide 1-2")
    main () 

def programme_3():
    # fonction principale
    def main():
        # boucle while pour afficher le menu jusqu'à ce que l'utilisateur quitte le programme       
        while True:
            # afficher le titre du programme
            print(" ")
            print(colored("Programme : Collecte du modèle MITRE ATTCK d’une menace ", "blue"))
            print("--------------------------------------------------------")
            # afficher les options du menu
            print("""\nQue souhaitez vous faire :
                1] Faire une collecte du modèle MITRE ATTCK
                2] Quitter le programme Collecte \n""")
            reponse = input("Votre choix : ")
            print("Vous avez choisi : ", reponse)

            if reponse == "1":
                # Affichage des choix possibles pour la collecte
                print(colored("""
                    Tactique -> https://attack.mitre.org/tactics/enterprise/
                    Technique -> https://attack.mitre.org/techniques/enterprise/
                    Mitigation -> https://attack.mitre.org/mitigations/enterprise/ \n""", "yellow"))
                
                # URL de base pour les choix de l'utilisateur
                choix1 = "https://attack.mitre.org/tactics/enterprise/"
                choix2 = "https://attack.mitre.org/techniques/enterprise/"
                choix3 = "https://attack.mitre.org/mitigations/enterprise/"

                 # afficher les options du menu
                print("""\nQue souhaitez vous collecter :
                    1] Tactique
                    2] Technique
                    3] Mitigation \n""")
                resp = input("Votre choix : ")
                print("Vous avez choisi : ", resp)

                # En fonction du choix de l'utilisateur, on récupère l'URL correspondante
                if resp == "1":
                    url = choix1
                elif resp == "2":
                    url = choix2
                elif resp == "3":
                    url = choix3

                # On exécute une requête HTTP vers l'URL donnée. On récupère les données HTML que le serveur renvoie et on stocke ces données en les parsant
                res = requests.get(url)
                html_page = res.content
                soup = BeautifulSoup(html_page, 'html.parser')
                text = soup.find_all(text=True)

                # On indique dans liste les balises HTML que l'on ne souhaite pas prendre en compte dans la collecte
                output = ''
                liste =[
                    '[document]',
                    'noscript',
                    'header',
                    'html',
                    'meta',
                    'head',
                    'input',
                    'script',
                ]

                # On parcourt le texte et on concatène les éléments non présents dans la liste
                for i in text:
                    if i.parent.name not in liste:
                        output += '{} '.format(i)

                # On affiche tous les résultats, sauf ceux qui contiennent les éléments dans la liste     
                print(output)
            elif reponse == "2":
                print("Vous avez quittez le programme Collecte")
                break
            else : 
                print("Entrer un nombre valide 1-2")
    main () 

def programme_4():
    def main():
        # Boucle pour permettre à l'utilisateur de faire plusieurs recherches sans quitter le programme
        while True:
            # Initialize the Shodan API client with your API key
            SHODAN_API_KEY = "GCfphiJloWlMiw710fKoK01T6hyZjAJ9"
            api = shodan.Shodan(SHODAN_API_KEY)

            print(" ")
            print(colored("Programme : Shodan ", "blue"))
            print("-------------------")

            # Menu principal pour afficher les options disponibles
            print("""\nQue souhaitez-vous faire :
            1] Recherche Shodan
            2] Recherche d'un hôte (OS)
            3] Recherche de base Shodan (toutes les IP)
            4] Collecte d'informations sommaires à l'aide de facettes
            5] Quitter le programme Shodan\n""")
            
            # Demande à l'utilisateur de saisir une option
            reponse = input("Votre choix : ")
            print("Vous avez choisi : ", reponse)

            # Si l'utilisateur choisit l'option 1
            if reponse == "1":
                print(colored("Exemple : apache, google", "yellow"))
                
                # Demande à l'utilisateur de saisir un terme à rechercher
                reponse2 = input("Saisir un nom : ")
                resultat = api.search(reponse2)

                # Affiche le nombre de résultats trouvés
                print('Résultat trouvés : {}'.format(resultat['total']))
                
                # Parcourir les résultats et afficher l'adresse IP et les données correspondantes
                for result in resultat['matches']:
                    print('IP: {}'.format(result['ip_str']))
                    print(result['data'])
                    print('')

            # Si l'utilisateur choisit l'option 2
            elif reponse == "2":
                print(colored("Exemple : 8.8.8.8 ", "yellow"))
                # Demande à l'utilisateur de saisir une adresse IP
                reponse = input("Saisir un adresse IP : ")
                host = api.host(reponse)

                # Affiche des informations générales sur l'hôte
                print("""
                    IP : {}
                    Organisation : {}
                    Systeme d'exploitation : {}
                """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

                # Parcourir tous les bannières et afficher les détails de chaque port
                for item in host['data']:
                    print("""
                            Port: {}
                            Banner: {}

                    """.format(item['port'], item['data']))

            # Si l'utilisateur choisit l'option 3
            elif reponse == "3":
                print(colored("Exemple : apache , google", "yellow"))
                # Demande à l'utilisateur de saisir un terme à rechercher
                reponse = input("Saisir un nom : ")
                resultat = api.search(reponse)

                # Boucle à travers les résultats et affiche chaque adresse IP
                for service in resultat['matches']:
                    print (service['ip_str'])

            elif reponse =="4":
                # Définition des différentes facettes à récupérer
                FACETS = [
                    'org',
                    'domain',
                    'port',
                    'asn',
                    
                    # Nous ne souhaitons afficher que les 3 premiers pays
                    # Si vous voulez voir plus de 5 résultats, vous pouvez utiliser ('country', 1000) pour voir les 1000 premiers pays, par exemple
                    ('country', 3),
                ]
                
                # Les titres pour chaque facette
                FACET_TITLES = {
                    'org': 'Top 5 Organisation',
                    'domain': 'Top 5 Domaines',
                    'port': 'Top 5 Ports',
                    'asn': 'Top 5 Systèmes autonomes',
                    'country': 'Top 3 Pays',
                }
                
                # Demande à l'utilisateur de saisir un nom pour la recherche
                print(colored("Exemple : apache, google ", "yellow"))
                requete = input("Saisir un nom : ")
                
                # Effectue la recherche avec les facettes
                resultat = api.count(requete, facets=FACETS)

                # Affiche les informations résumées de Shodan
                print('Informations résumées de Shodan')
                print('Requete : %s' % requete)
                print('Résultat total : %s\n' % resultat['total'])

                # Affiche les informations résumées pour chaque facette
                for facet in resultat['facets']:
                    print(FACET_TITLES[facet])

                    for term in resultat['facets'][facet]:
                        print('%s: %s' % (term['value'], term['count']))

                    # Affiche une ligne vide entre chaque information résumée
                    print('')

            elif reponse == "5":
                # Affiche un message de sortie si l'utilisateur choisit de quitter le programme
                print("Vous avez quittez le programme Shodan")
                break
            else : 
                # Si l'utilisateur entre un choix invalide, affiche un message d'erreur
                print("Entrer un nombre valide 1-2-3-4-5")
    main()

def programme_5():
    def main():
        while True:
            # Affiche le titre du programme
            print(" ")
            print(colored("Programme : WHOIS ", "blue"))
            print("------------------")

            # Affiche le menu
            print("""\nQue souhaitez vous faire:
            1] Recherche WHOIS
            2] Quitter le programme WHOIS\n""")
            
            # Demande à l'utilisateur de choisir une option
            reponse = input("Votre choix : ")
            print("Vous avez choisi : ", reponse)

            if reponse == "1":
                # Demande à l'utilisateur de saisir un nom de domaine
                domain = input("Saisir un domaine : ")

                # Utilise la bibliothèque Whois pour effectuer une recherche Whois sur le domaine donné
                result = whois.whois(domain)

                # Affiche les informations pour l'utilisateur
                print(f'Nom de domaine : {result.domain_name}')
                print(f'Registraire : {result.registrar}')
                print(f'Organisation : {result.org}')
                print(f'Adresse électronique du titulaire : {result.email}')
                print(f'Téléphone du titulaire : {result.phone}')
                print(f'Date de création: {result.creation_date}')
                print(f'Date expiration : {result.expiration_date}')
                print(f'Noms des serveurs: \n{result.name_servers}')
                print(f'Le statut :\n {result.status}\n')
            elif reponse == "2":
                # Si l'utilisateur a choisi l'option "Quitter", le programme se termine
                print("Vous avez quittez le programme WHOIS")
                break
            else : 
                # Si l'utilisateur a entré une option invalide, le programme affiche un message d'erreur
                print("Entrer un nombre valide 1-2")

    # Appelle la fonction main pour lancer le programme
    main()

 
# Fonction principal
def main():
    while True:
        print(" ")
        print(colored("Automatisation des actions RED TEAM ", "red"))
        print("-------------------------------------")

        print("Que souhaitez-vous faire : ")
        # Affiche le menu
        print("""\nQue souhaitez vous faire :
            1] Scan de vulnérabilité - NMAP
            2] Recherche OSINT sur un domaine stratégique - Google dorks
            3] Collecte du modèle MITRE ATTCK d’une menace
            4] Shodan
            5] Whois
            6] Quitter le programme \n""")
        reponse = input("Votre choix : ")

        if reponse =="1" :
            programme_1()   # Appel de la fonction du programme de scan de vulnérabilité - NMAP
        elif reponse =="2" :
            programme_2() # Appel la fonction du programme de recherche OSINT sur un domaine stratégique - Google dorks
        elif reponse =="3" :
            programme_3() # Appel la fonction du programme de collecte du modèle MITRE ATTCK d’une menace
        elif reponse =="4" :
            programme_4() # Appel la fonction du programme Shodan
        elif reponse =="5" :
            programme_5() # Appel la fonction du programme Whois
        elif reponse =="6":
            print("Fin du programme")
            sys.exit() # Sortir du programme
        else : 
            # Afficher un message d'erreur si le choix de l'utilisateur est invalide
            print("Entrer un nombre valide 1-2-3-4-5-6")      
main ()