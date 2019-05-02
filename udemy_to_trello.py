import re
import csv
from datetime import datetime
#Insert udemy_to_trello directory's path below
udemy_to_trello_path = r"udemy_to_trello\udemy_course_content.txt"

raw_course = open(udemy_to_trello_path, "r")
r1 = raw_course.readlines()
for line in r1:
    if line.strip("\n") != "Section:":
        while line =! 
        f.write(line)
dict1 = {r1[i].replace('\n',''):r1[i+1].strip() for i in range(0,len(r1)-1) if bool(re.match("^[0-9]+\.", r1[i]))}
for k in dict1.keys():
    try:
        dict1[k] = datetime.strptime(dict1[k], '%M:%S').time()        
    except ValueError:
        dict1[k] = datetime.strptime('00:00', '%M:%S').time()
#Spliting by day  
shift = 2 * 60
shifts = []
dict_shift = {}
for k in dict1:
    if sum(dict_shift.values()) <= shift:
        dict_shift[k] = float((dict1[k].hour/60) + dict1[k].minute + (dict1[k].second/60))
        print(k, dict_shift[k])
    else:
        print('DIA')
        shifts.append(dict_shift)
        dict_shift = {}
        dict_shift[k] = float((dict1[k].hour/60) + dict1[k].minute + (dict1[k].second/60))
        print(k, dict_shift[k])
shifts.append(dict_shift)
print(shifts)
#Creating python_to_trello .csv
with open('python_to_trello.csv', 'w', encoding="ISO-8859-1", newline='') as output_file:
    w = csv.writer(output_file)
    for i in shifts:
        w.writerows(i.items())
        
    







