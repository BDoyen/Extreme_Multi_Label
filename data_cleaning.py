import numpy as np
import re
import csv
import pandas as pd
import string
import numpy as np
from numpy import matrix, rank
        
### data cleaning function - data from stackexchange - Q&A Stackexchange related to  issues

###cleaning title plus tags
def clean0(string):
    
    string = re.sub(r'"",""',"",string)
    arr = [ x.strip() for x in string.strip('\n').split('\n') ]
    body = []
    tags = []
    
    for x in arr:
        
        if x == '':
            body.append('')
            tags.append('')
            
        else:
            x = x.lower()
            values = x.split(',')
               
            title = values[0]
            title = re.sub(r'[^\w\s]','',title)
            body.append(title.replace('"',''))
            
            t = values[1]
            label = t.split('><')
            label = [ elem.replace('<','') for elem in label ]
            label = [ elem.replace('>','') for elem in label ]
            label = [ elem.replace('"','') for elem in label ]
            tags.append(label)
            
    return body,tags


###cleaning body (regex power)
def clean1(string):
    
    string = re.sub(r'<strong>', '', string)
    string = re.sub(r'</strong>', '', string)
    string = re.sub(r'<br>', '', string)
    string = re.sub(r'</br>', '', string)
    string = re.sub(r'<a', '', string)
    string = re.sub(r'</a>', '', string)
    arr = [ x.strip() for x in string.strip('\n').split('"<p>') ]
    result = []
    
    for x in arr:
        x = re.sub(r'[^\w\s]','',x)
        x = re.sub(r'<p>','',x)
        x = re.sub(r'</p>','',x)
        x = re.sub(r'\n','',x)
        x = re.sub(r'"','',x)
        x = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", x)
        x = re.sub(r"\'s", " \'s", x)
        x = re.sub(r"\'ve", " \'ve", x)
        x = re.sub(r"n\'t", " n\'t", x)
        x = re.sub(r"\'re", " \'re", x)
        x = re.sub(r"\'d", " \'d", x)
        x = re.sub(r"\'ll", " \'ll", x)
        x = re.sub(r",", " , ", x)
        x = re.sub(r"!", " ! ", x)
        x = re.sub(r"\(", " \( ", x)
        x = re.sub(r"\)", " \) ", x)
        x = re.sub(r"\?", " \? ", x)
        x = re.sub(r"\s{2,}", " ", x)
        result.append(x.lower())
    
    return result
        

body_static = clean1(se_bodycsv)
body = body_static[1:len(body_static)]
title,tags = clean0(se_title_tagscsv)
title = title[1:len(body_static)]
tags = tags[1:len(body_static)]


#selecting only taged data
def clean2(body):
    title0 = title
    m = len(title)
    i = 0
    while i < m:
        if(title0[i] == ''):
            body[i] = ''
        i += 1
    return body

body = clean2(body)

body = [x for x in body if not x == '']
title = [x for x in title if not x == '']
tags = [x for x in tags if not x == '']        

text = list(map(lambda a,b: a+' '+b, title, body))

accu = []
for x in tags:
    accu = accu + list(x)


list_tags = []
for x in accu:
    if(x not in list_tags):
        list_tags.append(x)


num_c = len(list_tags)  
result_tags = []
for x in tags:
    res = [0]*num_c
    for y in x:
        index = list_tags.index(y)
        res[index] = 1
    result_tags.append(res)


def split(list_text):
    #first split of all the words   
    words_split = list(map(lambda str : str.split(),list_text))
    #list of all the words
    words = []
    for x in words_split:
        for y in x:
            words.append(y)  
    return words


#words in data corpus and label space
#inter = list(set(split(x_text)) & set(list_tags))

#words from labelled and unlabelled data
words_all = split(body)







