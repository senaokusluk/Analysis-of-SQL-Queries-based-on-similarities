# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:09:35 2020

@author: Hp
"""

import pandas as pd
ham_data = pd.read_csv("./full_data_son.csv",encoding='ANSI')
clean_data = pd.read_csv("./temizData.csv",encoding='ANSI')


#%%bag words işlemi için kullanılıyor
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

#bag of words
data_list=clean_data["scripts"].tolist()
cv1 = CountVectorizer(data_list,min_df=10)
x1=cv1.fit_transform(data_list).toarray()

#Bow Kelime sayılarını kelime kelime buldurduk
kelime_sayi1=x1.sum(axis=0).reshape(-1,1)
kelime_sayi_liste1=[]
for i in range(len(kelime_sayi1)):
    kelime_sayi_liste1.append(int(kelime_sayi1[i]))

kelimeler=cv1.vocabulary_
kelimeler=list(kelimeler.keys())
kelimeler=sorted(kelimeler)


"""
for i in range(len(deneme2)):
    deneme2.values()[i]=deneme[i]
"""
#tf idf
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(data_list,min_df=10)
x2 = tfidf.fit_transform(data_list).toarray()

#TF-IDF Kelime sayılarını kelime kelime buldurduk
kelime_sayi2=x2.sum(axis=0).reshape(-1,1)
kelime_sayi_liste2=[]
for i in range(len(kelime_sayi2)):
    kelime_sayi_liste2.append(float(kelime_sayi2[i]))

kelimeler=tfidf.vocabulary_
kelimeler=list(kelimeler.keys())
kelimeler=sorted(kelimeler)

dict_kelime_sayi = {'Kelimeler':kelimeler,'bow_KelimeSayisi':kelime_sayi_liste1,'tfidf_KelimeSayisi':kelime_sayi_liste2}
kelime_sayilari_df=pd.DataFrame(dict_kelime_sayi,columns=['Kelimeler','bow_KelimeSayisi','tfidf_KelimeSayisi'])
kelime_sayilari_df.to_csv(r'.\Kelime_Sayilari.csv',index=False)

#%% PCA ile boyut azaltma
from sklearn.decomposition import PCA

#bow
pca = PCA(n_components=2,whiten=True)
pca.fit(x1)
x1_pca=pca.transform(x1) 

data_x1=pd.DataFrame(x1_pca,columns=["x","y"])
plt.figure(1)
plt.scatter(data_x1.x,data_x1.y)
plt.xlabel("X Değerleri (PCA)")
plt.ylabel("Y Değerleri (PCA)")
plt.title("Kelime Torbası (Bag of Words (BoW))")
plt.show()

#tf-idf
pca = PCA(n_components=2,whiten=True)
pca.fit(x2)
x2_pca=pca.transform(x2) 

data_x2=pd.DataFrame(x2_pca,columns=["x","y"])
plt.figure(2)
plt.scatter(data_x2.x,data_x2.y)
plt.xlabel("X Değerleri (PCA)")
plt.ylabel("Y Değerleri (PCA)")
plt.title("Terim Sıklığı - Ters Belge Sıklığı (TF-IDF)")
plt.show()

#%% k-Means metrik bulma
from sklearn.cluster import KMeans

#Bag of Words
wcss1=[]
for k in range(1,15):
    k_means=KMeans(n_clusters=k, init = 'k-means++', random_state = 42)
    k_means.fit_transform(x1_pca)
    wcss1.append(k_means.inertia_)

plt.figure(3)
plt.plot(range(1,15),wcss1,color='red',label="Kelime torbası (Bag of Words (BoW))")
plt.xlabel("K Değerleri")
plt.ylabel("WCSS Değerleri")
plt.title("Bölmemiz gereken Küme sayısının tespiti için")
plt.suptitle("WCSS Tablosu")

plt.show()

#tf-idf
wcss3=[]
for k in range(1,15):
    k_means=KMeans(n_clusters=k, init = 'k-means++', random_state = 42)
    k_means.fit_transform(x2_pca)
    wcss3.append(k_means.inertia_)

plt.figure(3)
plt.plot(range(1,15),wcss3,color="green",label="Terim Sıklığı - Ters Belge Sıklığı (TF-IDF)")
plt.legend(loc='upper right')
plt.show()





