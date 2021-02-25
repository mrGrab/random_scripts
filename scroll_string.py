#!/usr/bin/env python3

import sys
from time import sleep

def scroll(text, delay=0.5):
	lst_text = list(text)
	line = ""
	temp = [""] *10
	for i in range(len(lst_text)):
		sleep(delay)
		temp.append(lst_text[i])
		temp.pop(0)
		print("| {:>10} |".format(line.join(temp)), end="\r")

line = input('Enter some text: ');
scroll(line)
