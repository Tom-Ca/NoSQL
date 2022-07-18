from pymongo import MongoClient
import xmltodict
from menu import *
from pymongo.server_api import ServerApi


def connecte_to_mongodb(client):
    list_dosier = [f for f in os.listdir('./Ressources/') if not os.path.isfile(os.path.join('./Ressources/',f)) ]
    # créé database
    db2 = client["activities_fitbit"]

    for dos in list_dosier:
        if dos != "activities" and dos != "file":
            list_file = os.listdir('Ressources/' + dos + "/")
            for i in list_file:
                # créé collection artiste et lui donne le fichier 01artists.json
                path_file = './Ressources/' + dos + "/" + i
                with open(path_file) as f:
                    file_data = json.load(f)
                    file_data[0].update({"_id": i})
                    collection = db2[dos]
                    # print(f.name)
                try:
                    # print(file_data)
                    collection.insert_many(file_data)
                except :
                    # print("existe deja")
                    pass
        elif dos == "activities":
            list_dosier_act = [f for f in os.listdir('./Ressources/activities/') if
                           not os.path.isfile(os.path.join('./Ressources/activities/', f))]
            for dos_act in list_dosier_act:
                list_file = os.listdir('./Ressources/' + dos + "/" + dos_act + "/")
                for i in list_file:
                    # créé collection artiste et lui donne le fichier 01artists.json
                    path_file = 'Ressources/' + dos + "/" + dos_act + "/" + i
                    with open(path_file) as f:
                        file_data = json.load(f)
                        file_data[0].update({"_id": i})
                    collection = db2[dos + "-" + dos_act]
                    try:
                        collection.insert_many(file_data)
                    except :
                        # print("existe deja")
                        pass

def xml_to_json():

    list_dosier = [ f for f in os.listdir('./Ressources/activities/') if not os.path.isfile(os.path.join('./Ressources/activities/',f)) ]
    list_tcx = os.listdir('./Ressources/file/')

    for dissier in list_dosier:
        list_toXML = []
        list_file = os.listdir('./Ressources/activities/' + dissier + "/")
        for l1 in list_tcx:
            with open('./Ressources/file/' + l1, 'r') as myfile:
                content = myfile.read()
                obj = xmltodict.parse(content)
                activitie_of_file = obj["TrainingCenterDatabase"]["Activities"]["Activity"]["@Sport"]
            if l1[:-4] + '.json' not in list_file and activitie_of_file == dissier:
                list_toXML.append(l1)
        if list_toXML:
            for i in list_toXML:
                with open('Ressources/file/' + i, 'r') as myfile:
                    obj = xmltodict.parse(myfile.read())
                fichier = open('Ressources/activities/' + dissier + "/" + i[:-4] + '.json', "a")
                fichier.write('[')
                fichier.write(json.dumps(obj))
                fichier.write(']')
                fichier.close()
        print(len(list_toXML) , "fichier creer dans" , dissier)

    for file_tcx in list_tcx:
        with open('./Ressources/file/' + file_tcx, 'r') as myfile:
            content = myfile.read()
            obj = xmltodict.parse(content)
            activitie_of_file = obj["TrainingCenterDatabase"]["Activities"]["Activity"]["@Sport"]
            if activitie_of_file not in list_dosier:
                print(activitie_of_file)
                if not os.path.exists('Ressources/activities/' + activitie_of_file):
                    os.makedirs('Ressources/activities/' + activitie_of_file)
                    print("nouveaux dossier creer : ", activitie_of_file)

                fichier = open('Ressources/activities/' + activitie_of_file + "/" + file_tcx[:-4] + '.json', "a")
                fichier.write('[')
                fichier.write(json.dumps(obj))
                fichier.write(']')
                fichier.close()
                print("nouveaux fichier creer dans", activitie_of_file)


def modif_activities():
    list_file = os.listdir('./Ressources/activities/Running')
    # print(list_file)
    for file_tcx in list_file:
        with open('./Ressources/activities/Running/' + file_tcx, 'r') as myfile:
            # print(file_tcx)
            content = (json.loads(myfile.read()))
            try:
                for i in range(len(content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"])):
                    if "Position" in content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]:
                        x = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["Position"]["LatitudeDegrees"])
                        y = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["Position"]["LongitudeDegrees"])
                        content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["LatitudeDegrees"] = x
                        content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["LongitudeDegrees"] = y
                        content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i].pop("Position")

                    if "HeartRateBpm" in content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]:
                        z = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["HeartRateBpm"]["Value"])
                        content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i]["HeartRateBPM"] = z
                        content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]["Track"]["Trackpoint"][i].pop("HeartRateBpm")
            except:
                if len(content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"]) != 7:
                    for j in range(len(content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"])):
                        for i in range(len(content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"]["Trackpoint"])):
                            if "Position" in content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][ "Trackpoint"][i]:
                                x = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["Position"]["LatitudeDegrees"])
                                y = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["Position"]["LongitudeDegrees"])
                                content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["LatitudeDegrees"] = x
                                content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["LongitudeDegrees"] = y
                                content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i].pop("Position")
                            if "HeartRateBpm" in \
                                    content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                        "Trackpoint"][i]:
                                z = (content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["HeartRateBpm"]["Value"])
                                content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i]["HeartRateBPM"] = z
                                content[0]["TrainingCenterDatabase"]["Activities"]["Activity"]["Lap"][j]["Track"][
                                    "Trackpoint"][i].pop("HeartRateBpm")
                pass
                # print(content)

        fichier = open('./Ressources/activities/Running/' + file_tcx, "w")
        fichier.write(json.dumps(content))
        fichier.close()

def replace_tab(client):
    db = client["activities_fitbit"]
    liste_dos = db.list_collection_names()
    i = 0
    i_tab = []
    nexte = 0
    x = 0
    print("Quelle table on remplace ?")
    for dos in liste_dos:
        i_tab.append(i)
        print(i, ":", dos)
        i += 1

    while nexte != 1:
        x = input()
        if int(x) in i_tab:
            nexte = 1
        else:
            print("Mauvaise donnée")
    db.drop_collection(liste_dos[int(x)])
    connecte_to_mongodb(client)

def restaur_bd(client):
    db = client["activities_fitbit"]
    liste_dos = db.list_collection_names()
    for i in liste_dos:
        db.drop_collection(i)
    connecte_to_mongodb(client)

def sup_tab(client):
    db = client["activities_fitbit"]
    liste_dos = db.list_collection_names()
    i = 0
    i_tab = []
    nexte = 0
    x = 0
    print("Quelle table on supprime ?")
    for dos in liste_dos:
        i_tab.append(i)
        print(i, ":", dos)
        i += 1

    while nexte != 1:
        x = input()
        if int(x) in i_tab:
            nexte = 1
        else:
            print("Mauvaise donnée")
    db.drop_collection(liste_dos[int(x)])

def sup_bdd(client):
    db = client["activities_fitbit"]
    liste_dos = db.list_collection_names()
    for dos in liste_dos:
        db.drop_collection(dos)
    print("BDD supprimée")


if __name__ == '__main__':
    # import get_token
    # For local
    client = MongoClient()
    # For Atlas
    # client = MongoClient("mongodb+srv://Tom:5ecMDNgtNR61Neah@cluster0.lre4o.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
    end = 0
    while end != 1:
        nexte = 0
        x = 0
        print("Que voulez-vous faire ?")
        print("0 : Aller chercher de nouvelles données et les insérés")
        print("1 : Insérer de nouvelles données")
        print("2 : Supprimer une table")
        print("3 : Remplacer une table")
        print("4 : Supprimer la bdd")
        print("5 : Restaurer la bdd")
        print("6 : Finir")
        while nexte != 1:
            x = input()
            if x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6":
                nexte = 1
            else:
                print("Mauvaise donnée")

        if x == "0":
            path = user_choice()
            xml_to_json()
            modif_activities()
            connecte_to_mongodb(client)

        elif x == "1":
            connecte_to_mongodb(client)

        elif x == "2":
            sup_tab(client)

        elif x == "3":
            replace_tab(client)

        elif x == "4":
            sup_bdd(client)

        elif x == "5":
            restaur_bd(client)

        elif x == "6":
            end = 1


