#Import requests and beautiful soup modules
import requests
from bs4 import BeautifulSoup


def decode():

	#Request for web page http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture
	r = requests.get('http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture')

	#Create Soup
	soup = BeautifulSoup(r.text, 'html.parser')

	#Print out relevant text
	for p in soup(class_='content-section'): 
		x = p.text + '\n'
		print (x.encode('latin-1').decode('utf-8'))


#Allow main program to be run from command line
if __name__ == '__main__':
	decode()
