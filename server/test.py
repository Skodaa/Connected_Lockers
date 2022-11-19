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

ADRESSE = ''
PORT = 50000
BUFFER_SIZE = 8192
SEPARATOR = ","

##
# Fonction créant le socket server
# @return : le socket server
def create_server() -> socket:
    # Création du socket
    serveur:socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(type(serveur))
    # Paramétrage du serveur 
    serveur.bind((ADRESSE, PORT))
    # Mise du serveur en écoute
    serveur.listen(5)
    print(f"[*] Listening at {ADRESSE}:{PORT}")
    return serveur

##
# Fonction connectant le socket serveur à la base de données
# @return : le tuple issue de la connexion 
def DB_connexion() -> tuple:
   conn = psycopg2.connect(database="volquardsen_lockers", user='volquardsen', password='BipBoop', host='postgresql-volquardsen.alwaysdata.net', port= '5432')
   cursor = conn.cursor()
   return (conn,cursor)

##
# Fonction affichant les données contenues dans un tableau
# @return : None
def affiche_donnees(donnees: list) -> None:
    print("[+] données recues : ",end='')
    print(donnees)

def user_type(cursor,utilisateur: str) -> bool:
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

    update: str = f"UPDATE casier SET occupe = FALSE, reserve = FALSE, heure_restant = NULL, heure_reservation = NULL, heure_fermeture = NULL, id_uti = NULL WHERE (id_casier LIKE '{locker}')"
    cursor.execute(update)
    connexion.commit()
    if(user_type(cursor,utilisateur) == "etudiant"):
        utilisation: str = f"SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        if(res[0] > 1):
            res[0] = res[0] - 1
            nb_utilisation: str = f"UPDATE etudiant SET utilisation_etudiant = {res[0]} WHERE (id_etudiant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
    else :
        utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        if(res[0] > 1):
            res[0] = res[0] - 1
            nb_utilisation: str = f"UPDATE enseignant SET utilisation_prof = {res[0]} WHERE (id_enseignant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
    print(f"[~] Fermeture du casier : {locker}")

##
# Fonction permettant de fermer un casier
# @param cursor
# @param connexion 
# @param locker : id du casier qui va être fermé
# @param utilisateur : id de l'utilisateur qui ferme le casier
# @return : None
def fermeture(cursor,connexion,locker:str,utilisateur:str) -> None:
    
    update: str = f"UPDATE casier SET occupe = TRUE, id_uti = '{utilisateur}' WHERE (id_casier LIKE '{locker}')"
    cursor.execute(update)
    connexion.commit()
    if(user_type(cursor,utilisateur) == "etudiant"):
        utilisation: str = f"SELECT utilisation_etudiant FROM etudiant WHERE (id_etudiant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        print(type(res[0]))
        if(res[0] < 1):
            ret:int = res[0] + 1
            nb_utilisation: str = f"UPDATE etudiant SET utilisation_etudiant = {ret} WHERE (id_etudiant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
            return "1,Casier fermé"
        else:
            return "0,Action impossible : nombre d'utilisation dépassé"
        
    else :
        utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{utilisateur}')"
        cursor.execute(utilisation)
        res = cursor.fetchone()
        if(res[0] < 3):
            ret:int = res[0] + 1
            nb_utilisation: str = f"UPDATE enseignant SET utilisation_prof = {ret} WHERE (id_enseignant LIKE '{utilisateur}')"
            cursor.execute(nb_utilisation)
            connexion.commit()
            return "1,Casier fermé"
        else:
            return "0,Action impossible : nombre d'utilisation dépassé"

##### Prendre en copte le département du casier
##
# Fonction permettant de reserver un casier s'il n'est pas utilisé ni déjà réservé
# @param cursor
# @param donnees : les donnees reçu par le serveur
def reservation(cursor,connexion,utilisateur: str,locker: str) -> None:

    is_free:str = f"SELECT id_casier FROM casier WHERE (id_casier LIKE '{locker}' AND occupe = FALSE AND reserve = FALSE);"
    cursor.execute(is_free)
    valid = cursor.fetchone()
    print(valid)
    if(valid == None):
        return "Impossible de réserver le casier."
    else:
        reserved: str = f"UPDATE casier SET reserve = TRUE WHERE (id_casier LIKE '{locker}')"
        cursor.execute(reserved)    
        connexion.commit()
        uti : str= f"UPDATE casier SET id_uti = '{utilisateur}' WHERE (id_casier LIKE '{locker}')"
        cursor.execute(uti)
        connexion.commit()
        print(f"[+] {locker} has been reserved")
        return "Casier réservé."

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
        if(res[0] > 1):
            return False
        else:
            return True
    else:
        enseignant_utilisation: str = f"SELECT utilisation_prof FROM enseignant WHERE (id_enseignant LIKE '{uti}')"
        cursor.execute(enseignant_utilisation)
        res = cursor.fetchone()
        if(res[0] > 3):
            return False
        else:
            return True

##### verifier si locker appartient a departement
##
# Fonction vérifiant si le locker est disponible
# @param locker : le casier a vérifier
# @return si le casier est disponible
def check_locker(cursor,locker:str,id_utilisateur:str,commande: str)->bool:

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
    print(f"[-] locker is free : {check_casier}")
    
    if(check_casier == True):

        # Verification de l'éligibilité de l'utilisateur à fermer un casier
        check_utilisateur:bool = check_uti(cursor,utilisateur)
        print(f"[-] utilisateur is free : {check_utilisateur}")

        if(check_utilisateur == True and commande == "close"):
            return fermeture(cursor,connexion,casier,utilisateur)

        elif(check_utilisateur == False and commande == "close"):
            return "0,L'utilisateur ne peut pas occuper un casier"

        elif(commande == "open"):
            ouverture(cursor,connexion,casier,utilisateur)
            return "1,Casier ouvert."

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
    check_uti:str = f"SELECT id_utilisateur FROM utilisateur WHERE (id_utilisateur LIKE '{utilisateur}')"
    cursor.execute(check_uti)
    res_utilisateur = cursor.fetchone()
    connexion.commit()
    # Si l'utilisateur est présent dans la base de données on continue les tests, sinon on renvoie le message d'erreur associé.
    if(res_utilisateur == None):
        return "0,Echec authentification : {utilisateur} inconnu"
    else:
        # Vérification id_carte présent dans la base de données
        check_carte:str = f"SELECT id_carte FROM carte WHERE (id_carte LIKE '{carte}')"
        cursor.execute(check_carte)
        res_carte = cursor.fetchone()
        connexion.commit()
        # Si la carte est présente dans la base de données on continue les tests, sinon on renvoie le message d'erreur associé.
        if(res_carte == None):
            return "0,Echec authentification : {carte} inconnue"
        else:
            # Vérification de l'association de la carte avec l'utilisateur
            check_association: str = f"SELECT u.id_utilisateur FROM utilisateur AS u JOIN carte AS c ON c.id_utilisateur LIKE u.id_utilisateur"
            cursor.execute(check_association)
            res_association = cursor.fetchone()
            connexion.commit()
            # Si la carte n'est pas associée à l'utilisateur on renvoi le message d'erreur associé, sinon on renvoie le message d'authentification réussi
            if(res_association == None):
                return "0,Echec authentification : la carte {carte} n'est pas associé à l'utilisateur {utilisateur}"
            else:
                return "1,Authentificcation réussie"

##
# Fonction qui récupère les données envoyées par le client tant que la connexion n'est pas fermée et décide de l'action à réaliser en fonction des données recues.
# @param cursor
# @param connexion
# @param client : socket du client
# @return : None
def handle_client(cursor,connexion,client: socket) ->None:
    client_actif = True
    while client_actif:
        donnees = client.recv(BUFFER_SIZE).decode().split(SEPARATOR)
        affiche_donnees(donnees)

        # Cas d'arrêt de connexion au serveur : si aucunes données est recues ou si close_connection est recue
        if not donnees:
            reponse = "Arrêt du serveur : aucunes données recues"
            reponse = str.encode(reponse)
            client.send(reponse + "\n")
            close_client(client)
            print("[-] Arrêt du serveur : aucunes données recues")
        elif "close_connection" in donnees[0]:
            reponse = "Arrêt du serveur : échanges terminés"
            reponse = str.encode(reponse)
            client.send(reponse + "\n")
            close_client(client)
            print("[-] Arrêt du serveur : échanges terminés")
        # determination de l'action à réaliser
        else:
            reponse:str
            nb_donnees = len(donnees)
            match nb_donnees:
                # Cas où on souhaite authentifier un utilisateur
                case 2:
                    carte = donnees[1]
                    reponse = authentification(cursor,connexion,donnees[0],carte[:8])
                    print(f"[-] Envoi de la réponse : " + reponse)
                    reponse = str.encode(reponse + "\n")
                    try :
                        client.send(reponse)
                    except:
                        client_actif = False
                        close_client(client)
                        print("[-] Arrêt forcé du serveur")
                # Cas où au vu du nombre d'aguments, l'action est d'ouvrir ou fermer un casier
                case 3 :
                    # Cas où l'action à réaliser est d'ouvrir un casier
                    if "open" in donnees[2]:
                        donnees[2] = "open"
                        reponse: str = selection(cursor,connexion,donnees[0],donnees[1],donnees[2])
                        print(f"[-] Envoi de la réponse : {reponse}")
                        reponse = str.encode(reponse + "\n") 
                        try :
                            client.send(reponse)
                        except:
                            client_actif = False
                            close_client(client)
                            print("[-] Arrêt forcé du serveur")
                    # Cas où l'action à réaliser est de fermer un casier
                    elif "close" in donnees[2]:
                        donnees[2] = "close"
                        reponse: str = selection(cursor,connexion,donnees[0],donnees[1],donnees[2])
                        print(f"[-] Envoi de la réponse : {reponse}")
                        reponse = str.encode(reponse + "\n")
                        try :
                            client.send(reponse)
                        except:
                            client_actif = False
                            close_client(client)
                            print("[-] Arrêt forcé du serveur")
                    elif "reservation" in donnees[2]:
                        reponse: str = reservation(cursor,connexion,donnees[0],donnees[1])
                        print(f"[-] Envoi de la réponse : {reponse}")
                        reponse = str.encode(reponse + "\n")
                        try:
                            client.send(reponse)
                        except:
                            client_actif = False
                            close_client(client)
                            print("[-] Arrêt forcé du serveur")
                    else:
                        reponse = "Veuillez réessayer"
                        print(f"[-] Envoi de la réponse : {reponse}")
                        reponse = str.encode(reponse + "\n")
                        try:
                            client.send(reponse)
                        except:
                            client_actif = False
                            close_client(client)
                            print("[-] Arrêt forcé du serveur")

##
# Fonction qui déconnecte un client.
# @param client : socket du client à déconnecter
# @return : None
def close_client(client: socket) ->None:
    client.close()
    print("[-] Client deconnected.")

##
# Fonction qui arrête le serveur.
# @param client : socket du serveur à arrêter
# @return : None
def close_server(serveur: socket) -> None:
    serveur.close()
    print("[-] Server stops.")

serveur: socket = create_server()
connexion,cursor = DB_connexion()

# Maintient de la connexion avec le client par un thread
while True:
    client, adresseClient = serveur.accept()
    print(f"[+] {adresseClient} is connected.")
    
    threading.Thread(target=handle_client(cursor,connexion,client),args=(client, adresseClient)).start()