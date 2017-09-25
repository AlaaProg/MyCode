from urllib.request import urlopen
from urllib.parse import urljoin
from winsound import Beep
import argparse



def search():
    use = argparse.ArgumentParser(description='Serch Login admin ')
    use.add_argument("-url",dest='url',help="Enter url website")
    use.add_argument('-list',dest='list',help = 'Enter path list')
    gave = use.parse_args()
    url = gave.url
    filelist = gave.list



    try:
        read_list = open(filelist,'r').read().split("\n")
        
        for name_login in read_list:
            request = urljoin(url,name_login)
            try:
                opurl = urlopen(request)
                print('[',opurl.reason,']',request)
                Beep(500,200)
            except:
                "[ No ]{}[ No ]".format(name_login)
    except:
        print("[ # ] -url  : Enter url website ")
        print("[ # ] -list : Enter path list   ")
        print("--------------------------------\n")
        print("[ # ] -url http:/localhost/ -list new.txt  ")


if __name__ == '__main__':
	print(""" 
    00000000000000000000000000000000000000000000000000
    T ______________________________________________ T
    0|                                              |0
    0|          \------ ------- ------/             |0
    0|         || Serch Control Admin ||            |0
    0|          /------ ------- ------\             |0
    0|----------------------------------------------|0
    0|----------------------------------------------|0
    0|          \-----   ----   -----/              |0
    0|         || Shia   BoYs   Hack ||             |0
    0|          /-----   ----   -----\              |0
    0|______________________________________________|0               
    00000000000000000000000000000000000000000000000000
		""")
	search()
        
        
      
    
    
    
