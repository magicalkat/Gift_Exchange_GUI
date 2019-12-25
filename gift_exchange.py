# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:22:16 2019

@author: yyhlabkate
"""
import random as rd

def check_same_giver_receiver(giver,receiver):
    for i in range(len(giver)):
#        print ("check_func")
        if giver[i]==receiver[i]:
            x=receiver[i]
            cal=giver.copy()
            del cal[i]
            rd_num=rd.choice(cal)
            receiver[i]=receiver[rd_num-1]
            receiver[rd_num-1]=x
            return check_same_giver_receiver(giver,receiver)
    return giver,receiver

def gift_exchange(num_of_people):
    giver=list(range(1,int(num_of_people)+1))
    receiver=giver.copy()
    rd.shuffle(receiver)
    check_same_giver_receiver(giver,receiver)  
    return giver,receiver

#def draw(num_of_people, draw_times):
#    for i in range(int(draw_times)):
#        giver,receiver=gift_exchange(num_of_people)
#    for i in range(len(giver)):
#        print(str(giver[i])+" to "+str(receiver[i]))
        
#draw(20,100)