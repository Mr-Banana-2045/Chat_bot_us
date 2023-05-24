import time
import datetime

def find(txt, text):
	msg = text.split()
	
	if txt in msg:
		return "\033[94mBot:\033[92m hello my friend"
	elif koja in msg:
		return "\033[94mBot:\033[92m in my pocket"
	elif kojast in msg:
		return "\033[94mBot:\033[92m in my pocket"
	elif chi in msg:
		return "\033[94mBot:\033[92m I don't know, I'm not in the news"
	elif bash in msg:
		return "\033[94mBot:\033[92m Yes, in short"
	elif ki in msg:
		return "\033[94mBot:\033[92m my aunt"
	elif chet in msg:
		return "\033[94mBot:\033[92m not your business"
	elif chetori in msg:
		return "\033[94mBot:\033[92m not your business"
	elif migam in msg:
		return "\033[94mBot:\033[92m to this me"
	elif goftam in msg:
		return "\033[94mBot:\033[92m to this me"
	elif inja in msg:
		return "\033[94mBot:\033[92m my aunt's pocket"
	elif bay in msg:
		return "\033[94mBot:\033[92m Go away so I don't see you again"
	elif emroz in msg:
		return "\033[94mBot:\033[92m I don't know brother"
	elif diroz in msg:
		return "\033[94mBot:\033[92m I don't know brother"
	elif farda in msg:
		return "\033[94mBot:\033[92m I don't know brother"
	elif emsal in msg:
		return "\033[94mBot:\033[92m it's not my business"
	elif parisal in msg:
		return "\033[94mBot:\033[92m it's not my business"
	elif saldige in msg:
		return "\033[94mBot:\033[92m it's not my business"
	elif time in msg:
		now = datetime.datetime.now()
		times = now.strftime("%H:%M:%S")
		return "\033[94mBot:\033[92m "+times
	elif sen in msg:
		return "\033[94mBot:\033[92m not your business"
	elif chera in msg:
		return "\033[94mBot:\033[92m because because"
	elif to in msg:
		return "\033[94mBot:\033[92m not your business"
	elif man in msg:
		return "\033[94mBot:\033[92m okey"
	elif maan in msg:
		return "\033[94mBot:\033[92m okey"
	elif date in msg:
		nom = datetime.datetime.now()
		dates = nom.strftime("%d/%m/%Y")
		return "\033[94mBot:\033[92m "+dates
	else:
		return "\033[91merror"
		
txt = "hello"
koja = "where"
kojast = "where is it"
chi = "what"
bash = "ok"
ki = "when"
chet = "how"
chetori = "how arw you"
migam = "i say"
inja = "here"
bay = "bye"
goftam = "i said"
emroz = "today"
diroz = "yesterday"
farda = "tomorrow"
emsal = "year"
parisal = "last year"
saldige = "next year"
time = "time"
sen = "age"
chera = "why"
to = "you"
man = "me"
maan = "my"
date = "date"

while True:
	text = input("\033[93myou > \033[97m")
	finds = find(txt, text)
	print(finds)