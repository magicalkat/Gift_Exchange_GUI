# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 13:57:31 2019

@author: yyhlabkate
"""

import tkinter as tk
import gift_exchange as ge

#Main calculation
def draw():
    num_of_people = people_num_entry.get()
    draw_times = regenerating_time_entry.get()
    for i in range(int(draw_times)):
        giver,receiver=ge.gift_exchange(num_of_people)
    for i in range(len(giver)):
        char=str(giver[i])+"\tto\t"+str(receiver[i])+"\n"
        text.insert('insert',char)


#Build the Window
window = tk.Tk()
top_frame = tk.Frame(window)

#Setting Window properties
window.title('Gift Exchange')
window.geometry('800x600')
window.configure(background='white')

#For header in the window
header_label = tk.Label(window, text='交換禮物生成器')
header_label.pack()

#For Parameters:People number group 
people_num_frame = tk.Frame(window)
people_num_frame.pack(side=tk.TOP)
#Title of People number
people_num = tk.Label(people_num_frame, text='人數')
people_num.pack(side=tk.LEFT)
#Entry frame for People number
people_num_entry = tk.Entry(people_num_frame)
people_num_entry.pack(side=tk.LEFT)

#For Parameters:Re-generating time
regenerating_time_frame = tk.Frame(window)
regenerating_time_frame.pack(side=tk.TOP)
#Title of People number
regenerating_time = tk.Label(regenerating_time_frame, text='重抽次數')
regenerating_time.pack(side=tk.LEFT)
#Entry frame for People number
regenerating_time_entry = tk.Entry(regenerating_time_frame)
regenerating_time_entry.pack(side=tk.LEFT)

#For botton generating name list
#generate_btn = tk.Button(window, text='生成交換名單')
generate_btn = tk.Button(window, text='生成交換名單',
                         command=draw)
generate_btn.pack()

#For text window
text=tk.Text(window, height=20)
text.pack()


#Operating the window
window.mainloop()