import re
with open("baby1990.html") as open_file:
    data = open_file.read()
names = []
nameDict=  {}
m = re.search(r'(?<=in\s)\d+', data)
year = m.group()
#print(year)
names.append(year)
#print(names)
combinedTuple = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>', data)
#print(combinedTuple[0])
for x in combinedTuple:
    #print(x)
    (rank, boyname, girlname) = x
    if boyname not in nameDict:
        nameDict[boyname] = rank
    if girlname not in nameDict:
        nameDict[girlname] = rank
for name in nameDict:
    names.append(name + " " + nameDict[name])
#print(names)
#tesing GIT!!!
text = '\n'.join(names)
print(text)
print(" ")
