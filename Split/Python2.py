from bs4 import BeautifulSoup
import demoji
import datetime

demoji.download_codes()
date = datetime.datetime.now()
#-------------------------------------------------------------------------------------
dire = '/Users/shashishmac/PythonProjects/agenda/htmlDirectory/'

ILApage = open(dire+"ILA.html", 'r')
ILA = BeautifulSoup(ILApage, "lxml")

Mathpage = open(dire+"Math.html", 'r')
Math = BeautifulSoup(Mathpage, "lxml")

Sciencepage = open(dire+"Science.html", 'r')
Science = BeautifulSoup(Sciencepage, "lxml")

SSpage = open(dire+"SS.html", 'r')
SS = BeautifulSoup(SSpage, "lxml")

ACpage = open(dire+"AC.html", 'r')
AC = BeautifulSoup(ACpage, "lxml")

Cellopage = open(dire+"Cello.html", 'r')
Cello = BeautifulSoup(Cellopage, "lxml")
#---------------------------------------------------------------------------------------
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

data = []

ila = []
math = []
science = []
ss = []
ac = []
cello = []

def remove_em(text):
    dem = demoji.findall(text)
    for item in dem.keys():
        text = text.replace(item, '')
    return text
#--------------------------------------------------------------------------------------------------

for x in days:
    for day in ILA.select('h2:-soup-contains('+x+')'):
        response= ''
        try:
            for item in day.find_next('li').find_all('li'):
                bullet_point = next(item.stripped_strings)
                response = response+bullet_point + '<br>'
            ila.append(response)
        except AttributeError:
            ila.append('No School<br>')

for x in days:
    for day in Math.select('h2:-soup-contains('+x+')'):
        response= ''
        try:
            for item in day.find_next('li').find_all('li'):
                response = response + item.text + '<br>'
                response=response.replace("\xa0", '')
                response=response.replace("(Links to an external site.)", '')
            math.append(response)
        except AttributeError:
            ila.append('No School<br>')

for x in days:
    for day in Science.select('h2:-soup-contains('+x+')'):
        response= ''
        try:
            for item in day.find_next('li').find_all('li'):
                bullet_point = next(item.stripped_strings)
                response = response+bullet_point + '<br>'
            science.append(response)
        except AttributeError:
            ila.append('No School<br>')

for x in days:
    for day in SS.select('h2:-soup-contains('+x+')'):
        response = ''
        try:
            for item in day.find_next('li').find_all('li'):
                response = response + item.text + '<br>'
                response=response.replace("\xa0", '')
                response=response.replace("(Links to an external site.)", '')
            ss.append(response)
        except AttributeError:
            ila.append('No School<br>')

for x in days:
    for day in AC.select('h2:-soup-contains('+x+')'):
        response = ''
        try:
            for item in day.find_next('li').find_all('li'):
                bullet_point = next(item.stripped_strings)
                response = response + bullet_point + '<br>'
            ac.append(response)
        except AttributeError:
            ila.append('No School<br>')

# for x in days:
#     for day in Cello.select('h2:-soup-contains('+x+')'):
#         response= ''
#         for item in day.find_next('ul').find_all('li'):
#             bullet_point = next(item.stripped_strings)
#             response = response+bullet_point + '<br>'
#         cello.append(response)

cello = ["No School", "", "", "", ""]

sub = {tuple(ila):"ILA", tuple(math):"Math", tuple(science):"Science", tuple(ss):"Social<br>Studies", tuple(ac): "Academy<br>Connect", tuple(cello):"Elective"}

for clas in sub.keys():
    for element in clas:
        data.append(remove_em(element))

data.pop(8)
data.insert(8, "Block")
data.pop(13)
data.insert(13, "Block")
data.pop(17)
data.insert(17, "Block")
data.pop(22)
data.insert(22, "Block")
data.pop(27)
data.insert(27, "Block")
# print(data)
#----------------------------------------------------------------------------------------------------------------------
#Table
classes = {"ILA":'#d0e2f3', "Math":'#f5cacc', "Science":'#d9ead3', "Social<br>Studies":'#ffe598', "Academy<br>Connect!":
    '#dad2e9', "Elective":'#f9cb9c'}

file = open("/Users/shashishmac/PythonProjects/agenda/output.html", "w")

future = (datetime.datetime.now() + datetime.timedelta(days=7)).date()
stri = str(date.month)+"/"+ str(date.day)+' - '+str(future.month)+"/"+str(future.day)
table = "<h3>Date:______________________<u>"+ stri +"</u>___________________</h3>\n<head>\n<style>table, th, td" \
        " {\nborder: 3px solid black;\nborder-collapse: collapse;\n}\n</style>\n</head>\n<table style='width:100%'>\n"

#-----------------------------------------------------------------------------------
#Table
table += "  <tr>\n"
table += "    <th>{0}</th>\n".format(" ")
for z in days:
    table += "    <th style = 'height:74px;width:350px'>{text}</th>\n".format(text=z)
table += "  </tr>\n"

for index, subject in enumerate(classes):
    table += "  <tr>\n"
    table += f"    <th style='height:100px;width:100px' bgcolor='{classes[subject]}'>{subject}</th>\n"
    for i in range(len(days)):
        table += f"    <td>{data[index * len(days) + i]}</td>\n"
    table += "  </tr>\n"
#-----------------------------------------------------------------------------------

file.writelines(table)


