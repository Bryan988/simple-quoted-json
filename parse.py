import bson.json_util
import json
import re

file = open('db.bson', 'r', encoding="utf8")
fw = open('data.txt', 'w', encoding="utf8")
print("Starting process")
totalLines = "420440"
compteur = 1
for line in file:
    print(" ---- Step : "+str(compteur) + "/" + totalLines + " ---")
    compteur += 1
    try:
        line = bson.json_util.dumps(line)

    #Removing aboutme
        jsonFileString = json.loads(line)
        jsonFileString = re.sub("(\')(aboutMe)(\':) (.*) \'profilePicture'","'aboutMe': 'aze' ,'profilePicture'", jsonFileString)
        jsonFileString = re.sub("ObjectId\(\'\w*\'\)",'1', jsonFileString)
        jsonFileString = re.sub("None",'1',jsonFileString)
        jsonFileString = re.sub("False",'0',jsonFileString)
        jsonFileString = re.sub("True",'0',jsonFileString)
        jsonFileString = re.sub("datetime\.datetime\([0-9]{4}, [0-9]{2}, [0-9]{2}, [0-9]{2}, [0-9]{2}\)",'0',jsonFileString)
        
        dictJson = eval(jsonFileString)
        fw.write(dictJson['email']+":"+dictJson['password']+ ":" + dictJson['phoneNo'] + "\n")
    except Exception:
        print(Exception)
        pass
print("Process finished")
file.close()
fw.close()
