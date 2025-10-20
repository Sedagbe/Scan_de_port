import socket
from datetime import datetime

# ---------------------------
# 1️- Introduction
# ---------------------------
print("=== Scanner de ports ===")
target = input("Entrez une adresse IP ou un nom de domaine à scanner : ")

# Convertit le nom de domaine en adresse IP
target_ip = socket.gethostbyname(target)

print(f"\n[+] Cible : {target_ip}")
print("[+] Début du scan à :", datetime.now())
print("-" * 50)

# ---------------------------
# 2️ - Boucle de scan
# ---------------------------
# On va scanner les ports de 1 à 100 
for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)  # délai d’attente
    result = sock.connect_ex((target_ip, port))  # 0 = ouvert
    if result == 0:
        print(f"[OUVERT] Port {port}")
    sock.close()

print("-" * 50)
print("[+] Scan terminé à :", datetime.now())

#entrez scanme.nmap.org dans la console pour tester le script.
#(C’est un serveur de test autorisé pour l’apprentissage.)
