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
import re

baseurl = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, "html.parser")


word = soup.find_all('p')
for occurance in word: 
	element = occurance.text
	paragraph = re.findall('\\bstudent\\b', element)
	print (paragraph)
	element = re.sub('\\bstudent\\b', 'AMAZING student', element)
	print (element)

link = soup.find_all('img')

for a in link: 
	href = a["src"]
	if (href) == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg": 
		a["src"] = "http://new-files.camplenox.com/photos/uploads/15052/normal/sami20140626-16047-zowl8k-0.jpg"

for a in link: 
	href = a["src"]
	if not href.startswith("https:"):
		print ("before changing",a["src"])
		a["src"] = "https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png"
		print (a['src'])

result = str(soup)


f = open("project3.html", "w") 

f.write(result)
f.close()







