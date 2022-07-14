# Imports
from ast import Try
import os
from pathlib import Path
import subprocess, sys
import shutil
from turtle import home
from dataclasses import replace

#Variables
name = input("Enter User's first and last name here:")
name2 = name.replace(" ", ".").lower()
title = input("Enter user's title:")
office = int(input("Select user's office \n 1) Phoenix \n 2) Boise \n 3) San Diego \n 4) Irvine \n 5) San Jose \n 6) Salt Lake City \n 7) Denver \n 8) Orlando \n 9) Honolulu Hawaii \n 10) Kauai/Lihue Hawaii \n 11) Nashville \n Select Answer here: "))
teamsnumber= input("Enter user's Teams Number in this format: xxx.xxx.xxxx:")
cellnumber = input("Enter user's cell number in this format: xxx.xxx.xxxx:")

# Image Sources
slc_img = ("""<img id=example.jpg""")
irvine_img = ("""<img id=example.jpg""")
phoenix_img = ("""<img id=example.jpg""")
boise_img = ("""<img id=example.jpg""")
denver_img = ("""<img id=example.jpg""")
san_diego_img = ("""<img id=example.jpg""")
san_jose_img= ("""<img id=example.jpg""")
orlando_img = ("""<img id=example.jpg""")
nashville_img = ("""<img id=example.jpg""")
hawaii_img = ("""<img id=example.jpg""")




#office variables
phoenix = ("example_address")
boise = ("example_address")
san_diego = ("example_address")
irvine = ("example_address")
san_jose = ("example_address")
slc = ("example_address")
denver = ("example_address")
orlando = ("example_address")
tennessee = ("example_address")
oahu_hawaii = ("example_address")
kauai_hawaii = ("example_address")

# Path Variables
global path
global path_2
path = ('template.html')
path_2 = ('/Users_Signatures/')

    
try:
    # Write Office Phoenix
    if office == 1:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", phoenix)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", phoenix_img)
                        new.write(line)
        
        

    

    # Write Office Boise
    elif office == 2:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", boise)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", boise_img)
                        new.write(line)


    # Write Office San Diego
    elif office == 3:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", san_diego)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", san_diego_img)
                        new.write(line)


    #Write Office irvine
    elif office == 4:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", irvine)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace('placeholder', irvine_img)
                        new.write(line)

    #Write Office San Jose
    elif office == 5: 
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", san_jose)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", san_jose_img)
                        new.write(line)

    # Write Office slc
    elif office ==6:
        path_2
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace("Office Address", slc)
                        line = line.replace("Title", title)
                        line = line.replace('Name', name)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace('placeholder', slc_img)
                        new.write(line)

    #Write Office denver
    elif office ==7:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", denver)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", denver_img)
                        new.write(line)

    #Write Office orlando
    elif office == 8:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", orlando)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", orlando_img)
                        new.write(line)

    #Write Office Honolulu 
    elif office == 9:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace("Office Address", oahu_hawaii)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", hawaii_img)
                        new.write(line)

    # Write office kauai Hawaii
    elif office == 10:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace('Office Address', kauai_hawaii)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", hawaii_img)
                        new.write(line)

    
    # Write office Nashville
    elif office == 11:
        with open('template.html', 'rt') as file:
                with open(name2 + "'s" + "_" + 'signature.htm', 'wt') as new:
                    for line in file:
                        line = line.replace('Name', name)
                        line = line.replace("Title", title)
                        line = line.replace('Office Address', tennessee)
                        line = line.replace("Teams Number", teamsnumber)
                        line = line.replace("Cell Number", cellnumber)
                        line = line.replace("placeholder", nashville_img)
                        new.write(line)

   
    print("Printing signature...")

except Exception as e:
    ("Could not Print SIgnature")
    print(e)



