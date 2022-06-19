import xml.etree.ElementTree as ET
from selenium import webdriver
#----------------------------------------------------------------------------------------------
tree = ET.parse('/Users/shashishmac/PythonProjects/agenda/input.xml')
root = tree.getroot()
#------------------------------------------------------------------------------------------------

POST_LOGIN_URL = 'https://fisd.instructure.com/login/ldap'

for u in root.iter('username'):
    username = u.text

for p in root.iter('password'):
    password = p.text

for I in root.iter('ILA'):
    ILAlink = I.text

for M in root.iter('Math'):
    Mathlink = M.text

for S in root.iter('Science'):
    Sciencelink = S.text

for SS in root.iter('SS'):
    SSlink = SS.text

for AC in root.iter('AC'):
    AClink = AC.text

for Cello in root.iter('Cello'):
    Cellolink = Cello.text

#------------------------------------------------------------------------------------------
driver = webdriver.Chrome('/Users/shashishmac/PythonProjects/agenda/chromedriver')
driver.get(POST_LOGIN_URL)

driver.find_element_by_name('pseudonym_session[unique_id]').send_keys(username)
driver.find_element_by_name('pseudonym_session[password]').send_keys(password)
driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/div[2]/button').click()
#--------------------------------------------------------------------------------------------
dire = '/Users/shashishmac/PythonProjects/agenda/htmlDirectory/'

driver.get(ILAlink)
ILApage = driver.page_source
Ila = open(dire+"ILA.html", "w")
Ila.writelines(ILApage)

driver.get(Mathlink)
Mathpage = driver.page_source
Math = open(dire+"Math.html", "w")
Math.writelines(Mathpage)

driver.get(Sciencelink)
Sciencepage = driver.page_source
Science = open(dire+"Science.html", "w")
Science.writelines(Sciencepage)

driver.get(SSlink)
SSpage = driver.page_source
SS = open(dire+"SS.html", "w")
SS.writelines(SSpage)

driver.get(AClink)
ACpage = driver.page_source
AC = open(dire+"AC.html", "w")
AC.writelines(ACpage)

driver.get(Cellolink)
Cellopage = driver.page_source
Cello = open(dire+"Cello.html", "w")
Cello.writelines(Cellopage)


