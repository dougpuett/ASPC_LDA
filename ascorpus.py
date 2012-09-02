import urllib2
import string
import re
import bs4
import os
from bs4 import BeautifulSoup
print("Downloading Old English Poetry From Internet...")
soup = BeautifulSoup(urllib2.urlopen("http://www.sacred-texts.com/neu/ascp/"))

output1 = open(os.getcwd() + "/poems1", 'w')
output2 = open(os.getcwd() + "/names.csv", 'w')
counter = 0
output = ""
names = ""
for link in soup.find_all('a'):
	if link.get('href')[0] == "a":
		soup2 = BeautifulSoup(urllib2.urlopen("http://www.sacred-texts.com/neu/ascp/" + link.get('href')))
		counter += 1
		poem = ""
		for text in soup2.find_all('dd'):
			poem += text.get_text()	
		poem = poem.replace("\n\n", "\n")	
		poem = poem.replace("\n", "")	
		poem = poem.replace(u'\xa0', u" ")
		poem = poem.replace("\n          ", "")
		poem = poem.replace("  ", " ")
		poem = poem.replace("  ", " ")
		poem = poem.replace("  ", " ")
		poem = poem.replace("  ", " ")
		poem = poem.replace("  ", " ")
		poem = poem.replace(u'\xf0', u'th')
		poem = poem.replace(u'\xe6', u'ae')
		poem = poem.replace(u'\xfe', u'th')
		poem = poem.replace(u'\xde', u'Th')
		poem = poem.replace(u'\xd0', u'Th')
		poem = poem.replace(u'\xc6', u'Ae')
		poem = poem.encode('ascii','ignore')
		poem = poem.lower()
		exclude = set(string.punctuation)
		poem = ''.join(ch for ch in poem if ch not in exclude)
		output += poem + "\n"
		names += "%s\t"  %counter
		names += link.get_text() + "\n"
		print(link.get_text() + ": " + "DOWNLOAD COMPLETE")

output1.write("%s \n"  %counter)
output1.write("%s" %output[:-1])
output2.write("%s" %names[:-1])
output1.close()
output2.close()
print("OLD ENGLISH POETIC CORPUS DOWNLOAD COMPLETE")