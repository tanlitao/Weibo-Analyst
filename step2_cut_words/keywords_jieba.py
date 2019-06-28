#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:51:48 2017
@author: Ming JIN
"""
from jieba import analyse

tfidf = analyse.extract_tags

fo = fo = open("data_keywords.dat", "w", encoding='utf-8')
fo.close()

for line in open("data_full.dat", encoding='utf-8'):
    
    text = line

    keywords = tfidf(text,allowPOS=('ns','nr','nt','nz','nl','n', 'vn','vd','vg','v','vf','a','an','i'))

    result=[]

    for keyword in keywords:
        
        result.append(keyword)

    #print(result)
    fo = open("data_keywords.dat", "a+", encoding='utf-8')

    for j in result:
          
        fo.write(j)
        fo.write(' ')
     
    fo.write('\n')
    fo.close()

print("Keywords Extraction Done!")


