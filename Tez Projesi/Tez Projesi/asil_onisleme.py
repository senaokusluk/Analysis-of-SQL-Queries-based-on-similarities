# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:24:46 2020

@author: Hp
"""
import pandas as pd
import re

data_sorgular = pd.read_csv("./full_data_son.csv",encoding='ANSI',error_bad_lines=False) #,sep=";"
data_sorgular = data_sorgular['scripts'].str.lower()

data_sorgular = pd.DataFrame(data_sorgular,columns=['scripts'])

data_tablolar = pd.read_csv("./Tablolar.csv",encoding='ANSI',error_bad_lines=False) #,sep=";"
data_tablolar = data_tablolar['tabloAdlari'].str.lower()

data_tablolar = pd.DataFrame(data_tablolar,columns=['tabloAdlari'])


metin="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
metin=metin.lower()
list_alfabe=metin.split(" ")

list_yeni=[]
for sorgu in data_sorgular["scripts"]:
    for isim in data_tablolar["tabloAdlari"]:
        sorgu=sorgu.replace("insert into","insertinto")
        deger=str(isim)
        deger=deger.replace("[","")
        deger=deger.replace("]","")
        deger=deger.replace("'","")
        sorgu=sorgu.replace(deger,"")
    
    
    sorgu=sorgu.replace('cast',"castinto")
    sorgu=sorgu.replace('row_number',"row number")
    sorgu=sorgu.replace('"',"")
    sorgu=sorgu.replace('*',"")
    sorgu=sorgu.replace('\\',"")
    sorgu=sorgu.replace('>',"")
    sorgu=sorgu.replace('<',"")
    sorgu=sorgu.replace('?',"")
    sorgu=sorgu.replace('-',"")
    sorgu=sorgu.replace('-=',"")
    sorgu=sorgu.replace('+=',"")
    sorgu=sorgu.replace('*=',"")
    sorgu=sorgu.replace('/=',"")
    sorgu=sorgu.replace('='," ")
    sorgu=sorgu.replace(')'," ")
    sorgu=sorgu.replace('('," ")
    sorgu=sorgu.replace(']',"~")
    sorgu=sorgu.replace('[',"~")
    sorgu=sorgu.replace(':',"")
    sorgu=sorgu.replace('{',"")
    sorgu=sorgu.replace('}',"")
    
    sil=re.findall("[a-z0-9@]+\s{1}[i][n][t]",sorgu)
    sil1=re.findall("[a-z0-9@]+\s{1}[n][v][a][r][c][h][a][r]",sorgu)
    sil=sil+sil1
    esitMi=False
    for i in range(len(sil)):
        deger1=sil[i].split(" ")
        for j in range(len(list_alfabe)):
            silinecek_deger=deger1[0]
            if silinecek_deger==list_alfabe[j]:
                esitMi=True
        if esitMi==False:        
            if deger1[0]!="convert":
                sorgu=sorgu.replace(deger1[0],"")
    
    sil=re.findall("[a-z0-9]+[.]{1}[a-z0-9]+",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
    sil=re.findall("[a-z0-9]+[_]{1}[a-z0-9]+[_]{1}[a-z0-9]+",sorgu)
    sil1=re.findall("[a-z0-9]+[_]+[a-z0-9]+",sorgu)
    sil=sil+sil1
    
    for i in range(len(sil)):
            sorgu=sorgu.replace(sil[i],"")
    
    sil=re.findall("[a-z0-9]+[_]{1}",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
    
    sil=re.findall("[a-z0-9]{1}[a-z0-9]{1}[a-z0-9]{1}[.]{1}",sorgu)
    sil1=re.findall("[a-z0-9]{1}[a-z0-9]{1}[.]{1}",sorgu)
    sil2=re.findall("[a-z0-9]{1}[.]{1}",sorgu)
    sil=sil+sil1+sil2
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
    sil=re.findall("[a-z0-9]+[.]{1}\s",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
    
    sil=re.findall("'[a-z\s0-9/%@+~^|`=&/]+'",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
    
    sil=re.findall("##[a-z\s0-9%]+##",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
    sil=re.findall("#[a-z0-9]+",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
    sil=re.findall("'[a-z\s0-9/%@+~^|`=&/]+'",sorgu)
    sil1=re.findall("'\s{1}[a-z\s0-9/%@+~`^|]+'",sorgu)
    sil2=re.findall("'%\s{1}[a-z\s0-9/%@+~`^|]+%'",sorgu)
    sil=sil+sil1+sil2
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
    
    sil=re.findall("[0-9]{1}[0-9]{1}[0-9]{1}",sorgu)
    sil1=re.findall("[0-9]{1}[0-9]{1}",sorgu)
    sil2=re.findall("[0-9]{1}",sorgu)
    sil=sil+sil1+sil2
    for i in range(len(sil)):
        deger=str(sil[i])
        deger=deger.replace("[","")
        deger=deger.replace("]","")
        deger=deger.replace("'","")
        sorgu=sorgu.replace(deger," ")  
        
    sil=re.findall("[w][i][t][h]\s{1}[a-z0-9]+\s{1}[a][s]",sorgu)
    esitMi=False
    for i in range(len(sil)):
        for j in range(len(list_alfabe)):
            deger=sil[i].split(" ")
            if deger[1]==list_alfabe[j]:
                esitMi=True
        if esitMi==False:
            sorgu=sorgu.replace(sil[i],"with")
            sorgu=sorgu.replace(" "+deger[1]+" "," ")
    
    sil=re.findall("\s{1}[a][s]\s{1}[a-z_]+[a-z]+",sorgu)
    sil1=re.findall("\s[~]{1}[a-z\s/%']+[~]{1}\s",sorgu)
    sil2=re.findall("\s[~]{1}[a-z\s/%']+\s[a-z\s/%']+[~]{1}\s",sorgu)
    sil=sil+sil1+sil2
    esitMi=False
    for i in range(len(sil)):
        deger=sil[i]
        deger=deger.lstrip()
        deger=deger.rstrip()
        deger_liste=deger.split(" ")
        if len(deger_liste)>1:
            silinecek_deger=deger_liste[1]
            for j in range(len(list_alfabe)):
                if silinecek_deger==list_alfabe[j]:
                    esitMi=True
            if esitMi==False:
                    if deger_liste[1]!="float":
                        if deger_liste[1]!="int":
                            if deger_liste[1]!="decimal":
                                if deger_liste[1]!="varchar":
                                    if deger_liste[1]!="datepart":
                                        if deger_liste[1]!="numeric":
                                            if deger_liste[1]!="date":
                                                if deger_liste[1]!="bigint":
                                                    if deger_liste[1]!="xml":
                                                        sorgu=sorgu.replace(sil[i]," ")
                                                        if deger_liste[1]!="month":
                                                            if deger_liste[1]!="year":
                                                                if deger_liste[1]!="day":
                                                                    if deger_liste[1]!="week":
                                                                        if deger_liste[1]!="num":
                                                                            if deger_liste[1]!="weekday":
                                                                                sorgu=sorgu.replace(deger_liste[1]," ")
                                                    
        
    
        
    sil=re.findall("[a-z0-9]{1}[a-z0-9]+[,]{1}\s",sorgu)
    for harf in list_alfabe:
        str1=harf+", "
        if any(str1 in s for s in sil):
            sinir_deger=sil.count(str1)
            for m in range(sinir_deger):
                sil.remove(str1)
    esitMi=False            
    for i in range(len(sil)):
        for j in range(len(list_alfabe)):
            deger=sil[i].split(",")
            if deger[0]==list_alfabe[j]:
                esitMi=True
        if esitMi==False:
            if deger[0]!="null":
                if deger[0]!="datetime":
                    if deger[0]!="date":
                        if deger[0]!="month":
                            if deger[0]!="day":
                                if deger[0]!="year":
                                    if deger[0]!="dd":
                                        if deger[0]!="mm":
                                            if deger[0]!="yy":
                                                if deger[0]!="week":
                                                    if deger[0]!="asc":
                                                        if deger[0]!="int":
                                                            if deger[0]!="hour":
                                                                if deger[0]!="num":
                                                                    if deger[0]!="weekday":
                                                                        if deger[0]!="numeric":
                                                                            sorgu=sorgu.replace(deger[0]," ")
                                    
    
    sil=re.findall("[a-z0-9]{1}[a-z0-9]+[,]{1}\s",sorgu)
    sil1=re.findall("[a-z0-9]{1}[,]{1}\s",sorgu)
    sil=sil+sil1
    for harf in list_alfabe:
        str1=harf+", "
        if any(str1 in s for s in sil):
            sinir_deger=sil.count(str1)
            for m in range(sinir_deger):
                sil.remove(str1)
    esitMi=False           
    for i in range(len(sil)):
         for j in range(len(list_alfabe)):
            deger=sil[i].split(",")
            if deger[0]==list_alfabe[j]:
                esitMi=True
         if esitMi==False:
            if deger[0]!="null":
                if deger[0]!="datetime":
                    if deger[0]!="date":
                        if deger[0]!="month":
                            if deger[0]!="day":
                                if deger[0]!="year":
                                    if deger[0]!="dd":
                                        if deger[0]!="mm":
                                            if deger[0]!="yy":
                                                if deger[0]!="week":
                                                    if deger[0]!="asc":
                                                        if deger[0]!="int":
                                                            if deger[0]!="hour":
                                                                if deger[0]!="num":
                                                                    if deger[0]!="weekday":
                                                                        if deger[0]!="numeric":
                                                                            sorgu=sorgu.replace(deger[0]," ")
                                    
            
    sil=re.findall("\s{1}[a-z]{1}\s{1}",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i]," ")
    
    sil=re.findall("[@]{1}[a-z0-9]+",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
    
        
    sil=re.findall("\s{1}[/]{1}[a-z0-9]+[/]{1}\s{1}",sorgu)
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
        
        
    sorgu=sorgu.replace(','," ")
    sorgu=sorgu.replace('_',"")
    sorgu=sorgu.replace('!',"")
    sorgu=sorgu.replace('/',"")
    sorgu=sorgu.replace('~~',"")
    sorgu=sorgu.replace('+',"")
    sorgu=sorgu.replace("''","")
    sorgu=sorgu.replace('@',"")
    sorgu=sorgu.replace('#',"")
    sorgu=sorgu.replace(' . '," ")
    sorgu=sorgu.replace('  '," ")
    sorgu=sorgu.replace('   '," ")
    sorgu=sorgu.replace('    '," ")
    sorgu=sorgu.replace('  '," ")
    sorgu=sorgu.replace(';',"")
    sorgu=sorgu.replace(' . '," ")
    sorgu=sorgu.replace('.',"")
    sorgu=sorgu.replace("''","")
    sorgu=sorgu.replace("&","")
    
    sil=re.findall("\s{1}[a][s]\s{1}[~]{1}[/'%a-z\s]+[~]{1}\s{1}",sorgu)
    sil1=re.findall("\s[~]{1}[/'%a-z\s]+[~]{1}",sorgu)
    sil=sil+sil1
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i]," ")
    
    
    sorgu=sorgu.replace("ctinto","cast")
    sorgu=sorgu.replace("castinto","cast")
    sorgu=sorgu.replace("insertinto","insert into")
    sorgu=sorgu.replace("as as","")
    sorgu=sorgu.replace(" as "," ")
    sorgu=sorgu.replace('id',"")
    sorgu=sorgu.replace('entity',"identity")
    sorgu=sorgu.replace(" ~~ "," ")
    sorgu=sorgu.replace("~~"," ")
    sorgu=sorgu.replace(" ' ' "," ")
    sorgu=sorgu.replace(" name "," ")
    sorgu=sorgu.replace(" ~ "," ")
    sorgu=sorgu.replace("%"," ")
    sorgu=sorgu.replace(" group by "," group ")
    sorgu=sorgu.replace(" group "," group by ")
    sorgu=sorgu.replace(" order by "," order ")
    sorgu=sorgu.replace(" order "," order by ")
    sorgu=sorgu.replace("~"," ")
    
    for val in list_alfabe:
        val=str(val)
        sorgu=sorgu.replace(" "+val+" " , " ")
        if val!="e":
            sorgu=sorgu.replace(val+"time" , " ")
        sorgu=sorgu.replace(" "+val+val+" " , " ")
        sorgu=sorgu.replace(" "+val+val+val+" " , " ")
        sorgu=sorgu.replace(" "+val+val+val+val+" " , " ")
    
    sil=re.findall("'[a-z\s0-9/%@+~^$|`]+'",sorgu)
    sil1=re.findall("'\s{1}[a-z\s0-9/%@+~`^$|]+'",sorgu)
    sil2=re.findall("'%\s{1}[a-z\s0-9/%@+~`^$|]+%'",sorgu)
    sil=sil+sil1+sil2
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i],"")
    
    sorgu=sorgu.replace(" etime " , " ")
    sorgu=sorgu.replace(" tinto " , " ")
    sorgu=sorgu.replace(" tp " , " ")
    sorgu=sorgu.replace(" stdev " , " ")
    
    sil=re.findall("\s{1}[a-z]{1}[a-z]{1}\s{1}",sorgu)
    if any(" or " in s for s in sil):
        sinir_deger=sil.count(" or ")
        for i in range(sinir_deger):
            sil.remove(" or ")
    if any(" on " in s for s in sil):
        sinir_deger=sil.count(" on ")
        for i in range(sinir_deger):
            sil.remove(" on ")
    if any(" is " in s for s in sil):
        sinir_deger=sil.count(" is ")
        for i in range(sinir_deger):
            sil.remove(" is ")
    if any(" by " in s for s in sil):
        sinir_deger=sil.count(" by ")
        for i in range(sinir_deger):
            sil.remove(" by ")
    if any(" in " in s for s in sil):
        sinir_deger=sil.count(" in ")
        for i in range(sinir_deger):
            sil.remove(" in ")
            
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i]," ")
        
    sil=re.findall("\s{1}[a-z]{1}[a-z]{1}[a-z]{1}\s{1}",sorgu)
    if any(" and " in s for s in sil):
        sinir_deger=sil.count(" and ")
        for i in range(sinir_deger):
            sil.remove(" and ")
    if any(" end " in s for s in sil):
        sinir_deger=sil.count(" end ")
        for i in range(sinir_deger):
            sil.remove(" end ")
    if any(" asc " in s for s in sil):
        sinir_deger=sil.count(" asc ")
        for i in range(sinir_deger):
            sil.remove(" asc ")
    if any(" top " in s for s in sil):
        sinir_deger=sil.count(" top ")
        for i in range(sinir_deger):
            sil.remove(" top ")
    if any(" not " in s for s in sil):
        sinir_deger=sil.count(" not ")
        for i in range(sinir_deger):
            sil.remove(" not ")
    if any(" min " in s for s in sil):
        sinir_deger=sil.count(" min ")
        for i in range(sinir_deger):
            sil.remove(" min ")
    if any(" max " in s for s in sil):
        sinir_deger=sil.count(" max ")
        for i in range(sinir_deger):
            sil.remove(" max ")
    if any(" sum " in s for s in sil):
        sinir_deger=sil.count(" sum ")
        for i in range(sinir_deger):
            sil.remove(" sum ")
    if any(" len " in s for s in sil):
        sinir_deger=sil.count(" len ")
        for i in range(sinir_deger):
            sil.remove(" len ")
    if any(" avg " in s for s in sil):
        sinir_deger=sil.count(" avg ")
        for i in range(sinir_deger):
            sil.remove(" avg ")
    if any(" int " in s for s in sil):
        sinir_deger=sil.count(" int ")
        for i in range(sinir_deger):
            sil.remove(" int ")
    if any(" set " in s for s in sil):
        sinir_deger=sil.count(" set ")
        for i in range(sinir_deger):
            sil.remove(" set ")
    if any(" get " in s for s in sil):
        sinir_deger=sil.count(" get ")
        for i in range(sinir_deger):
            sil.remove(" get ")
    if any(" put " in s for s in sil):
        sinir_deger=sil.count(" put ")
        for i in range(sinir_deger):
            sil.remove(" put ")
    if any(" use " in s for s in sil):
        sinir_deger=sil.count(" use ")
        for i in range(sinir_deger):
            sil.remove(" use ")
    if any(" row " in s for s in sil):
        sinir_deger=sil.count(" row ")
        for i in range(sinir_deger):
            sil.remove(" row ")
    if any(" day " in s for s in sil):
        sinir_deger=sil.count(" day ")
        for i in range(sinir_deger):
            sil.remove(" day ")
    if any(" key " in s for s in sil):
        sinir_deger=sil.count(" key ")
        for i in range(sinir_deger):
            sil.remove(" key ")
    if any(" log " in s for s in sil):
        sinir_deger=sil.count(" log ")
        for i in range(sinir_deger):
            sil.remove(" log ")
    if any(" str " in s for s in sil):
        sinir_deger=sil.count(" str ")
        for i in range(sinir_deger):
            sil.remove(" str ")
    if any(" for " in s for s in sil):
        sinir_deger=sil.count(" for ")
        for i in range(sinir_deger):
            sil.remove(" for ")
    if any(" num " in s for s in sil):
        sinir_deger=sil.count(" num ")
        for i in range(sinir_deger):
            sil.remove(" num ")
    if any(" abs " in s for s in sil):
        sinir_deger=sil.count(" abs ")
        for i in range(sinir_deger):
            sil.remove(" abs ")
    if any(" raw " in s for s in sil):
        sinir_deger=sil.count(" raw ")
        for i in range(sinir_deger):
            sil.remove(" raw ")
    if any(" xml " in s for s in sil):
        sinir_deger=sil.count(" xml ")
        for i in range(sinir_deger):
            sil.remove(" xml ")
    for i in range(len(sil)):
        sorgu=sorgu.replace(sil[i]," ")
        
    sorgu=sorgu.replace("stdev"," ")
    sorgu=sorgu.replace("relevantbyweek"," ")
    sorgu=sorgu.replace(" value "," ")
    sorgu=sorgu.replace(" cs "," ")
    sorgu=sorgu.replace(" clustered "," ")
    sorgu=sorgu.replace(" sysobjects "," ")
    sorgu=sorgu.replace(" aver "," ")
    sorgu=sorgu.replace(" arent "," ")
    sorgu=sorgu.replace(" status "," ")
    sorgu=sorgu.replace(" sele "," select ")
    sorgu=sorgu.replace("sele "," select ")
    sorgu=sorgu.replace(" quotename "," ")
    sorgu=sorgu.replace(" name "," ")
    sorgu=sorgu.replace(" lect "," ")
    sorgu=sorgu.replace(" name "," ")
    sorgu=sorgu.replace(" lastname "," ")
    sorgu=sorgu.replace(" gro "," group ")
    sorgu=sorgu.replace(" result "," ")
    sorgu=sorgu.replace(" wh "," ")
    sorgu=sorgu.replace(" rep "," ")
    sorgu=sorgu.replace(" subq "," ")
    sorgu=sorgu.replace(" activity "," ")
    sorgu=sorgu.replace(" amount "," ")
    sorgu=sorgu.replace(" badge "," ")
    sorgu=sorgu.replace(" bottom "," ")
    sorgu=sorgu.replace(" firstname "," ")
    sorgu=sorgu.replace(" wi "," with ")
    sorgu=re.sub("\\W"," ",sorgu)
    
    for val in list_alfabe:
        val=str(val)
        sorgu=sorgu.replace(" "+val+" " , " ")
        if val!="e":
            sorgu=sorgu.replace(val+"time" , " ")
        sorgu=sorgu.replace(" "+val+val+" " , " ")
        sorgu=sorgu.replace(" "+val+val+val+" " , " ")
        sorgu=sorgu.replace(" "+val+val+val+val+" " , " ")
        
    sorgu=sorgu.replace("      "," ")
    sorgu=sorgu.replace("     "," ")
    sorgu=sorgu.replace("    "," ")
    sorgu=sorgu.replace("   "," ")
    sorgu=sorgu.replace("  "," ")
    sorgu=sorgu.strip()
    
    if sorgu!="":
        list_yeni.append(sorgu)

cleaned_data=pd.DataFrame(list_yeni,columns=['scripts'])

cleaned_data.to_csv(r'.\temizData.csv',index=False)