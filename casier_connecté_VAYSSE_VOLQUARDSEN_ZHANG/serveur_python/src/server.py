"""!
Code serveur réseau réalisé en python, nous y retrouverons toutes les fonctions permettant d'écouter de communiquer avec le client ainsi que la base de données.

@author VOLQUARDSEN Alex VAYSSE Matthieu
@version 1.0.5
@since 31/10/2022

Format des message normalement reçu par le serveur :

verification éligibilité pour ouvrir ou fermer un casier : [id_utilisateur],[id_casier],[id_carte]
reservation d'un casier : [id_utilisateur],[id_casier] -> si le casier est déjà réserver, ou qu'il est occupé, ou que l'utilisateur ne peut pas réserver de casier, alors retourne une erreur
fermeture d'un casier : [id_utilisateur],[id_casier],[commande(ici fermeture)] -> si l'utilisateur peut occuper le casier et que le casier est libre alors il se ferme et est attribuer à l'utilisateur
ouverture d'un casier : [id_utilisateur],[id_casier],[commande(ici ouverture)] -> si l'utilisateur utilise bien se casier actuellement, alors il s'ouvre sinon erreur 

"""

import socket
import psycopg2
import threading
from datetime import datetime
import log_configuration as l
import time

ADRESSE = ''
port = 50001
BUFFER_SIZE = 8192
SEPARATOR = ","
HEURE_MAX = 18

DEFAULT_TIMEOUT = 60;


##
# Fonction créant le socket server
# @return : le socket server
def create_server() -> socket:
    global port
    # Création du socket
    serveur:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        connect = False
        # Paramétrage du serveur 
        while(connect == False):
            try: # on essaye de connecter le serveur au port et à l'adresse
                serveur.bind((ADRESSE, int(port))) 
                connect = True
            except socket.error: # si un probleme de connection est rencontré, on demande un nouveau port à écouter
                print(f" Port : {port} already used please select a new one GAY :")
                port = input("New port : ")
                
        l.logging.info(f"Server running on port : {port}")
        # Mise du serveur en écoute
        serveur.listen(10)
        l.logging.info("Serveur binded for maximum 10 clients at the same time")
        print(f"[*] Listening at {ADRESSE}:{port}")
        l.logging.info(f"Server listening at {ADRESSE}")
        
    except : # si on arrive vraiment pas à se connecter on envoie une erreur
        l.logging.error("Error occured while binding the server")
    return serveur
        


    

##
# Fonction connectant le socket serveur à la base de données
# @return : le tuple issue de la connexion 
def DB_connexion(db_name: str, user_name: str, pwd: str, host_link: str, port_number: str) -> tuple:
   conn = psycopg2.connect(database = db_name, user = user_name, password = pwd, host = host_link, port = port_number)
   l.logging.info(f"Serveur connected to database : {db_name} on port {port_number}")
   cursor = conn.cursor()
   return (conn,cursor)

##
# Fonction affichant les données contenues dans un tableau
# @return : None
def affiche_donnees(donnees: list,addresseClient) -> None:
    l.logging.debug(f"Data received : {donnees} from {addresseClient}")
    print("[+] données recues : ",end='')
    print(donnees)


##
# Fonction retournant le type d'utilisateur, s'il s'agit d'un etudiant ou d'un enseignant 
# @param utilisateur : l'id de l'utilisateur dont on veut le type
# @return le type de l'utilisateur
def user_type(cursor,utilisateur: str) -> str:
    type_utilisateur:str = f"SELECT id_etudiant FROM etudiant WHERE (id_etudiant LIKE '{utilisateur}')"
    cursor.execute(type_utilisateur)
    res = cursor.fetchone()
    if(res != None) :
        return "etudiant"
    else:
        return "enseignant"

##### Check le département utilisateur 
##### Check utilisation en cours
##
# Fonction permettant d'ouvrir un casier
# @param cursor : 
# @param connexion :
# @param locker : id du casier qui va être ouvert
# @param utilisateur : id de l'utilisateur qui ouvre le casier
# @return : None
def ouverture(cursor,connexion,locker:str,utilisateur)->None:

    update: str = f"UPDATE casier SET occupe = FALSE, reserve = FALSE, heure_reservation = NULL, heure_butoire = NULL, id_uti = NULL WHERE (id_casier LIKE '{locker}')"
    cursor.execute(update)
    connexion.commit()
    # on vérifie si l'utilisateur est un étudiant ou non
    if(user_type(cursor,utilisateur) == "etudiant"):
        # si c'est le cas, on vérifie sont nombre d'utilisation en cours
        utilisation: str = f"SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        res = res[0]
        # si l'utilisateur a déjà une utilisation, on decremente ce compteur 
        if(res == 1):
            res = res - 1
            nb_utilisation: str = f"UPDATE etudiant SET utilisation_etudiant = {res} WHERE (id_etudiant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
    # si l'utilisateur est un enseignant
    else :
        utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        # s'il a des utilisation, on lui enleve une utilisation en ouvrant le casier
        if(res[0] <= 3 and res[0] > 0):
            res = res[0]
            res = res - 1
            nb_utilisation: str = f"UPDATE enseignant SET utilisation_prof = {res} WHERE (id_enseignant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
    print(f"[~] Ouverture du casier : {locker}")
        
##
# Fonction donnant l'heure butoire pour ouvrir le casier 
# @param current_time : l'heure de fermeture du casier
# @return l'heure butoire d'ouverture avant pénalité
def reservation_time(current_time: str) -> tuple:
    time_max = HEURE_MAX - int(current_time[0:2])
    time_max = time_max + int(current_time[0:2])
    reservation_time = str(time_max) + current_time[2:]
    return reservation_time

##
# Fonction permettant de fermer un casier
# @param cursor
# @param connexion 
# @param locker : id du casier qui va être fermé
# @param utilisateur : id de l'utilisateur qui ferme le casier
# @return : None
def fermeture(cursor,connexion,locker:str,utilisateur:str) -> int:
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    remaining_time = reservation_time(current_time) # on récupere l'heure butoire

    update: str = f"UPDATE casier set occupe = TRUE, heure_reservation = '{current_time}', heure_butoire = '{remaining_time}', id_uti = '{utilisateur}' WHERE (id_casier LIKE '{locker}')"
    cursor.execute(update)
    connexion.commit()
    # si l'utilisateur est un étudiant 
    if(user_type(cursor,utilisateur) == "etudiant"):
        utilisation: str = f"SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        res = res[0]
        if(res < 1): # si le nombre d'utilisation est zero on ajoute une utilisation
            res = res + 1
            nb_utilisation: str = f"UPDATE etudiant SET utilisation_etudiant = {res} WHERE (id_etudiant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
            print(f"[~] Fermeture du casier : {locker}")
            return 1
        else: # sinon on empeche la fermeture
            print("[-] Fermeture impossible")
            return 0
    # si l'utilisateur est un enseignant 
    else :
        utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        if(res[0] < 3): # on ajoute une utilisation s'il n'en as pas déjà 3
            res = res[0]
            res = res + 1
            nb_utilisation: str = f"UPDATE enseignant SET utilisation_prof = {res} WHERE (id_enseignant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
            print(f"[~] Fermeture du casier : {locker}")
            return 1
        else: # sinon on empeche la fermeture
            print("[-] Fermeture impossible")
            return 0

##
# Fonction permettant de séparer les différents éléments envoyés
# @param donnees : les données a splitter
# @return une liste des éléments
def change(donnees:str)->str:
    
    donnees = donnees[0] + donnees[1]
    affiche_donnees(donnees)
    return donnees


##
# Fonction vérifiant si l'utilisateur peut occupé un casier
# @param uti : l'utilisateur que l'on vérifie
# @return si oui ou non l'utilisateur peut occupé le casier
def check_uti(cursor,uti: str)->bool:

    type_utilisateur:str = user_type(cursor,uti)
    if(type_utilisateur == "etudiant"):
        etudiant_utilisation: str = f"SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant LIKE '{uti}')"
        cursor.execute(etudiant_utilisation)
        res = cursor.fetchone()
        res = res[0]
        if(res >= 1): # on vérifie si le nombre d'utilisation, s'il en as une on retourne faux sinon vrai
            return False
        else:
            return True
    else:
        # si l'utilisateur est un enseignant et qu'il n'as pas dépasser le nombre maximum d'utilisation, on retourne vrai
        enseignant_utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{uti}')"
        cursor.execute(enseignant_utilisation)
        res = cursor.fetchone()
        res = res[0]
        if(res >= 3):
            return False
        else:
            return True

##
# Fonction vérifiant si l'utilisateur est en cours ou non
# @param uti : l'id de l'utilisateur
# @return si oui ou non il est en cours
def course(cursor,uti: str) -> bool:
    type_utilisateur: str = user_type(cursor,uti)
    if type_utilisateur == "etudiant":
        a_cours_verification: str = f"SELECT id_cours FROM est_en_cours WHERE (id_uti = '{uti}')"
        cursor.execute(a_cours_verification)
        res = cursor.fetchone()
        res = res[0]
        if(res != None): # si l'utilisateur est en cours 
            temps_cours = f"SELECT debut FROM periode_cours WHERE (id_cours = '{res}')"
            cursor.execute(temps_cours)
            rep = cursor.fetchone()
            rep = rep[0]
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            rep = str(rep)
            time: int = int(rep[0:2]) - int(current_time[0:2])
            # on vérifie que l'utilisateur à cours dans un certains delais de temps 
            if(time >= -2 and time <= 2):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

##
# Fonction vérifiant que l'utilisateur est du même département que le casier
# @param l'id de l'utilisateur
# @param l'id du casier 
# @return si le casier et l'utilisateur sont du même département
def check_departement(cursor, utilisateur: str, casier: str) -> bool :
    verification_locker: str = f"SELECT id_dep FROM casier WHERE (id_casier LIKE '{casier}')"
    cursor.execute(verification_locker)
    res_locker = cursor.fetchone()
    res_locker = res_locker[0]
    verification_user: str = f"SELECT departement FROM utilisateur WHERE (id_uti LIKE '{utilisateur}')"
    cursor.execute(verification_user)
    res_user = cursor.fetchone()
    res_user = res_user[0]
    if(res_locker == res_user):
        return True
    else:
        return False

##### verifier si locker appartient a departement
##
# Fonction vérifiant si le locker est disponible
# @param locker : le casier a vérifier
# @return si le casier est disponible
def check_locker(cursor,locker:str,id_utilisateur:str,commande: str) -> bool:

    reserved: str = f"SELECT id_uti FROM casier WHERE (id_casier LIKE '{locker}' AND reserve = TRUE)"
    cursor.execute(reserved)
    id_reserved = cursor.fetchone()
    occupe: str = f"SELECT id_uti FROM casier WHERE (id_casier LIKE '{locker}' AND occupe = TRUE)"
    cursor.execute(occupe)
    id_occupied = cursor.fetchone()
    exist: str = f"SELECT id_casier FROM casier WHERE(id_casier LIKE '{locker}')"
    cursor.execute(exist)
    does_exist = cursor.fetchone()

    # Cas où le casier est réservé par un utilisateur
    if(id_reserved != None):
        reserved = f"{id_reserved}"
        reserved = reserved[2:-3]
        # Verification si l'id utilisateur est le même id inscrit dans le casier réservé
        if(reserved == id_utilisateur):
            return True
        else:
            return False
    # Cas où le casier est occupé par un utilisateur
    elif(id_occupied != None):
        if(commande == "open"):
            occupied = f"{id_occupied}"
            occupied = occupied[2:-3]
            # Verification si l'id utilisateur est le même id inscrit dans le casier occupé
            if(occupied == id_utilisateur):
                return True
        else:
            return False
    else:
        # Cas où le casier n'est pas occupé ni réservé alors, le casier peut être ouvert
        if(does_exist != None):
            return True
        # Cas où le casier demandé n'existe pas
        else:
            return False

##
# Fonction décidant de l'action à effectuer
# @param cursor 
# @param donnees : les données décidant de l'action
def selection(cursor,connexion,utilisateur: str, casier: str, commande: str) ->str:

    check_casier:bool = check_locker(cursor,casier,utilisateur,commande)
    print(f"[~] locker is free : {check_casier}")
    
    if(check_casier == True):

        # Verification de l'éligibilité de l'utilisateur à fermer un casier
        check_utilisateur:bool = check_uti(cursor,utilisateur)
        print(f"[~] utilisateur is free : {check_utilisateur}")
        # si l'utilisateur est éligible et que la fonction est "close" on ferme le casier
        if(check_utilisateur == True and commande == "close"):
            if(course(cursor,utilisateur) and check_departement(cursor,utilisateur,casier)):
                fermeture(cursor,connexion,casier,utilisateur)
                return f"1,Casier {casier} fermé."
            else:
                return f"0,L'utilisateur n'as pas cours dans les prochaines heures"
        # sinon on affiche une erreur
        elif(check_utilisateur == False and commande == "close"):
            return "0,L'utilisateur ne peut pas occuper un casier de plus"
        # si la commande est "open" on ouvre le casier
        elif(commande == "open"):
            ouverture(cursor,connexion,casier,utilisateur)
            return f"1,Casier {casier} ouvert."
        # sinon la commande est inconnue
        else:
            return "0,Erreur imprévue"
    else:

        if(commande != "open" and commande != "close"):
            return "0,Erreur commande"
            
        else :
            return "0,Action impossible"

##
# Fonction permettant d'authentifier un utilisateur à l'aide de son id ainsi que l'id de sa carte.
# @param cursor
# @param connexion 
# @param utilisateur : id de l'utilisateur
# @param carte : id de la carte de l'utilisateur
# @return : la chaine de caractère contenant la réponse (si 0,"message" alors l'authentification n'as pas aboutie sinon 1,"message")
def authentification(cursor,connexion,utilisateur:str,carte:str) ->str:
    # Vérification id_utilisateur présent dans la base de données
    check_uti:str = f"SELECT id_uti FROM utilisateur WHERE (id_uti LIKE '{utilisateur}')"
    cursor.execute(check_uti)
    res_utilisateur = cursor.fetchone()
    connexion.commit()
    # Si l'utilisateur est présent dans la base de données on continue les tests, sinon on renvoie le message d'erreur associé.
    if(res_utilisateur == None):
        return f"0,Echec authentification : {utilisateur} inconnu"
    else:
        # Vérification id_carte présent dans la base de données
        check_carte:str = f"SELECT id_carte FROM carte WHERE (id_carte LIKE '{carte}')"
        cursor.execute(check_carte)
        res_carte = cursor.fetchone()
        connexion.commit()
        # Si la carte est présente dans la base de données on continue les tests, sinon on renvoie le message d'erreur associé.
        if(res_carte == None):
            return f"0,Echec authentification : {carte} inconnue"
        else:
            # Vérification de l'association de la carte avec l'utilisateur
            check_association: str = f"SELECT id_carte FROM utilisateur WHERE (id_uti LIKE '{utilisateur}')"
            cursor.execute(check_association)
            res_association = cursor.fetchone()
            res = res_association[0]
            connexion.commit()
            # Si la carte n'est pas associée à l'utilisateur on renvoi le message d'erreur associé, sinon on renvoie le message d'authentification réussi
            if(res != carte):
                return f"0,Echec authentification : la carte {carte} n'est pas associé à l'utilisateur {utilisateur}"
            else:
                return "1,Authentification réussie"


##
# Fonction qui récupère les données envoyées par le client tant que la connexion n'est pas fermée et décide de l'action à réaliser en fonction des données recues.
# @param cursor
# @param connexion
# @param client : socket du client
# @return : None
def handle_client(cursor,connexion,client: socket,adresseClient) ->None:
    client_actif = True
    authentified = False
    utilisateur: str = ""

    while (client_actif):
        # le client est timeout après un certains temps
        client.settimeout(DEFAULT_TIMEOUT)
        try:
            # on récupere la donnée envoyer par le client
            donnees = client.recv(BUFFER_SIZE).decode().split(SEPARATOR)
            # on l'affiche avant de tenté quelque éxecution que se soit
            affiche_donnees(donnees,adresseClient)

            # Cas d'arrêt de connexion au serveur : si close_connection est recue
            if "close_connection" in donnees[0]:
                reponse = "2,Echanges terminés"
                reponse = str.encode(reponse + "\n")
                client.send(reponse)
                client_actif = False
                close_client(client,adresseClient)
            # determination de l'action à réaliser
            else:
                reponse:str
                nb_donnees = len(donnees)
                if nb_donnees == 2:
                    if "open" in donnees[1]:
                        # si la commande est open et que l'utilisateur est authentifié on traite la demande
                        if ("open" in donnees[1]) and (authentified == True):
                            donnees[1] = "open"
                            reponse: str = selection(cursor,connexion,utilisateur,donnees[0],donnees[1])
                            print(f"[-] Envoi de la réponse : {reponse}")
                            reponse = str.encode(reponse + "\n") 
                            try :
                                client.send(reponse)
                            except:
                                client_actif = False
                                close_client(client,adresseClient)
                        # sinon on retourne une erreur au client
                        else: 
                            reponse: str = "0,Action impossible"
                            reponse = str.encode(reponse + "\n")
                            try :
                                client.send(reponse)
                            except:
                                client_actif = False
                                close_client(client,adresseClient)
                    
                    elif "close" in donnees[1]:
                        # si la commande est close et que l'utilisateur est authentifié on effectue la commande
                        if ("close" in donnees[1]) and (authentified == True):
                            donnees[1] = "close"
                            reponse: str = selection(cursor,connexion,utilisateur,donnees[0],donnees[1])
                            print(f"[-] Envoi de la réponse : {reponse}")
                            reponse = str.encode(reponse + "\n")
                            try :
                                client.send(reponse)
                            except:
                                client_actif = False
                                close_client(client,adresseClient)
                        # sinon on retourne une erreur au client
                        else:
                            reponse: str = "0,Action impossible"
                            reponse = str.encode(reponse + "\n")
                            try :
                                client.send(reponse)
                            except:
                                client_actif = False
                                close_client(client,adresseClient)
                    # si aucune commande n'est trouver, on essaye d'identifié l'utilisateur avec les données reçu
                    else:
                        carte = donnees[1]
                        reponse = authentification(cursor,connexion,donnees[0],carte[:8])
                        check = reponse.split(",")
                        if(check[0] == "1"):
                            utilisateur = str(donnees[0])
                            authentified = True
                        print(f"[-] Envoi de la réponse : " + reponse)
                        reponse = str.encode(reponse + "\n")
                        try :
                            client.send(reponse)
                        except:
                            client_actif = False
                            close_client(client,adresseClient)
        # Si une erreur de connexion est trouver, on ferme la connexion
        except:
            print("[-] Client issue : unexpetedly closed")
            connected = client.getsockname()
            # si le client est encore connecté, on le ferme normalement
            if(connected == adresseClient ):
                reponse = "2,Echanges terminés"
                reponse = str.encode(reponse + "\n")
                client.send(reponse)
                close_client(client,adresseClient)
                l.logging.warning("Client error : too long to respond Client closed")
            #sinon on libere juste la place pour le prochain client
            else:
                client_actif = False
                client.close()
                l.logging.warning("Client error : unexpected disconnect")
                break    
           

##
# @function send_response : envoi une réponse à un client
# @param client : socket sur lequel envoyer le message
# @param addresseClient : utiliser pour le fichier log
# @param response: chaine de caractère à envoyer au client
# @return : None
def send_response(client: socket, addresseClient, response: str) -> None :
    client.send(response)
    l.logging.info(f"Envoi au client {addresseClient}, la réponse : {response}")

##
# Fonction qui déconnecte un client.
# @param client : socket du client à déconnecter
# @param addresseClient : utiliser pour le ficher log
# @return : None
def close_client(client: socket,addresseClient) ->None:
    client.close()
    l.logging.info(f"Client disconnected with address : {addresseClient}")
    print("[-] Client deconnected.")

##
# Fonction qui arrête le serveur.
# @param client : socket du serveur à arrêter
# @return : None
def close_server(serveur: socket) -> None:
    serveur.close()
    l.logging.info("Server shutting down")
    print("[-] Server stops.")


serveur: socket = create_server()
connexion,cursor = DB_connexion("volquardsen_lockers","volquardsen","BipBoop","postgresql-volquardsen.alwaysdata.net","5432")
res = 1

# Maintient de la connexion avec le client par un thread
while res == 1:
        client, adresseClient = serveur.accept()
        print(f"[+] {adresseClient} is connected.")
        l.logging.debug(f"New client connected with address : {adresseClient}")
    
        threading.Thread(target=handle_client(cursor,connexion,client,adresseClient),args=(client, adresseClient)).start()
