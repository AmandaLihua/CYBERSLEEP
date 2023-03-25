# CYBERSLEEP
PROJET D'ETUDES - SDV 

<p align="center">
  <img src="https://user-images.githubusercontent.com/60131013/227723653-cee18b3e-319b-4831-9edc-a21a5fb5e014.png" />
</p>

Vous faites partie d’un SOC en tant qu’Analyste redteam, votre Manager vous demande de réaliser l’automatisation d’action que vous réalisez tous les jours afin de vous faire gagner du temps sur vos tâches journalières.
Un analyste Red Team est chargé de simuler les tactiques, les techniques et les procédures (TTP) d'un attaquant potentiel pour évaluer la sécurité d'un système ou d'un réseau. Les actions typiques d'un analyste Red Team peuvent inclure :
- Effectuer une reconnaissance du système cible, en recherchant des informations sur les réseaux, les systèmes et les utilisateurs.

- Identifier les vulnérabilités potentielles dans le système cible en utilisant des outils automatisés et manuels.

- Élaborer une stratégie d'attaque pour exploiter les vulnérabilités détectées et obtenir un accès non autorisé au système cible.
- Effectuer des tests d'intrusion pour tester la sécurité du système cible en utilisant des techniques d'ingénierie sociale, des attaques de phishing, des exploits de  vulnérabilités et d'autres méthodes d'attaque.
- Élaborer des rapports détaillés sur les résultats des tests d'intrusion, y compris les vulnérabilités prouvées, les méthodes d'attaque utilisées et les recommandations pour améliorer la sécurité du système.
- Travailler en étroite collaboration avec les équipes de sécurité informatique pour identifier les faiblesses du système et proposer des solutions pour renforcer la sécurité.
- Fournir des conseils aux équipes de sécurité informatique sur les TTP utilisés par les cybercriminels et les moyens de les prévenir ou de les détecter.
- Participer aux exercices de simulation d'attaque pour aider les organisations à se préparer à des cyberattaques potentielles.
- Effectuer des recherches sur les nouvelles menaces et les vulnérabilités afin de rester informé des dernières tendances en matière de sécurité informatique.


*Les outils et techniques utilisé dans ce rapport sont effectué dans le cadre scolaire, nous ne promouvons, n'encourageons, ne soutenons ou n'incitons aucune activité illégale.*

## Installation
Il vous faudra utiliser "git clone".
<pre><code>git clone https://github.com/AmandaLihua/CYBERSLEEP</code></pre>
Puis
<pre><code>cd CYBERSLEEP </code></pre>

Exemple :
![image](https://user-images.githubusercontent.com/60131013/227726066-a9a2a001-2462-4522-9ee5-e25f32a5b6eb.png)



## Prérequis 
Il faut avoir Python d'installé sur votre poste ou votre VM.
Vous devez lancer le script "requirement.py" avant de lancer le programme principal.
**Il faut etre en mode "root" pour lancer le script "requirement.py"**

## Le programme - Automatisation des actions RED TEAM

![Screenshot_1](https://user-images.githubusercontent.com/60131013/227724419-9178dc06-69f5-4aac-8343-0a1397a9a396.png)

Le programme est constitué des 6 options :
1. Scan de vulnérabilité - NMAP

![Screenshot_2](https://user-images.githubusercontent.com/60131013/227724651-665fb5d6-f978-4ba6-a645-cb9be5277905.png)

Un scan de vulnérabilité est une technique d'analyse utilisée pour identifier les vulnérabilités potentielles d'un système, d'un réseau ou d'une application. Il consiste à examiner les composants du système, tels que les logiciels, les ports, les services et les protocoles, afin de déterminer s'ils présentent des vulnérabilités qui pourraient être exploitées par des attaquants.

Voici un exemple d'exécution : 

![image](https://user-images.githubusercontent.com/60131013/227728385-171c4abb-9455-44b1-8aee-423cc85455b8.png)

Résultat :

![image](https://user-images.githubusercontent.com/60131013/227728476-cb72c7ff-d849-4272-bd73-95ec64b8af23.png)


2. Recherche OSINT sur un domaine stratégique - Google dorks

![image](https://user-images.githubusercontent.com/60131013/227724707-3df07dea-c522-4267-a278-9f8efcc4654e.png)

Une recherche OSINT (Open-Source Intelligence) sur un domaine stratégique est une enquête qui utilise des sources d'informations ouvertes pour collecter des données sur une organisation, une entreprise ou un domaine particulier, dans le but d'obtenir des informations exploitables.

Les Google dorks sont des requêtes de recherche avancées qui permettent d'effectuer des recherches très ciblées sur Google. Ils peuvent être utilisés pour trouver des informations spécifiques sur des sites Web ou des domaines, tels que des fichiers PDF, des informations de contact, des pages de connexion, des répertoires, etc. Les dorks sont généralement utilisés pour trouver des failles de sécurité ou des informations sensibles qui peuvent être utilisées pour compromettre la sécurité d'un domaine ou d'une entreprise.

Voici un exemple d'exécution : 

![image](https://user-images.githubusercontent.com/60131013/227729090-313edf33-2166-4b88-96e9-dbc7ad496844.png)

Résultat :

![image](https://user-images.githubusercontent.com/60131013/227729119-a30f556a-93fb-4c12-a383-ede580f91044.png)

3. Collecte du modèle MITRE ATTCK d’une menace

![image](https://user-images.githubusercontent.com/60131013/227724723-2d4e2f78-f5f5-4aaa-8d40-059915ca9e7d.png)

La collecte du modèle MITRE ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) d'une menace est un processus qui vise à identifier les tactiques, techniques et procédures (TTP) utilisées par les attaquants pour mener une attaque sur un système ou une organisation. 

Voici un exemple d'exécution : 

![image](https://user-images.githubusercontent.com/60131013/227729161-204c389d-08d1-4edb-9c58-3ffb3b3078d3.png)

Résultat :

![image](https://user-images.githubusercontent.com/60131013/227729200-560b1f12-b7e1-4085-b842-bec3a97954e3.png)

4. Shodan

![image](https://user-images.githubusercontent.com/60131013/227724744-135909e9-773f-49cd-9548-22aee989f42a.png)

Shodan est un moteur de recherche spécialisé dans la recherche de dispositifs connectés à Internet. Contrairement aux moteurs de recherche traditionnels, qui indexent principalement des sites Web, Shodan analyse et indexe les dispositifs connectés à Internet, tels que les serveurs, les routeurs, les caméras IP, les objets connectés, les appareils domestiques intelligent.

Voici un exemple d'exécution : 

![image](https://user-images.githubusercontent.com/60131013/227729398-47746774-34e7-4742-a707-f2bbc19e8f22.png)

Résultat :

![image](https://user-images.githubusercontent.com/60131013/227729374-710dddd3-97b9-4f1f-bfcb-4c71f0847fea.png)

5. Whois

![image](https://user-images.githubusercontent.com/60131013/227724770-4c8c717a-f12f-4864-a892-3c5b375e75c7.png)

WHOIS est un protocole qui permet d'interroger une base de données publique pour obtenir des informations sur un nom de domaine, telles que le nom et les coordonnées du propriétaire, la date de création, les serveurs de noms et les dates d'expiration

Voici un exemple d'exécution : 

![image](https://user-images.githubusercontent.com/60131013/227729456-6f0f80be-7a69-497d-9fd2-ed3b80c67d6a.png)

Résultat :

![image](https://user-images.githubusercontent.com/60131013/227729469-e9599d5b-a554-41ed-93bb-0be101494689.png)

6. Quitter le programme

![image](https://user-images.githubusercontent.com/60131013/227729500-cc2d62bc-ed25-4a3d-a661-e65101a49c4a.png)


## Bibliographie
https://docs.python.org/3/reference/import.html 
https://danielmiessler.com/blog/nmap-use-the-top-ports-option-for-both-tcp-and-udp-simultaneously/  
https://www.securiteinfo.com/attaques/hacking/google-dorks-et-google-hacking.shtml 
https://python.doctor/page-beautifulsoup-html-parser-python-library-xml 
https://shodan.readthedocs.io/en/latest/tutorial.html  
https://pypi.org/project/python-whois/

