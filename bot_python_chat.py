

def find(txt, text):
	msg = text.split()
	
	if txt in msg:
		return "\033[94mBot:\033[92m hello my friend"
	elif koja in msg:
		return "\033[94mBot:\033[92m bye my friend"
	
	else:
		return "\033[91merror"
		
txt = "hello"
koja = "bye"


while True:
	text = input("\033[93myou > \033[97m")
	finds = find(txt, text)
	print(finds)
