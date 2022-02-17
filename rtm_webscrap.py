from email.mime import base
import requests
from bs4 import BeautifulSoup
from rtm_gui import *
import re
import random
from difflib import SequenceMatcher


def en_scrap(en_sentense,kr_sentense):
    #open file
    with open("baseword.txt","r") as f:
        content=f.readlines()
        word_count=len(content)
        word_count2=random.randint(1,word_count)-1
        word=content[word_count2][:-1]
        
    #scrap in naver dictionary
    url='https://www.ybmallinall.com/styleV2/dicview.asp?kwdseq=0&kwdseq2=0&DictCategory=DictEng&DictNum=24&ById=0&PageSize=5&StartNum=&GroupMode=&cmd=0&kwd={}'.format(word)
    response=requests.get(url).content
    html=BeautifulSoup(response,'html.parser')
    
    all_en=html.find_all('div',class_="Word")
    all_kr=html.find_all('div',class_="Example")
    all_en=str(all_en).replace("""<div class="Example">""","").replace("""<div class="Word">""","").replace("<b>","").replace("</b>","").replace("</div>","")
    all_en=all_en[1:][:-1]
    all_en=all_en.split('.,')
    all_kr=str(all_kr).replace("""<div class="Example">""","").replace("""<div class="Word">""","").replace("<b>","").replace("</b>","").replace("</div>","")
    all_kr=all_kr[1:][:-1]
    all_kr=all_kr.split('.,')

    
    sen_count=len(all_en)
    sen_count2=random.randint(1,sen_count)-1
    #result
    en_sentense=all_en[sen_count2]+'.'
    kr_sentense=all_kr[sen_count2]+'.'
    text=re.sub('[^a-zA-Z0-9]',' ',en_sentense)
    add_word=text.split()
    aw_count=len(add_word)
    for i in range(0,aw_count):
        if add_word[i]=='s':
            add_word.remove('s')
        else:
            pass
        if add_word[i]=='ll':
            add_word.remove('ll')
        else:
            pass
        if add_word[i]=='ve':
            add_word.remove('ve')
        else:
            pass
        if add_word[i]=='d':
            add_word.remove('d')
        else:
            pass
        if add_word[i]=='m':
            add_word.remove('m')
        else:
            pass
        if add_word[i]=='a':
            add_word.remove('a')
        else:
            pass
        if len(add_word)==i+1:
            break
    add_word2=random.sample(add_word,1)[0]
    with open("baseword.txt","a") as f:
        f.write(add_word2+"\n")
    return en_sentense , kr_sentense

def en_check(kr_sentense,in_text):
    percent=str(SequenceMatcher(None, kr_sentense, in_text).ratio()*100)[:4]
    return percent