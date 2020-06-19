# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:32:01 2020

@author: Hp
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer



#%% Kümelerin karşılaştırılması için

#Kume0 Kelime sayılarını kelime kelime buldurduk
kume0 = pd.read_csv("./A2Kumeler0.csv",encoding='ANSI')
data_list0=kume0["TFIDF Kume 0"].tolist()
tf_kume0 = TfidfVectorizer(data_list0,max_features=35)
kume0_x=tf_kume0.fit_transform(data_list0).toarray()


kelime_sayi0=kume0_x.sum(axis=0).reshape(-1,1)
kelime_sayi_liste0=[]
for i in range(len(kelime_sayi0)):
    kelime_sayi_liste0.append(float(kelime_sayi0[i]))

kelimeler0=tf_kume0.vocabulary_
kelimeler0=list(kelimeler0.keys())
kelimeler0=sorted(kelimeler0)

dict_kelime_sayi0 = {'Kelimeler':kelimeler0,'TFIDF_Kume0_KelimeSayisi':kelime_sayi_liste0}
kelime_sayilari_df0=pd.DataFrame(dict_kelime_sayi0,columns=['Kelimeler','TFIDF_Kume0_KelimeSayisi'])
kelime_sayilari_df0.to_csv(r'.\Kelime_Sayilari_A2Kume0.csv',index=False)


#Kume1 Kelime sayılarını kelime kelime buldurduk
kume1 = pd.read_csv("./A2Kumeler1.csv",encoding='ANSI')
data_list1=kume1["TFIDF Kume 1"].tolist()
tf_kume1 = TfidfVectorizer(data_list1,max_features=35)
kume1_x=tf_kume1.fit_transform(data_list1).toarray()

#Kume1 Kelime sayılarını kelime kelime buldurduk
kelime_sayi1=kume1_x.sum(axis=0).reshape(-1,1)
kelime_sayi_liste1=[]
for i in range(len(kelime_sayi1)):
    kelime_sayi_liste1.append(float(kelime_sayi1[i]))

kelimeler1=tf_kume1.vocabulary_
kelimeler1=list(kelimeler1.keys())
kelimeler1=sorted(kelimeler1)

dict_kelime_sayi1 = {'Kelimeler':kelimeler1,'TFIDF_Kume1_KelimeSayisi':kelime_sayi_liste1}
kelime_sayilari_df1=pd.DataFrame(dict_kelime_sayi1,columns=['Kelimeler','TFIDF_Kume1_KelimeSayisi'])
kelime_sayilari_df1.to_csv(r'.\Kelime_Sayilari_A2Kume1.csv',index=False)


#Kume2 Kelime sayılarını kelime kelime buldurduk
kume2 = pd.read_csv("./A2Kumeler2.csv",encoding='ANSI')
data_list2=kume2["TFIDF Kume 2"].tolist()
tf_kume2 = TfidfVectorizer(data_list2,max_features=35)
kume2_x=tf_kume2.fit_transform(data_list2).toarray()


kelime_sayi2=kume2_x.sum(axis=0).reshape(-1,1)
kelime_sayi_liste2=[]
for i in range(len(kelime_sayi2)):
    kelime_sayi_liste2.append(float(kelime_sayi2[i]))

kelimeler2=tf_kume2.vocabulary_
kelimeler2=list(kelimeler2.keys())
kelimeler2=sorted(kelimeler2)

dict_kelime_sayi2 = {'Kelimeler':kelimeler2,'TFIDF_Kume2_KelimeSayisi':kelime_sayi_liste2}
kelime_sayilari_df2=pd.DataFrame(dict_kelime_sayi2,columns=['Kelimeler','TFIDF_Kume2_KelimeSayisi'])
kelime_sayilari_df2.to_csv(r'.\Kelime_Sayilari_A2Kume2.csv',index=False)


#Kume3 Kelime sayılarını kelime kelime buldurduk
kume3 = pd.read_csv("./A2Kumeler3.csv",encoding='ANSI')
data_list3=kume3["TFIDF Kume 3"].tolist()
tf_kume3 = TfidfVectorizer(data_list3,max_features=35)
kume3_x=tf_kume3.fit_transform(data_list3).toarray()


kelime_sayi3=kume3_x.sum(axis=0).reshape(-1,1)
kelime_sayi_liste3=[]
for i in range(len(kelime_sayi3)):
    kelime_sayi_liste3.append(float(kelime_sayi3[i]))

kelimeler3=tf_kume3.vocabulary_
kelimeler3=list(kelimeler3.keys())
kelimeler3=sorted(kelimeler3)

dict_kelime_sayi3 = {'Kelimeler':kelimeler3,'TFIDF_Kume3_KelimeSayisi':kelime_sayi_liste3}
kelime_sayilari_df3=pd.DataFrame(dict_kelime_sayi3,columns=['Kelimeler','TFIDF_Kume3_KelimeSayisi'])
kelime_sayilari_df3.to_csv(r'.\Kelime_Sayilari_A2Kume3.csv',index=False)



#Kume4 Kelime sayılarını kelime kelime buldurduk
kume4 = pd.read_csv("./A2Kumeler4.csv",encoding='ANSI')
data_list4=kume4["TFIDF Kume 4"].tolist()
tf_kume4 = TfidfVectorizer(data_list4,max_features=35)
kume4_x=tf_kume4.fit_transform(data_list4).toarray()


kelime_sayi4=kume4_x.sum(axis=0).reshape(-1,1)
kelime_sayi_liste4=[]
for i in range(len(kelime_sayi4)):
    kelime_sayi_liste4.append(float(kelime_sayi4[i]))

kelimeler4=tf_kume4.vocabulary_
kelimeler4=list(kelimeler4.keys())
kelimeler4=sorted(kelimeler4)

dict_kelime_sayi4 = {'Kelimeler':kelimeler4,'TFIDF_Kume4_KelimeSayisi':kelime_sayi_liste4}
kelime_sayilari_df4=pd.DataFrame(dict_kelime_sayi4,columns=['Kelimeler','TFIDF_Kume4_KelimeSayisi'])
kelime_sayilari_df4.to_csv(r'.\Kelime_Sayilari_A2Kume4.csv',index=False)

