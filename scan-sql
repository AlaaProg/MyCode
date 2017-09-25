from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from urllib.parse import urljoin

class main():
	def __init__(self,URL):
		super(main,self).__init__()
		self.url    = URL
		self.list_1 = []
		self.Dic    = {}
		self.number = 1
	def fun_001(self,url_2):

		url_Open_1 = urlopen(url_2).read()
		sop_1 = soup(url_Open_1,"html.parser")
		for i in sop_1.findAll("a"):
			url_href = i.get("href")
			if not url_href == None:
				if not i.get("href").startswith("http") and not i.get("href").startswith("https") and not i.get("href").startswith("#"):
					a3 = urljoin(url_2,i.get("href"))
					try:
						if a3 in self.list_1:
							pass
						else:
							
							self.list_1.append(a3)
					except:
						pass
				elif len(url_href.split("/")) > 2 :
					if url_href.split("/")[2] == url_2.split("/")[2]:
						try:
							if url_href in self.list_1:
								pass
							else:
								self.list_1.append(url_href)	
						except:
							pass
				else:
					pass

	def fun_002(self):
		self.fun_001(self.url)
		for i in self.list_1:
			try:
				if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png") or i.endswith(".pdf"):
					continue;
				else:
					self.SQL_004(i)
					self.upload_003(i)
					self.fun_001(i)
			except:
				pass
	def upload_003(self,url_upload):
		#self.number = 1
		try:
			ur_Op = urlopen(url_upload).read()
			sop_2 = soup(ur_Op,"html.parser")
			try:
				upload = sop_2.select("form")
				if upload[0].select("input")[0].get("type") == "file":
					a_1 = "\tupload_:"
					print(a_1+url_upload)

			except:
				pass
		except:
			pass
	def SQL_004(self,url_sql):
		try:
			if int(url_sql[-1]):
				url_Open_3 = urlopen(url_sql).read()
				size = len(url_Open_3)
				if url_Open_3:
					url_Opne_4 = urlopen(url_sql+"+order+by+100--").read()
					if len(url_Opne_4) < size :
						self.number =len(self.Dic)-1
						a_2 = "\tSQL_:"
						print(a_2+url_sql)
						
					else:
						pass
			else:
				pass

		except:
			pass
    
if __name__ == "__main__":
	a =r"""

                                         /$$      /$$           /$$      
                                        | $$  /$ | $$          | $$      
  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$$ | $$ /$$$| $$  /$$$$$$ | $$$$$$$ 
 /$$_____/ /$$_____/ |____  $$| $$__  $$| $$/$$ $$ $$ /$$__  $$| $$__  $$
|  $$$$$$ | $$        /$$$$$$$| $$  \ $$| $$$$_  $$$$| $$$$$$$$| $$  \ $$
 \____  $$| $$       /$$__  $$| $$  | $$| $$$/ \  $$$| $$_____/| $$  | $$
 /$$$$$$$/|  $$$$$$$|  $$$$$$$| $$  | $$| $$/   \  $$|  $$$$$$$| $$$$$$$/
|_______/  \_______/ \_______/|__/  |__/|__/     \__/ \_______/|_______/  



		MMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWM
		W                                    W
		M                 BY                 M
		N                                    N
		W                ----                W
		M                                    M
		W      B o y P r o g r a m e r       W
		N                                    N
		M     -------------------------      M
		W                                    W
		M  Fb:www.facebook.com/boyprogramer  M
		N                                    N
		W ---------------------------------- W
		M                                    M
		WMWMWWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMWMW

		"""
	print("\n\n")
	print(a)
	while True:
		url_input =input("scan_: ")

		if url_input == "exit":
			exit()
		elif url_input.startswith("https") or url_input.startswith("http"):
			try:
				if urlopen(url_input):
					print("\n\n\n\nScan Now:\n\n\n")
					man = main(url_input)
					man.fun_002()
					
			except:
				print("[*]: Url Error'")
		else:
			print("""
\n\t -_- ! -_- ! _>\n
\t\t--------------------------------------
 \t\tscan_> http://127.0.0.1/
 \t\tscan_> exit ==> Close Script
\t\t--------------------------------------
				""")
			
#input()
#http://cqfa.cegep-chicoutimi.qc.ca/public/accueil.html
