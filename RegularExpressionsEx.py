from bs4 import BeautifulSoup as bs
import re
with open("baby1990.html") as open_file:
    data = open_file.read()

soup = bs(data,"html.parser")

table = soup.find_all('table')
body = table[2].find_all('td')
#print(body)
tdlist = []
ranklist=[]
boylist=[]
girllist=[]
i=0
for item in body:
    if(i%3==0):
        for x in re.findall(r'<td>(\d+)</td>',str(item)):
            ranklist.append(x)
        #ranklist.append(re.findall(r'<td>(\d+)</td>',str(item)))
    i=i+1
#print(ranklist)
j=1
#print(ranklist[0])
for i in range(0,1000):
    for x in re.findall(r'<td>(\w+)</td>',str(body[j])):
        boylist.append(x)
    j=j+3

j=2
for i in range(0,1000):
    #print(body[j])
    for x in re.findall(r'<td>(\w+)</td>',str(body[j])):
        girllist.append(x)
    j=j+3
    
#print(ranklist)
#print(boylist)
#print(girllist)
 totlist = []
for i in range(0,10):
    str1 = ranklist[i]+" "+boylist

 

