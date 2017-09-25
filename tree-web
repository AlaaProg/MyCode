from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from urllib.parse import urljoin
import colore as cons
import os 
import sys

class main():
	def __init__(self,URL):

		super(main,self).__init__()
		self.url    = URL
		self.list_1 = []

	def fun_1(self,url_2):
		try:
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
						if url_href.split("/")[2] == url_href.split("/")[2]:
							try:
								if url_href in self.list_1:
									pass
								else:
									self.list_1.append(url_href)	
							except:
								pass
					else:
						pass
		except:
			pass

	def list_w(self,_W):

		N_Text = "web_tree.txt"
		file_A = open(N_Text,"a")
		file_A.write(_W)

	def print_list(self):

		default_colors = cons.get_text_attr()
		default_bg = default_colors & 0x0070
		default_fg = default_colors & 0x0007

		self.fun_1(self.url)
		for i in self.list_1:
			try:
				if i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png") or i.endswith(".pdf"):
					self.list_w("url: "+str(i)+"\n")
					print("\t[ other ]:"+i)
					continue;
				else:
					cons.set_text_attr(cons.FOREGROUND_GREEN | default_bg | cons.FOREGROUND_GREEN )
					print("\t[ url ]:",end=" ")
					sys.stdout.flush()
					cons.set_text_attr(cons.FOREGROUND_GREY | default_bg | cons.FOREGROUND_GREY )
					print(i)
					self.list_w("url: "+str(i)+"\n")
					self.fun_1(i)
					cons.set_text_attr(default_colors)
			except:
				cons.set_text_attr(cons.FOREGROUND_RED | default_bg | cons.FOREGROUND_RED )
				print("\t[ url ]:",end=" ")
				sys.stdout.flush()
				cons.set_text_attr(cons.FOREGROUND_GREY | default_bg | cons.FOREGROUND_GREY )
				print(i+"\n")
				cons.set_text_attr(default_colors)
if __name__ == "__main__":
	a = """

		#   #   #   #   #   #   #   #   #  #  #
		            ---------------
		#          | website paths |          #
		            ---------------
		#                                     #
		                  
		#        By :  Boy PROGRAMER          #

		#     www.FB.com/boy.programmer.3     #

		#                                     #

		#   #  #   #   #   #   #   #   #   #  #
		
	"""
	while True:
		print(a)
		url_input = input("URL_> ")
		if os.path.exists("web_tree.txt"):
			os.remove("web_tree.txt")
		if url_input == "exit":
			exit()
		else:
			print("\n\n\n\n\nStart >\n\n")
			man = main(url_input)
			man.print_list()
