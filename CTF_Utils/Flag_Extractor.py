def extract(ch):
	f=open(ch , "r")
	ch=f.readline()
	while ch!="" :
		ch=ch[:len(ch)-1]
		p=ch.find("INFO FLAGPART: ")
		if p != -1 :
			ch=ch[p+15:]
			print(ch)
		ch=f.readline()
	f.clsoe()
		
#pp 
extract("server.log")
		
		
		
