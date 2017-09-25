print ("""
		$####################################################$
		$                                                    $
		$                Alaa Programmer                     $
		$ 													 $
		$####################################################$
""")
def char_list(in_put):
	open("file.txt","w")
	in_put = in_put
	a = list(in_put)
	lis = [1,2,3]
	tr = 0
	for i in range(len(a)):
		s = a[0]
		n = 1
		for c in range(0,len(a)):
			if n < len(a):
				b = a[n]
				a[n] = s
				a[c] = b
				n+=1
			open("file.txt","a+").write("".join(a)+"\n")

def number_(in_put):
	f = open("file.txt","w")
	f.close()
	add = open("file.txt","a+")
	if in_put.endswith("1") or in_put.endswith("2"):
		number = int(in_put[-1]+str("0000000"))
		while True:
			number+=1
			wr = str(in_put[:len(in_put)-1]+str(number))
			if number == 99999999:
				break;
			add.write(wr+"\n")
		add.close()

def plist(i,u):
	open("file.txt","w")
    c = 9999999999999
    while i < c :
        i += 1
        if i.startswith("0"):
            v = '0'
        else:
            v = ''
        n = str(v)+str(i)+'\n'
        open ("file.txt",'a').write(n)
        print(v+i)
        if i == u:
            break
        
         
    
         
