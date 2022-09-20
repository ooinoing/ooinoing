import os
import pandas as pd

PATH = os.getcwd()
file = open(PATH+'/1998_ep_9.txt', "r")

characters = ['일화','동일','노을','정환','덕선','선우','택','동룡','미란','보라','선영','태용','무성','정봉','법원','만순','주치의','간호사','기자1','유람','태수','전경']
josa = [',','의','은','는','']

df = pd.DataFrame(columns=["Q_char","Q_line","A_char","A_line"])

prev_char=''
prev_line=''
cur_char=''
cur_line=''

idx=0
FLAG=0


for line in file.readlines():
    line = line.rstrip()
    
    if(len(line)<2):
        continue
    
    if (line[0] in characters) and (line[1] not in josa):
        #print(line[0]+'\t'+line[1:])
        cur_char=line[0]
        cur_line=line[1:]
        FLAG=1
        
    if (line[:2] in characters) and (line[2] not in josa):
        #print(line[:2]+'\t'+line[2:])
        cur_char=line[:2]
        cur_line=line[2:]
        FLAG=1
    
    if (line[:3] in characters) and (line[3] not in josa):
        #print(line[:3]+'\t'+line[3:])
        cur_char=line[:3]
        cur_line=line[3:]
        FLAG=1
        
    if (FLAG):    
        df.loc[idx]=(prev_char,prev_line,cur_char,cur_line)
        prev_char=cur_char
        prev_line=cur_line
        idx+=1
    
    FLAG=0
    
df.to_csv(PATH+"/ep_9.csv")

file.close()