import sys
import requests
import subprocess
#for some reason bs4 was not being nice to me so i had to use this workaround. found this on stack overflow
def install_bs4():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bs4"])
try:
    from bs4 import BeautifulSoup
except:
    install_bs4()
    from bs4 import BeautifulSoup

#opens a txt file, feeds lines into an array, returns that array
def open_txt(txt):
    txtFile = open(txt,"r")
    txt = []
    for line in txtFile:
        line = line.rstrip('\n')
        txt.append(line)
    txtFile.close()
    return txt

#takes in an array and the name of a text file to write to
def write_to_txt(comments,txt):
    n = 1
    results_file = open(txt,"w",encoding="utf-8")
    for element in comments:
        results_file.write(f'Comment {n}.\n{str(element)}\n\n')
        n+=1
    results_file.close()
#takes in a link, returns an array of comments.
def get_reviews(link):
    #open and parses ebay feedback page.
    page = requests.get(link)
    soup = BeautifulSoup(page.text, features="html.parser")
    #get all comments from ebay page
    a = (soup.find_all('div',class_='fdbk-container__details__comment'))
    #converts elements of a to str, strips everything but comment, adds it to l.
    l = []
    for element in a:
        elementb = str(element)
        elementb = elementb.replace('<div class="fdbk-container__details__comment"><!--F#2--><!--F#4--><span>',"")
        elementb = elementb.replace('</span><!--F/--><!--F/--></div>',"")
        l.append(elementb)
    return l    

#takes two arguments, name of input text file, name of output textfile
if __name__ == "__main__":
    links = open_txt(sys.argv[1])
    print(len(links))
    n=0
    for element in links:
        l = get_reviews(element)
        name= sys.argv[2] +"_" + str(n) + ".txt"
        write_to_txt(l,name)
        n=n+1
