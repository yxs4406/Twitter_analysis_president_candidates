#!/usr/bin/env python
import split_words_new
import re
from nltk.corpus import stopwords

def remove(RE,text):
    ag = re.compile(RE, re.VERBOSE | re.I)
    return ag.sub(r'',text)

def cleanup(text):
    rem={}
    rem[1]='(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)'
    rem[2]='(\<(/?[^>]+)>)'
    rem[3]='(\*)'
    rem[4]='(\[.*\])'
    rem[5]='(\')'
    rem[6]='(\.+)'
    rem[7]='(\/)'
    rem[8]='(\')'
    rem[9]='(\,)'
    rem[10]='(\#)'
    rem[11]='(\:)'
    rem[12]='(\?)'
    rem[13]='(\@)'
    rem[14]='(\-+)'
    rem[15]='(\')'
    rem[16]='(\?)'
    rem[17]='(\%)'
    rem[18]='(\$)'
    rem[19]='(\!)'
    rem[20]='(\~)'
    rem[21]='(\))'
    rem[22]='(\()'
    rem[23]='(\")'
    rem[24]='(\&)'
    rem[25]='(\|)'
    rem[26]='(\+)'
    rem[27]='(\{)'
    rem[28]='(\})'
    rem[29]='(\;)'
    rem[30]='(\^)'
    rem[31]='(\=+)'
    rem[32]='(\_+)'
    rem[33]='(\+?)'
    rem[34]='(\<)'
    rem[35]='(\>)'
    rem[36]='(\")'
    CleanTweets = []
    for i in range(len(text)):
        t = text[i]
        for v in rem.values():
            t = remove(v,t)
        t1 = re.sub(r'[^\x00-\x7f]',r' ',t)
        t2 = t1.lower()
        t3 = [i for i in t2.split() if i not in stopwords.words('english')]
        t4 = ' '.join(t3)
        t5 = ''.join([i for i in t4 if not i.isdigit()])
        t6 = re.sub(r'\\+','',t5)
        t7 = re.sub(r'rt','',t6)
        t77 = t7.encode('ascii','ignore')
        t8 = split_words_new.check_unsplited_word(t77)
        t9 = re.sub(r'\s{2,}',' ',t8)
        t10 = t9.strip()
        t11 = "\n".join([ll.rstrip() for ll in t10.splitlines() if ll.strip()])
        CleanTweets.append(t11)
    Clean_Tweets=list(set(CleanTweets))
#   print(" ".join(Clean_Tweets))
#   print '================================'
    return Clean_Tweets

