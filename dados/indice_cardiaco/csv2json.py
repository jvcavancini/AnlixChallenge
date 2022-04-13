import csv
import json
from os.path import exists

year="2021"
header=["CPF","EPOC","ind_pulm"]

with open('json_data.json', 'w') as outfile:
    outfile.write("[")
    for day in range(0,31):
        for month in range(0,12):
            if day<10:
                file_name="0"+str(day)
            else:
                file_name=str(day)
            if month<10:
                file_name=file_name+"0"+str(month)+"2021"
            else:
                file_name=file_name+str(month)+"2021"
            #opening data file
            if exists(file_name):
                file = open(file_name)
                csvreader=csv.reader(file)
                next(csvreader)
                rows = []
                for row in csvreader:
                    rows.append(dict(zip(header,row[0].split(sep=" ", maxsplit=3))))
                file.close()
                for i in range(0,len(rows)):
                    rows[i]["CPF"]=rows[i]["CPF"][0:3]+rows[i]["CPF"][4:7]+rows[i]["CPF"][8:11]+rows[i]["CPF"][12:14]
                #convert rows to json
                #writes in json
                for row in rows:
                    json_string=json.dumps(row)
                    outfile.write(json_string + ",")
    outfile.write("]")
