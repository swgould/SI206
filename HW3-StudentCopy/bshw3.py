# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
import requests
from bs4 import BeautifulSoup

baseurl = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "lxml")
txt = soup.prettify()

webpage = open('file.html', 'w') 

for occurance in soup.find_all(id_="body-inside"):
	for word in occurance(class_="body-inside2"):
		if word.a == 'studnet':
			word.a.replace('student', 'AMAZING student').strip()


# webpage.write()
# webpage.close()

# webbrowser.open_new_tab('http://collemc.people.si.umich.edu/data/bshw3StarterFile.html')






