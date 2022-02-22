from email.mime import base
from multiprocessing import get_context
import string
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
    all_kr=all_kr.split('.,')#choose one sentense

    
    sen_count=len(all_en)
    sen_count2=random.randint(1,sen_count)-1
    
    #result
    en_sentense=all_en[sen_count2].replace('.',"")+'.'
    try:
        kr_sentense=all_kr[sen_count2].replace('.',"")+'.'
    except:
        en_sentense="Errorl"
        kr_sentense="Errorl"
        print("error:unexpect list index")

    text=re.sub('[^a-zA-Z0-9]',' ',en_sentense)
    add_word=text.split()
    aw_count=len(add_word)
    for i in range(0,aw_count):
        if len(add_word)==i+1:
            break
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

    if add_word[0]!="Errorl":
        with open("baseword.txt","a") as f:
            f.write(add_word2+"\n")
    else:
        pass
    return en_sentense , kr_sentense, add_word

def en_check(kr_sentense,in_text):
    percent=str(SequenceMatcher(None, kr_sentense, in_text).ratio()*100)[:4]
    return percent

def en_searchword(search_word):
    search_url='https://dic.daum.net/search.do?q={}'.format(search_word)
    response=requests.get(search_url).content
    html=BeautifulSoup(response,'html.parser')
    search_result=str(html.find('ul',attrs={"class":"list_search"}))
    search_result=search_result.replace('<ul class="list_search">',"")
    search_result=search_result.replace('<li><span class="num_search">',"")
    search_result=search_result.replace('</span>',"")
    search_result=search_result.replace('<span class="txt_search">',"")
    search_result=search_result.replace('</daum:word>',"")
    search_result=search_result.replace('</li>',"")
    search_result=search_result.replace('</ul>',"")
    while search_result.find('<')!=-1:
        index1=search_result.find('<')
        index2=search_result.find('>')
        search_result=search_result[:index1]+search_result[index2+1:]
        if search_result.find('<')==-1:
            break
    search_result=search_result.replace('\n'," ")
    search_result=search_result[1:][:-1]
    return search_result