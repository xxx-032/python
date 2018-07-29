#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-28 16:57:57
# @Author  : cmj (451939499@qq.com)
# @Link    : http://example.org
# @Version : simplecal1.0

import tkinter
import os
import re
import math
from tkinter import *
reset = False

#绑定鼠标左击事件
def buttonCallback(event):
	global label
	global reset
	choose = event.widget['text']
	if choose == "C":
		label['text'] = "0"
		return

	if choose == "√":
		re_num = re.compile("^[0-9.]*$")
		if re_num.findall(label['text']):
			label['text'] = str(math.sqrt((float(label['text']))))
		else:
			label['text'] = "0"
		return

	if choose == "1/x":
		re_num = re.compile("^[0-9.]*$")
		if re_num.findall(label['text']):
			label['text'] = str(1/(float(label['text'])))
		else:
			label['text'] = "0"
		return

	if choose == "=":
		#eval(expression, globals=None, locals=None) 将字符串str当成有效的表达式来求值并返回计算结果
		try:
			label['text'] = str(eval(label['text']))
		except:
			label['text'] = "0"
		reset = True
		return

	if choose == "←":
		label['text'] = label['text'][:len(label['text'])-1]
		if label['text'] == "":
			label['text'] = "0"
		return 

	current = label['text']

	if current == "0" or reset is True:
		current = ""
		reset = False

	label['text']= current + choose



col = 400
row = 400
mywidth = 75
myheight = 70
calc = tkinter.Tk() 
calc.title("计算器")
calc.minsize(col,row)
calc.maxsize(col,row)
label = tkinter.Label(calc,text = "0",bg = 'white',anchor = 'e',font = ("Arial",15))
label.place(x=10,y=10,width=col- 20,height=40)

showText = "789/456*123-0.C+"
showcolText = "√±"
showrowText = "()"
for i in range(4):
	for j in range(4):
		b = Button(master = calc,text = showText[i*4+j],width = 9,height = 2)
		b.place(x = 10 +mywidth*j,y =70 + myheight*i)
		b.bind("<Button-1>",buttonCallback) #<Button->1左击  2滑轮 3右击

for i in range(2):
	b = Button(master = calc,text = showrowText[i],width = 9,height = 2)
	b.place(x = 10 +mywidth*i,y =70 + myheight*4)
	b.bind("<Button-1>",buttonCallback)

for i in range(2):
	b = Button(master = calc,text = showcolText[i],width = 9,height = 2)
	b.place(x = 10 + mywidth*4,y =70 + myheight*i)
	b.bind("<Button-1>",buttonCallback)

b = Button(master = calc,text = "1/x",width = 9,height = 2)
b.place(x = 10 +mywidth*2,y =70 + myheight*4,width = 2*mywidth)
b.bind("<Button-1>",buttonCallback)

b = Button(master = calc,text = "←",width = 9,height = 2)
b.place(x = 10 + mywidth*4,y =70 + myheight*2)
b.bind("<Button-1>",buttonCallback)

b = Button(master = calc,text = "=",width = 9,height = 2)
b.place(x = 10 + mywidth*4,y =70 + myheight*3,height=117)
b.bind("<Button-1>",buttonCallback)


calc.mainloop()