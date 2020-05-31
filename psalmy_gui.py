#!/usr/bin/env python
#coding=utf-8
import easygui, sys
def buduj_psalmy():
    psalmy = open('psalmy.txt', 'r')
    psalmylist = psalmy.readlines()
    for psalm in psalmylist:
        plik = psalm
        for znak in [',','.','\n']:
            plik = plik.replace(znak,'')
        plikurl = "refreny_psalmow/" + plik
        print(plik)
        plikobj = open(plikurl, 'w')
        psalm = psalm.replace('\n','')
        plikobj.write("""
<?xml version="1.0" encoding="UTF-8"?>
<song>
  <title>%s</title>
  <author></author>
  <copyright></copyright>
  <hymn_number></hymn_number>
  <presentation></presentation>
  <ccli></ccli>
  <capo print="false"></capo>
  <key></key>
  <aka></aka>
  <key_line></key_line>
  <user1></user1>
  <user2></user2>
  <user3></user3>
  <theme></theme>
  <tempo></tempo>
  <time_sig></time_sig>
  <lyrics>
 %s
</lyrics></song>
        """%(plik,psalm))
        plikobj.close()
    psalmy.close()

#buduj_psalmy()

msg = "Czy chcesz zbudować bazę refrenów psalmów? Pliki znajdziesz w podfolderze refreny_psalmow/ ."
title = "Psalmy"
y_button = "Tak"
if easygui.ynbox(msg, title):
    buduj_psalmy()
else:
    sys.exit(0)
