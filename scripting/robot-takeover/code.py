import requests
import sys
import re

agent = "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0"
files = ["aNfIgBCI.txt","LcTn5BGk.txt","QgPJjVFxry.txt","4eZhuGnS.txt","fC1I.txt"]
a = [''] * 64
while True:
	url = "http://challenge.ctf.games:31879"
	response = requests.get(url+"/robots.txt",headers={'User-Agent': agent})
	result = response.text
	#print(result)
	for line in result.splitlines():
	#	print(agent)
		if ('User-agent' in line):
			agent = line.split(' ', 1)[1]
		elif ('Disallow' in line):
			f = line.split(' ', 1)[1]
			response = requests.get(url+"/"+f,headers={'User-Agent': agent})
			if ('REJOICE' in response.text):
				print(response.text, f)
				flag_index, file_index = re.findall('INDEX (\d+)', response.text)
				flag_index = int(flag_index)
				file_index = int(file_index)
				print(flag_index, f[file_index+1])
				a[flag_index] = f[file_index+1]
				print(''.join(a))

sys.exit()

for f in files:
	url = "http://challenge.ctf.games:31879/"+f
	response = requests.get(url, headers=headers)
	print(response.text)
	

new_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1"

new_files = ["CkA6DT.txt","wOO1sx.txt","czx.txt","696EVmn.txt"]


new_headers = {
    'User-Agent': new_agent
}
for f in new_files:
	url = "http://challenge.ctf.games:31879/"+f
	response = requests.get(url, headers=new_headers)
	print(response.text)


agent = 'User-agent: Mozilla/5.0 (Windows NT 5.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'
response = requests.get("http://challenge.ctf.games:31879/D5vYWmeggH.txt", headers={'User-Agent':agent})
print(response.text)

#Disallow: /CJq.txt
#Disallow: /5fs9508Azc.txt
#Disallow: /KBr46u.txt
#Disallow: /STE.txt
#Disallow: /0Oi.txt
#User-agent: Mozilla/5.0 (Windows NT 5.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0
#Disallow: /FKBil57C.txt
#Disallow: /QfZQySev.txt
#Disallow: /s66D1dMm.txt
#Disallow: /KBr46u.txt
#Disallow: /PRYp7.txt
#Disallow: /STE.txt
#Disallow: /0Oi.txt

