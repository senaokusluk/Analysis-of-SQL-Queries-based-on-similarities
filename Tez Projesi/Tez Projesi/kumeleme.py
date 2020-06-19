# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:58:05 2020

@author: Hp
"""

import pandas as pd
ham_data = pd.read_csv("./full_data_son.csv",encoding='ANSI')
clean_data = pd.read_csv("./temizData.csv",encoding='ANSI')
data_list=clean_data["scripts"].tolist()

#bag words işlemi için kullanılıyor
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

cv = CountVectorizer(data_list,min_df=10)
x1=cv.fit_transform(data_list).toarray()


# PCA ile boyut azaltma
from sklearn.decomposition import PCA

pca = PCA(n_components=2,whiten=True)
pca.fit(x1)
x1_pca=pca.transform(x1) 

data_x1=pd.DataFrame(x1_pca,columns=["x","y"])

# k-Means key = 5 için
from sklearn.cluster import KMeans
#Bag of Words ile yapılan veri dönüşümünün kümelenmesi
k_means= KMeans(n_clusters=5)
kumeleme=k_means.fit_predict(x1_pca)

data_x1["label"] = kumeleme


plt.figure(1)
plt.scatter(data_x1.x[data_x1.label == 0],data_x1.y[data_x1.label == 0],color ='red',label="Küme 1")
plt.scatter(data_x1.x[data_x1.label == 1],data_x1.y[data_x1.label == 1],color ='blue',label="Küme 2")
plt.scatter(data_x1.x[data_x1.label == 2],data_x1.y[data_x1.label == 2],color ='green',label="Küme 3")
plt.scatter(data_x1.x[data_x1.label == 3],data_x1.y[data_x1.label == 3],color ='orange',label="Küme 4")
plt.scatter(data_x1.x[data_x1.label == 4],data_x1.y[data_x1.label == 4],color ='magenta',label="Küme 5")

plt.xlabel("X Değerleri")
plt.ylabel("Y Değerleri")
plt.title("Bag of Words ve k-Means ile Kümelenmiş Tablo")
plt.legend(loc='upper right')
plt.show()

# Kümelerden rastgele 20'şer değer alıp birbirleriyle benzeyip benzemediğini kontrol edeceğiz.
import random

#alternatif 1 için
kume0=[]
kume1=[]
kume2=[]
kume3=[]
kume4=[]

for index,data in enumerate(data_x1["label"]):
    if data==0:
        kume0.append(index)
    elif data==1:
        kume1.append(index)
    elif data==2:
        kume2.append(index)
    elif data==3:
        kume3.append(index)
    else:
        kume4.append(index)
  
kume0_sec=[]
kume1_sec=[]
kume2_sec=[]
kume3_sec=[]
kume4_sec=[]

secilmis_eleman0=0
secilmis_eleman1=0
secilmis_eleman2=0
secilmis_eleman3=0
secilmis_eleman4=0

for i in range(30):
    secilmis_eleman0=random.choice(kume0)
    secilmis_eleman1=random.choice(kume1)
    secilmis_eleman2=random.choice(kume2)
    secilmis_eleman3=random.choice(kume3)
    secilmis_eleman4=random.choice(kume4)
    
    if secilmis_eleman0 not in kume0_sec:
        kume0_sec.append(secilmis_eleman0)
    if secilmis_eleman1 not in kume1_sec:
        kume1_sec.append(secilmis_eleman1)
    if secilmis_eleman2 not in kume2_sec:
        kume2_sec.append(secilmis_eleman2)
    if secilmis_eleman3 not in kume3_sec:
        kume3_sec.append(secilmis_eleman3)
    if secilmis_eleman4 not in kume4_sec:
        kume4_sec.append(secilmis_eleman4)


script=""
list_kume0=[]
list_kume1=[]
list_kume2=[]
list_kume3=[]
list_kume4=[]

for i in range(20):
    script=clean_data["scripts"][kume0_sec[i]]
    list_kume0.append(script)
    script=clean_data["scripts"][kume1_sec[i]]
    list_kume1.append(script)
    script=clean_data["scripts"][kume2_sec[i]]
    list_kume2.append(script)
    script=clean_data["scripts"][kume3_sec[i]]
    list_kume3.append(script)
    script=clean_data["scripts"][kume4_sec[i]]
    list_kume4.append(script)

clean_kume0=pd.DataFrame(list_kume0,columns=['Bow Kume 0'])
clean_kume1=pd.DataFrame(list_kume1,columns=['Bow Kume 1'])
clean_kume2=pd.DataFrame(list_kume2,columns=['Bow Kume 2'])
clean_kume3=pd.DataFrame(list_kume3,columns=['Bow Kume 3'])
clean_kume4=pd.DataFrame(list_kume4,columns=['Bow Kume 4'])


clean_kume0.to_csv(r'.\A1Kumeler0.csv',index=False)
clean_kume1.to_csv(r'.\A1Kumeler1.csv',index=False)
clean_kume2.to_csv(r'.\A1Kumeler2.csv',index=False)
clean_kume3.to_csv(r'.\A1Kumeler3.csv',index=False)
clean_kume4.to_csv(r'.\A1Kumeler4.csv',index=False)


#%% TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(data_list,min_df=10)
x2 = tfidf.fit_transform(data_list).toarray()

# PCA ile boyut azaltma
from sklearn.decomposition import PCA
pca = PCA(n_components=2,whiten=True)
pca.fit(x2)
x2_pca=pca.transform(x2) 

data_x2=pd.DataFrame(x2_pca,columns=["x","y"])

# k-Means key = 5 için
from sklearn.cluster import KMeans
#Bag of Words ile yapılan veri dönüşümünün kümelenmesi
k_means2= KMeans(n_clusters=5)
kumeleme2=k_means2.fit_predict(x2_pca)

data_x2["label"] = kumeleme2

plt.figure(2)
plt.scatter(data_x2.x[data_x2.label == 0],data_x2.y[data_x2.label == 0],color ='red',label="Küme 1")
plt.scatter(data_x2.x[data_x2.label == 1],data_x2.y[data_x2.label == 1],color ='blue',label="Küme 2")
plt.scatter(data_x2.x[data_x2.label == 2],data_x2.y[data_x2.label == 2],color ='green',label="Küme 3")
plt.scatter(data_x2.x[data_x2.label == 3],data_x2.y[data_x2.label == 3],color ='orange',label="Küme 4")
plt.scatter(data_x2.x[data_x2.label == 4],data_x2.y[data_x2.label == 4],color ='magenta',label="Küme 5")

plt.xlabel("X Değerleri")
plt.ylabel("Y Değerleri")
plt.title("TF-IDF ve k-Means ile Kümelenmiş Tablo")
plt.legend(loc='lower right')
plt.show()

#%% Kümelerden rastgele 20'şer değer alıp birbirleriyle benzeyip benzemediğini kontrol edeceğiz.
import random

#alternatif 1 için
kume0=[]
kume1=[]
kume2=[]
kume3=[]
kume4=[]

for index,data in enumerate(data_x2["label"]):
    if data==0:
        kume0.append(index)
    elif data==1:
        kume1.append(index)
    elif data==2:
        kume2.append(index)
    elif data==3:
        kume3.append(index)
    else:
        kume4.append(index)
  
kume0_sec=[]
kume1_sec=[]
kume2_sec=[]
kume3_sec=[]
kume4_sec=[]

secilmis_eleman0=0
secilmis_eleman1=0
secilmis_eleman2=0
secilmis_eleman3=0
secilmis_eleman4=0

for i in range(30):
    secilmis_eleman0=random.choice(kume0)
    secilmis_eleman1=random.choice(kume1)
    secilmis_eleman2=random.choice(kume2)
    secilmis_eleman3=random.choice(kume3)
    secilmis_eleman4=random.choice(kume4)
    
    if secilmis_eleman0 not in kume0_sec:
        kume0_sec.append(secilmis_eleman0)
    if secilmis_eleman1 not in kume1_sec:
        kume1_sec.append(secilmis_eleman1)
    if secilmis_eleman2 not in kume2_sec:
        kume2_sec.append(secilmis_eleman2)
    if secilmis_eleman3 not in kume3_sec:
        kume3_sec.append(secilmis_eleman3)
    if secilmis_eleman4 not in kume4_sec:
        kume4_sec.append(secilmis_eleman4)


script=""
list_kume0=[]
list_kume1=[]
list_kume2=[]
list_kume3=[]
list_kume4=[]

for i in range(20):
    script=clean_data["scripts"][kume0_sec[i]]
    list_kume0.append(script)
    script=clean_data["scripts"][kume1_sec[i]]
    list_kume1.append(script)
    script=clean_data["scripts"][kume2_sec[i]]
    list_kume2.append(script)
    script=clean_data["scripts"][kume3_sec[i]]
    list_kume3.append(script)
    script=clean_data["scripts"][kume4_sec[i]]
    list_kume4.append(script)

clean_kume0=pd.DataFrame(list_kume0,columns=['TFIDF Kume 0'])
clean_kume1=pd.DataFrame(list_kume1,columns=['TFIDF Kume 1'])
clean_kume2=pd.DataFrame(list_kume2,columns=['TFIDF Kume 2'])
clean_kume3=pd.DataFrame(list_kume3,columns=['TFIDF Kume 3'])
clean_kume4=pd.DataFrame(list_kume4,columns=['TFIDF Kume 4'])


clean_kume0.to_csv(r'.\A2Kumeler0.csv',index=False)
clean_kume1.to_csv(r'.\A2Kumeler1.csv',index=False)
clean_kume2.to_csv(r'.\A2Kumeler2.csv',index=False)
clean_kume3.to_csv(r'.\A2Kumeler3.csv',index=False)
clean_kume4.to_csv(r'.\A2Kumeler4.csv',index=False)













