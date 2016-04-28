import tools
import pandas as pd
import csv
import re

def process(text):
    s = tools.clean_words.cleanup(text.split())
    (p,n) = tools.emotion_check.PNrate(' '.join(s))
    if p==0 or n==0:
	print 'data sample is too small!'
    else:
	return float(p)/float(n)

def readin(file_name):
	can=pd.DataFrame(columns=['name','date','tweets'])
	with open(file_name,'rb') as f:
    		reader = csv.reader(f)
    		k=0
    		for row in reader:
        		k+=1
        		print row
        		rw = re.sub(r';+',';',str(row))
        		ro=[rr for rr in rw.split(';')]
        		can.loc[k]=[ro[0],ro[1].split()[0],process(ro[4])]


	return can.groupby(['date']).sum()
