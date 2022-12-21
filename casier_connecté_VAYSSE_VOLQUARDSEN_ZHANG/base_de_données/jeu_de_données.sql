INSERT INTO departement(id_departement,nom_departement,sites,filieres)VALUES('1001','Informatique','Saint-Martin','L1-MIPI,L2-I,L3-I');
INSERT INTO departement(id_departement,nom_departement,sites,filieres)VALUES('1002','Mathématiques','Saint-Martin','L1-MIPI,10000004L2-M,L3-M');
INSERT INTO departement(id_departement,nom_departement,sites,filieres)VALUES('1003','Physique','Saint-Martin','L1-MIPI,L2-P,L3-P');
INSERT INTO departement(id_departement,nom_departement,sites,filieres)VALUES('1004','CUPGE','Saint-Martin','L1-MIPI,L2-CUPGE,L3-CUPGE');

INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001030','447034567888','2742','2020-08-31','2023-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001031','447934167848','4378','2020-08-31','2023-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001032','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001033','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001034','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001036','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001037','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001038','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001039','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001040','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001041','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('00001042','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('10000001','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('10000002','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('10000003','007034067988','9341','2015-08-31','2025-07-01');
INSERT INTO carte(id_carte,num,code,date_creation,date_validite)VALUES('10000004','007034067988','9341','2015-08-31','2025-07-01');


INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100493',NULL,'VAYSSE','Matthieu','2002-07-05','matthieuvaysse2002@cyu.fr','0643316947','1001','00001030',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100517',NULL,'VOLQUARDSEN','Alex','2001-12-16','alex.vloquardsen@cyu.fr','0679801313','1001','00001031',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100400',NULL,'LEMAIRE','Marc','1968-10-24','marc.lemaire@cyu.fr','0679561327','1001','10000001',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100401',NULL,'LEMATEU','Gérard','1979-10-13','gerard.lemateu@cyu.fr','0647693821','1002','10000002',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100402',NULL,'OBUCHET','Jeanne','1982-01-01','jeanne.obuchet@cyu.fr','0614312000','1003','10000003',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100403',NULL,'LAGROSTET','David','1980-05-20','gerard.lemateu@cyu.fr','0647693821','1004','10000004',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100415',NULL,'VITO','WAYANE','1990-11-22','WAYANE.VITO@cyu.fr','0677790327','1004','00001032',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100114',NULL,'REMYMORIN','GUYVELINE','1987-08-10','GUYVELINE.REMYMORIN@cyu.fr','0657808624','1001','00001033',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100333',NULL,'HLIHAL','DJAWED','2003-11-23','DJAWED.HLIHAL@cyu.fr','0682498524','1003','00001034',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100087',NULL,'CAPDOROY','SCHNEIDER','1974-09-08','SCHNEIDER.CAPDOROY@cyu.fr','0600440880','1003','00001035',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100921',NULL,'ROCHEFABRE','MARIA-MERCEDES','1966-06-08','MARIA-MERCEDES.ROCHEFABRE@cyu.fr','0674506115','1003','00001036',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100804',NULL,'AMGUINE','GUILIANE','1993-09-22','GUILIANE.AMGUINE@cyu.fr','0685781129','1004','00001037',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100459',NULL,'ROSEFELDMANSEDGWICK','INTISAR','1994-03-03','INTISAR.ROSEFELDMANSEDGWICK@cyu.fr','0640816620','1004','00001038',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100993',NULL,'EZZAOUINI','ABDOULAHI','1995-10-16','ABDOULAHI.EZZAOUINI@cyu.fr','0639223346','1001','00001039',false,NULL,false);
INSERT INTO utilisateur (id_uti, mdp_uti, nom_uti, prenom_uti, anniversaire_uti, mail_uti, telephone_uti, departement, id_carte, penalite, temps_penalite, handicap)VALUES('22100630',NULL,'MACIUGA','CHAHINE','1970-08-22','CHAHINE.MACIUGA@cyu.fr','0617398801','1002','00001040',false,NULL,false);

INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100493','2022-2023','L3-I','GroupeCMS5','groupeD',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100517','2022-2023','L3-I','GroupeCMS5','groupeD',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100415','2022-2023','L2-I','GroupeCMS3','groupeA',0,true);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100114','2022-2023','L2-I','GroupeCMS3','groupeC',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100087','2022-2023','L3-M','GroupeCMS5','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100630','2022-2023','L2-M','GroupeCMS3','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100804','2022-2023','L2-M','GroupeCMS3','groupeB',0,true);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100872','2022-2023','L2-P','GroupeCMS3','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100921','2022-2023','L3-P','GroupeCMS5','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100459','2022-2023','L3-P','GroupeCMS5','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100993','2022-2023','L3-CUPGE','GroupeCMS5','groupeA',0,false);
INSERT INTO etudiant(id_etudiant,annee_etude,filiere,groupe_CM,groupe_TD,utilisation_etudiant,tuteur)VALUES('22100333','2022-2023','L3-CUPGE','GroupeCMS5','groupeA',0,false);

INSERT INTO enseignant(id_enseignant,utilisation_prof,filieres)VALUES('22100400',0,'L3-I/L1-MIPI/L2-I');
INSERT INTO enseignant(id_enseignant,utilisation_prof,filieres)VALUES('22100401',0,'L1-MIPI/L2-M/L3-M');
INSERT INTO enseignant(id_enseignant,utilisation_prof,filieres)VALUES('22100402',0,'L1-MIPI/L2-P/L3-P');
INSERT INTO enseignant(id_enseignant,utilisation_prof,filieres)VALUES('22100403',0,'L1-MIPI/L2-CUPGE/L3-CUPGE');


INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00205','TD-3projetBD/Réseau','1001',25,'13:45','16:15');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00206','CMAlgoetSDA','1001',25,'08:30','10:00');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00102','CMdroite','1002',25,'09:00','12:45');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00201','TDdroite','1002',25,'13:45','18:00');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00212','CMpoint','1003',25,'08:45','13:00');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00213','TDpoint','1003',25,'14:30','16:30');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00250','CMdur','1004',25,'08:45','11:15');
INSERT INTO periode_cours(id_cours,nom,departement,effectif,debut,fin)VALUES('00218','TDcompliqué','1004',25,'13:00','16:00');

INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_01','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_02','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_03','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_04','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_05','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_06','1001',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_07','1002',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_08','1002',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_09','1002',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_10','1002',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_11','1003',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_12','1003',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_13','1003',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_14','1004',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_15','1004',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_16','1004',false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_17',NULL,false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_18',NULL,false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_19',NULL,false,false,NULL,NULL,NULL);
INSERT INTO casier(id_casier,id_dep,occupe,reserve,heure_reservation,heure_butoire,id_uti)VALUES('locker_20',NULL,false,false,NULL,NULL,NULL);


INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100493','1001');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100517','1001');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100400','1001');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100401','1002');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100402','1003');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100403','1004');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100415','1004');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100114','1001');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100333','1003');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100087','1003');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100921','1003');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100804','1004');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100459','1004');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100993','1001');
INSERT INTO est_dans(id_utilisateur,id_departement)VALUES('22100630','1002');


INSERT INTO est_en_cours(id_uti,id_cours)VALUES('22100493','00205');
INSERT INTO est_en_cours(id_uti,id_cours)VALUES('22100493','00206');