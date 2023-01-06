package client;

import java.io.BufferedReader; 
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetSocketAddress;
import java.net.Socket;
import java.net.SocketAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

import org.apache.log4j.ConsoleAppender;
import org.apache.log4j.Level;
import org.apache.log4j.Logger;
import org.apache.log4j.PatternLayout;


/**
 * Cette classe contient le Client et les m�thodes qui lui sont associ� dans le but de pouvoir se connecter � un serveur et de lui envoyer des informations
 * 
 * @author VOLQUARDSEN, VAYSSE, ZHANG
 * @version 2.0.5
 */
public class Client {
	
	private String ip;
	private int port;
	
	/**
	 * Constructeur du client, si les parametres donn�s dont null alors ils sont initialis� avec une valeur par d�faut
	 * @param ip : l'ip de connexion du client
	 * @param port : le port de connexion du client
	 */
	public Client(String ip, int port)
	{
		if(ip == null)
		{
			this.ip = "127.0.0.1";
		}
		else
		{
			this.ip = ip; 
		}
		if(port == 0)
		{
			this.port = 50000;
		}
		else 
		{
			this.port = port;
		}
		
	}
	
	public String getIp() {
		return ip;
	}


	public void setIp(String ip) {
		this.ip = ip;
	}


	public int getPort() {
		return port;
	}


	public void setPort(int port) {
		this.port = port;
	}
	
	/**
	 * Fonction v�rifiant si un message est conforme et peut �tre envoy�.
	 * @param msg : le message � v�rifier
	 * @return un bool�en indiquant si le message peut �tre envoy�
	 */
	public static boolean check_msg(String msg)
	{
		// "," est pour nous un s�parateur entres les arguments, s'il ne le contient pas il y as de grandes chances que le message soit incorrecte.
		if(msg.contains(","))
		{
			// Nos cartes d'�tudiants commence toutes par 22 donc si on ne le trouve pas on v�rifie les autres possibilit�s
			if(msg.contains("22"))
			{
				// Pour les messages d'authentification, la longueur est toujours de 17 caractere et donc si ce n'est pas le cas, le message est incorrecte.
				if(msg.length() == 17)
				{
					return true;
				}
				else
				{
					return false;
				}
			}
			// Si le message ne contient pas le marqueur de carte, on v�rifie s'il s'agit d'une requete de modification d'�tat d'un casier
			else if(msg.contains("locker"))
			{
				// Si c'est le cas, on v�rifie que la requ�te est bien l'une de c'elle qui est possible
				if(msg.contains("open") || msg.contains("close"))
				{
					// Si la requete est trouver, on v�rifie qu'aucuns �l�ments superflux va venir causer d'erreur en v�rifiant la taille du message forcement inferieur a 16
					if(msg.length() > 16)
					{
						return false;
					}
					else
					{
						return true;
					}
				}
				else {
					return false;
				}
				
			}
			// dans le cas ou aucuns des marqueurs n'est retrouv�, on retourne que le message est incorrecte.
			else {
				return false;
			}
			
		}
		// Si le message ne contient pas de "," mais est "close_connection" alors c'est une commande autoris� et le message est valid�.
		else if(msg.contains("close_connection"))
		{
			return true;
		}
		else
		{
			return false;
		}
			
	}

	/**
	 * Programme principale ou s'executeras l'ensemble des fonctions du client
	 * @param args
	 * @throws InterruptedException
	 * @throws IOException
	 */
	
	static final Logger logger = Logger.getLogger(Log4j.class);
	
	public static void main(String[] args) throws InterruptedException, IOException {
		
		ConsoleAppender console = new ConsoleAppender();
		console.setLayout(new PatternLayout("%d [%p|%c|%C{1}] %m%n"));
		console.setThreshold(Level.DEBUG);
		console.activateOptions();
		Logger.getRootLogger().addAppender(console);
		
		// ENSEMBLE DES VARIABLES LOCALES //
		final Socket socketClienttemp; 
		Socket socketClient = new Socket(); // socket se connectant au serveur
		final BufferedReader entree; // Va lire les messages re�u par le serveur
		final PrintWriter sortie; // Va envoyer les message du client vers le serveur
		final Scanner sc = new Scanner(System.in); // pour lire les entr�es clavier
		
		Client client = new Client(null,0); // Client initialis� avec les valeurs pr�-enregistrer
		int tentative = 0; // compteur de tentative de connexion initialis� � 0
		String data = null; // donn�e re�u avant connexion pouvant modifi� l'ip du client
		BufferedReader reader = new BufferedReader(
		new InputStreamReader(System.in)); // Nous permet de r�cuperer la commande initiale
		data = reader.readLine();
		if(data.contains("admin")) // Si la commande initial contient "admin" c'est qu'il s'agit d'une carte de modification d'ip
		{
			// Une carte de modification d'ip est de forme "admin,[ip]" on r�cupere donc maintenant l'ip
			String[] command = data.split(",");
			client.setIp(command[1]); // on change l'ip du client pour le nouvel ip obtenu
			client.setPort(Integer.parseInt(command[2]));// on change le port du client pour le nouvel ip obtenu
		}
		logger.info("Client running with the address " + client.getIp() + " on port : " + client.getPort());
		
		
		// D�but de la connexion avec le serveur
		try {
			// Tant qu'il nous reste des tentatives on essaye de se connecter
			while(tentative < 6)
			{
				socketClient = new Socket(); // avant chaque tentative on r�initialise le socket
				try
				{
					// on incremente le compteur de tentative
					tentative++;
					// on essaye de connecter le socket � l'aide des ip et port indiqu� dans le client
					socketClient.connect(new InetSocketAddress(client.getIp(),client.getPort()));
					
					if(socketClient.isConnected())
					{
						// Si on arrive � se connecter, on affiche les informations du socket et on fait en sorte de sortir de la boucle while
						System.out.println(socketClient);
						tentative = 100;
					} // Sinon on continue tant qu'on le peut encore
				}
				catch (IOException e)
				{ // Si la connexion ne c'est pas faite et qu'il nous reste des tentatives
					if(tentative < 6)
					{ // on affiche juste un message indiquant que l'on rencontre des difficult�s et on attend 3 secondes pour s'assurer plus de chances de connexion
						System.err.println("Probleme lors de la connexion, nouvelle tentative dans 3secondes");
						Thread.sleep(3000);
						logger.warn("Retrying connection");
					}else
					{ // Si au bout des 5 tentatives nous ne somme pas connect�, alors on abandonne et on affiche une erreur de connexion
						System.err.println("Delais d�pass�, connexion au serveur �chou�");
						logger.warn("Client couldn't connect, delay passed");
					}
				}
			}
			
			socketClienttemp = socketClient;
			// Si on est correctement connect�, on initialise les moyens de communiqu� via le socket
			sortie = new PrintWriter(socketClient.getOutputStream());
            entree = new BufferedReader(new InputStreamReader(socketClient.getInputStream()));
           
            // On met en place un thread qui permet de communiqu� en continue durant la connexion          
            Thread envoyer = new Thread(new Runnable() {
        	  String msg;
        	  
        	  public void run() {
        		  while(true) {
        			  msg = sc.nextLine();
        			  boolean valid = check_msg(msg);
        			  // On v�rifie si le message peut �tre envoy�
        			  if(valid == true)
        			  {
        				  sortie.println(msg); // si c'est le cas on l'envoi
        				  logger.debug("Send message : " + msg);
        			  }
        			  else
        			  {
        				  System.out.println("Argument invalide !"); // Sinon on affiche une erreur
        				  logger.warn("Argument is invalid");
        			  }
        			  sortie.flush(); // on la sortie pour ne pas envoyer d'information en double ou corrompre les prochaines infromations
        		  }
        	  }
            });
            envoyer.start(); // on lance le Thread
            
            // Cette fois si c'est un Thread pour r�cuperer les informations transmises par le serveur
           Thread recevoir = new Thread(new Runnable() {
        	   
        	   String msg;
        	   
        	   public void run() {
        		   
        		   try {
        			   msg = entree.readLine();
        			   while(msg != null) {
        				   String[] words = msg.split(",",2);
        				   logger.debug("Message received : " + words[1]);
        				   int check = Integer.parseInt(words[0]);
        				   if(check == 0) {
        					   System.out.println("Erreur : " + words[1]);
        				   }else if(check == 1){
        					   System.out.println("Action r�ussie : " + words[1]);
        				   }else {
        					   System.out.println(words[1]);
        					   System.out.println("D�connect� du serveur, arr�t du client.");
        				   }
        				   msg = entree.readLine();
        			   }
        			   sortie.close();
        			   socketClienttemp.close();
        		   }catch(IOException e) {
        			   e.printStackTrace();
        		   }
        	   }
           });
           recevoir.start(); // on lance le Thread d'�coute
          
           Thread timeout = new Thread(new Runnable() {
        	   
        	   String msg;
        	   
        	   public void run() {
        		   
        		   try {
	        		   Thread.sleep(60000);
	        		   msg = "Connection with server too long";
	        		   
	        		   sortie.println(msg);
	        		   msg = "close_connection";
	        		   sortie.println(msg);
	        		   System.out.println("Connexion avec le serveur trop longue, abandon");
	        		   System.exit(0);
        		   }catch (InterruptedException e) {
        			   e.printStackTrace();
        		   }
        	   }
           });
           timeout.start();	
           
            
		}catch(IOException e){
			e.printStackTrace();
			System.err.println("Aucun serveur trouv� ! veuillez v�rifier que les services sont actifs"); // Si ultimement nous n'arrivons pas � nous connect�, nous affichons une erreur.
			logger.fatal("No server found");
		}
	}
}
