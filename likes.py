import urllib
from BeautifulSoup import BeautifulSoup
import requests

imagelist=[]
giflist=[]
def getimagelikes(name):
	url='http://9gag.com/u/'+name+'/likes'
	response=requests.get(url)
	source=response.text.encode('ascii', 'ignore')
	soup=BeautifulSoup(source)
	count=0
	for like in soup.findAll('a',{'class':'badge-evt badge-track badge-track-no-follow' }):
		x= like.findAll('img')
		link=str(x[0].get('src'))
		imagelist.append(str(x[0].get('alt')))
		count+=1
	with open("Output_image.txt", "w+") as text_file:
			for i,j in enumerate(imagelist):
				text_file.write("For image "+str(i)+": "+j )
				text_file.write("\n")

def getgiflikes(name):
	url='http://9gag.com/u/'+name+'/likes'
	response=requests.get(url)
	source=response.text.encode('ascii', 'ignore')
	soup=BeautifulSoup(source)
	count=0
	for like in soup.findAll('div',{'class':'badge-animated-container-static gif-post presenting' }):
		x=like.findAll('img')
		link= str(x[0].get('src'))
		link=link.replace('s.jpg','sv.mp4')
		giflist.append(str(x[0].get('alt')))
		urllib.urlretrieve(link,'gif_'+name+"_"+str(count)+'.mp4')
		count+=1
	with open("Output_gif.txt", "w+") as text_file:
			for i,j in enumerate(giflist):
				text_file.write("For gif "+str(i)+": "+j )
				text_file.write("\n")

ch=raw_input('Enter the name of the user: ')
getgiflikes('mirandared')
getimagelikes(ch)