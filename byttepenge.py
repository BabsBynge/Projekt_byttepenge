# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 08:08:31 2021

@author: madsl
"""

#nedenstående variabler skal have en billedeværdi når færdig
Ikr = 1
IIkr = 2
Vkr = 5
Xkr = 10
Lkr = 50
Ckr = 100
CCkr = 200
Dkr = 500
Mkr = 1000


def difference(a, b):
    c = a - b
    return c


def pay_back(a):
    int(a)
    if a >= 1000:
        x = a // 1000
        for i in range (x):
            print("1000kr")
            a = a - Mkr  
            if 1000 > a >= 500:
                x = a // 500
                for i in range (x):
                    print("500kr")
                    a = a - Dkr
                    if 500 > a >= 200:
                        x = a // 200
                        for i in range (x):
                            print("200kr")
                            a = a - CCkr
                            if 200 > a >= 100:
                                x = a // 100
                                for i in range (x):
                                    print("100kr")
                                    a = a - Ckr
                                    if 100 > a >= 50:
                                        x = a // 50
                                        for i in range (x):
                                            print("50kr")
                                            a = a - Lkr
                                            if 50 > a >= 10:
                                                x = a // 10
                                                for i in range (x):
                                                    print("10kr")
                                                    a = a - Xkr
                                                    if 10 > a >= 5:
                                                        x = a // 5
                                                        for i in range (x):
                                                            print("5kr")
                                                            a = a - Vkr
                                                            if 5 > a >= 2:
                                                                x = a // 2
                                                                for i in range (x):
                                                                    print("2kr")
                                                                    a = a - IIkr
                                                                    if 2 > a >= 1:
                                                                        x = a // 1
                                                                        for i in range (x):
                                                                            print("1kr")
                                                                            a = a - Ikr
                                                            elif 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr    
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr   
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr     
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr      
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr                       
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr          
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr 
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr   
                            elif 100 > a >= 50:
                                x = a // 50
                                for i in range (x):
                                    print("50kr")
                                    a = a - Lkr
                                    if 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr      
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr                       
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr          
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr 
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                                            
                    elif 200 > a >= 100:
                        x = a // 100
                        for i in range (x):
                            print("100kr")
                            a = a - Ckr
                            if 100 > a >= 50:
                                x = a // 50
                                for i in range (x):
                                    print("50kr")
                                    a = a - Lkr
                                    if 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr      
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr                       
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr          
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr 
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 500 > a >= 200:
                x = a // 200
                for i in range (x):
                    print("200kr")
                    a = a - CCkr
                    if 200 > a >= 100:
                        x = a // 100
                        for i in range (x):
                            print("100kr")
                            a = a - Ckr
                            if 100 > a >= 50:
                                x = a // 50
                                for i in range (x):
                                    print("50kr")
                                    a = a - Lkr
                                    if 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr      
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr                       
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr          
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr 
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 200 > a >= 100:
                        x = a // 100
                        for i in range (x):
                            print("100kr")
                            a = a - Ckr
                            if 100 > a >= 50:
                                x = a // 50
                                for i in range (x):
                                    print("50kr")
                                    a = a - Lkr
                                    if 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr      
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr                       
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr          
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr 
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr                
                    elif 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 200 > a >= 100:
                x = a // 100
                for i in range (x):
                    print("100kr")
                    a = a - Ckr
                    if 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
                                       
                                
            elif 100 > a >= 50:
                x = a // 50
                for i in range (x):
                    print("50kr")
                    a = a - Lkr
                    if 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr                
                    elif 10 > a >= 5:
                         x = a // 5
                         for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                           print("1kr")
                                           a = a - Ikr 
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr  
            elif 20 > a >= 10:
                x = a // 10
                for i in range (x):
                    print("10kr")
                    a = a - Xkr
                    if 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                           print("1kr")
                                           a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 5 > a >= 2:
                           x = a // 2
                           for i in range (x):
                               print("2kr")
                               a = a - IIkr
                               if 2 > a >= 1:
                                    x = a // 1
                                    for i in range (x):
                                        print("1kr")
                                        a = a - Ikr
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
                    
            elif 10 > a >= 5:
                x = a // 5
                for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
                    
            elif 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
                            
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
            
    elif 1000 > a >= 500:
        x = a // 500
        for i in range (x):
            print("500kr")
            a = a - Dkr
            if 500 > a >= 200:
                x = a // 200
                for i in range (x):
                    print("200kr")
                    a = a - CCkr
                    if 200 > a >= 100:
                        x = a // 100
                        for i in range (x):
                            print("100kr")
                            a = a - Ckr
                            if 100 > a >= 50:
                                x = a // 50
                                for i in range (x):
                                    print("50kr")
                                    a = a - Lkr
                                    if 50 > a >= 10:
                                        x = a // 10
                                        for i in range (x):
                                            print("10kr")
                                            a = a - Xkr
                                            if 10 > a >= 5:
                                                x = a // 5
                                                for i in range (x):
                                                    print("5kr")
                                                    a = a - Vkr
                                                    if 5 > a >= 2:
                                                        x = a // 2
                                                        for i in range (x):
                                                            print("2kr")
                                                            a = a - IIkr
                                                            if 2 > a >= 1:
                                                                x = a // 1
                                                                for i in range (x):
                                                                    print("1kr")
                                                                    a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr    
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr   
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr     
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 50 > a >= 10:
                                 x = a // 10
                                 for i in range (x):
                                     print("10kr")
                                     a = a - Xkr
                                     if 10 > a >= 5:
                                         x = a // 5
                                         for i in range (x):
                                             print("5kr")
                                             a = a - Vkr
                                             if 5 > a >= 2:
                                                 x = a // 2
                                                 for i in range (x):
                                                     print("2kr")
                                                     a = a - IIkr
                                                     if 2 > a >= 1:
                                                         x = a // 1
                                                         for i in range (x):
                                                             print("1kr")
                                                             a = a - Ikr
                                             elif 2 > a >= 1:
                                                 x = a // 1
                                                 for i in range (x):
                                                     print("1kr")
                                                     a = a - Ikr
                                     elif 5 > a >= 2:
                                         x = a // 2
                                         for i in range (x):
                                             print("2kr")
                                             a = a - IIkr
                                             if 2 > a >= 1:
                                                 x = a // 1
                                                 for i in range (x):
                                                     print("1kr")
                                                     a = a - Ikr    
                                     elif 2 > a >= 1:
                                         x = a // 1
                                         for i in range (x):
                                             print("1kr")
                                             a = a - Ikr      
                            elif 10 > a >= 5:
                                 x = a // 5
                                 for i in range (x):
                                     print("5kr")
                                     a = a - Vkr
                                     if 5 > a >= 2:
                                         x = a // 2
                                         for i in range (x):
                                             print("2kr")
                                             a = a - IIkr
                                             if 2 > a >= 1:
                                                 x = a // 1
                                                 for i in range (x):
                                                     print("1kr")
                                                     a = a - Ikr                       
                                     elif 2 > a >= 1:
                                         x = a // 1
                                         for i in range (x):
                                             print("1kr")
                                             a = a - Ikr          
                            elif 5 > a >= 2:
                                 x = a // 2
                                 for i in range (x):
                                     print("2kr")
                                     a = a - IIkr
                                     if 2 > a >= 1:
                                         x = a // 1
                                         for i in range (x):
                                             print("1kr")
                                             a = a - Ikr 
                            elif 2 > a >= 1:
                                 x = a // 1
                                 for i in range (x):
                                     print("1kr")
                                     a = a - Ikr     
                    elif 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                            elif 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr                 
            elif 200 > a >= 100:
                x = a // 100
                for i in range (x):
                    print("100kr")
                    a = a - Ckr
                    if 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 100 > a >= 50:
                x = a // 50
                for i in range (x):
                    print("50kr")
                    a = a - Lkr
                    if 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 50 > a >= 10:
                x = a // 10
                for i in range (x):
                    print("10kr")
                    a = a - Xkr
                    if 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr    
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr      
            elif 10 > a >= 5:
                x = a // 5
                for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr                       
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr          
            elif 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr                               
                                            
    elif 500 > a >= 200:
        x = a // 200
        for i in range (x):
            print("200kr")
            a = a - CCkr
            if 200 > a >= 100:
                x = a // 100
                for i in range (x):
                    print("100kr")
                    a = a - Ckr
                    if 100 > a >= 50:
                        x = a // 50
                        for i in range (x):
                            print("50kr")
                            a = a - Lkr
                            if 50 > a >= 10:
                                x = a // 10
                                for i in range (x):
                                    print("10kr")
                                    a = a - Xkr
                                    if 10 > a >= 5:
                                        x = a // 5
                                        for i in range (x):
                                            print("5kr")
                                            a = a - Vkr
                                            if 5 > a >= 2:
                                                x = a // 2
                                                for i in range (x):
                                                    print("2kr")
                                                    a = a - IIkr
                                                    if 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                                    elif 2 > a >= 1:
                                                        x = a // 1
                                                        for i in range (x):
                                                            print("1kr")
                                                            a = a - Ikr
                                    elif 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr    
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr      
                            elif 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr                       
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr          
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr 
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 100 > a >= 50:
                x = a // 50
                for i in range (x):
                    print("50kr")
                    a = a - Lkr
                    if 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 50 > a >= 10:
                x = a // 10
                for i in range (x):
                    print("10kr")
                    a = a - Xkr
                    if 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr    
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr      
            elif 10 > a >= 5:
                x = a // 5
                for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr                       
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr          
            elif 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
            
    elif 200 > a >= 100:
        x = a // 100
        for i in range (x):
            print("100kr")
            a = a - Ckr
            if 100 > a >= 50:
                x = a // 50
                for i in range (x):
                    print("50kr")
                    a = a - Lkr
                    if 50 > a >= 10:
                        x = a // 10
                        for i in range (x):
                            print("10kr")
                            a = a - Xkr
                            if 10 > a >= 5:
                                x = a // 5
                                for i in range (x):
                                    print("5kr")
                                    a = a - Vkr
                                    if 5 > a >= 2:
                                        x = a // 2
                                        for i in range (x):
                                            print("2kr")
                                            a = a - IIkr
                                            if 2 > a >= 1:
                                                x = a // 1
                                                for i in range (x):
                                                    print("1kr")
                                                    a = a - Ikr
                                    elif 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr    
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr      
                    elif 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr                       
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr          
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr 
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 50 > a >= 10:
                x = a // 10
                for i in range (x):
                    print("10kr")
                    a = a - Xkr
                    if 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr    
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr      
            elif 10 > a >= 5:
                x = a // 5
                for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr                       
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr          
            elif 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr 
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
                                   
                            
    elif 100 > a >= 50:
        x = a // 50
        for i in range (x):
            print("50kr")
            a = a - Lkr
            if 50 > a >= 10:
                x = a // 10
                for i in range (x):
                    print("10kr")
                    a = a - Xkr
                    if 10 > a >= 5:
                        x = a // 5
                        for i in range (x):
                            print("5kr")
                            a = a - Vkr
                            if 5 > a >= 2:
                                x = a // 2
                                for i in range (x):
                                    print("2kr")
                                    a = a - IIkr
                                    if 2 > a >= 1:
                                        x = a // 1
                                        for i in range (x):
                                            print("1kr")
                                            a = a - Ikr
                            elif 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                    print("1kr")
                                    a = a - Ikr
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr                
            elif 10 > a >= 5:
                 x = a // 5
                 for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                   print("1kr")
                                   a = a - Ikr 
            elif 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr  

    elif 20 > a >= 10:
        x = a // 10
        for i in range (x):
            print("10kr")
            a = a - Xkr
            if 10 > a >= 5:
                x = a // 5
                for i in range (x):
                    print("5kr")
                    a = a - Vkr
                    if 5 > a >= 2:
                        x = a // 2
                        for i in range (x):
                            print("2kr")
                            a = a - IIkr
                            if 2 > a >= 1:
                                x = a // 1
                                for i in range (x):
                                   print("1kr")
                                   a = a - Ikr
                    elif 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
                            a = a - Ikr
            elif 5 > a >= 2:
                   x = a // 2
                   for i in range (x):
                       print("2kr")
                       a = a - IIkr
                       if 2 > a >= 1:
                            x = a // 1
                            for i in range (x):
                                print("1kr")
                                a = a - Ikr
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
            
    elif 10 > a >= 5:
        x = a // 5
        for i in range (x):
            print("5kr")
            a = a - Vkr
            if 5 > a >= 2:
                x = a // 2
                for i in range (x):
                    print("2kr")
                    a = a - IIkr
                    if 2 > a >= 1:
                        x = a // 1
                        for i in range (x):
                            print("1kr")
            elif 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
            
    elif 5 > a >= 2:
        x = a // 2
        for i in range (x):
            print("2kr")
            a = a - IIkr
            if 2 > a >= 1:
                x = a // 1
                for i in range (x):
                    print("1kr")
                    a = a - Ikr
                    
    elif 2 > a >= 1:
        x = a // 1
        for i in range (x):
            print("1kr")
            a = a - Ikr

        
#hvad skal  de betale?
pay = int(input("at betale: "))

#hvad betaler de med?
cos_pay = int(input("betalt: "))

print("skal have",(difference(cos_pay, pay)),"tilbage")

print(pay_back(difference(cos_pay, pay)))



#for a in 1kr:
#    print("1kr")
#    a = a -  1kr