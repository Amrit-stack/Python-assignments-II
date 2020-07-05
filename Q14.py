import csv
people=[{'name':'George', 'address':'4312 Abbey Road','age':22},{'name':'John','address':'54 Love Ave','age':21}]
csvfile=open('people.csv','w', newline='')
fields=list(people[0].keys())
obj=csv.DictWriter(csvfile, fieldnames=fields)      
obj.writeheader()      
obj.writerows(people)      
csvfile.close()  