#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Filename : getRepls.py
#  Author   : Rajesh Pandian M | mrpaj@gmail.com |  @mrprajesh
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
# ~ v0.3 Wed, 16-Jun-2021, 00:48:02 IST
# ~ * Feature to generate rollnums
# ~ * Given a prefixBatch and totalOnRoll
# ~ * feature for dryRun while testing
#
# ~ v0.2 - Tue, 15-Jun-2021, 11:27:42 IST
# ~ * Opens chrome tab
# ~ * checks OS and opens it accordingly
#
# ~ v0.1 - Tue, 14-Jun-2021, 21:29:12 IST
# ~ * Basic Module to open tab done


# SAMPLE URL
#~https://replit.com/@LambdaCS1111/SoloCoding2Princes-Quest-cs20b087.zip

projectName = "SoloCoding2Princes-Quest"
teamsList = ['AlphaCS1111', 'BetaCS1111', 'GammaCS1111', 'DeltaCS1111', 'EpsilonCS1111', 'ZetaCS1111', 'EtaCS1111', 'ThetaCS1111', 'IotaCS1111', 'KappaCS1111', 'LambdaCS1111']

## EDIT below only for auto-generate roll numbers
totalOnRoll = 87
prefixBatch = "cs20b"
rollNos     = []
# ~ For testing purpose only
# ~ ===========================
# ~ rollNos     = [ "cs20b001" ] #single number
dryRun      = False

## CS1111 - 2021  - Do NOT edit below!
rollNos = [ "cs20b001", "cs20b002", "cs20b003", "cs20b004", "cs20b005", "cs20b006", "CS20B007", "cs20b008", "cs20b009", "cs20b010", "cs20b011", "cs20b012", "cs20b013", "cs20b014", "cs20b015", "cs20b016", "cs20b017", "cs20b018", "cs20b019", "CS20B020", "cs20b021", "cs20b022", "cs20b023", "cs20b024", "cs20b025", "cs20b026", "CS20B027", "cs20b028", "cs20b029", "cs20b030", "cs20b031", "cs20b032", "cs20b033", "cs20b034", "cs20b035", "cs20b036", "cs20b037", "cs20b038", "cs20b039", "Cs20b040", "cs20b041", "cs20b042", "cs20b043", "cs20b044", "cs20b045", "cs20b046", "cs20b047", "cs20b048", "cs20b049", "cs20b050", "cs20b051", "CS20B052", "cs20b053", "CS20B054", "cs20b055", "CS20B056", "cs20b057", "cs20b058", "cs20b059", "cs20b060", "cs20b061", "CS20B062", "cs20b063", "cs20b064", "cs20b065", "cs20b066", "cs20b067", "cs20b068", "cs20b069", "cs20b070", "cs20b071", "cs20b072", "cs20b073", "cs20b074", "cs20b075", "cs20b076", "cs20b077", "cs20b078", "CS20B079", "cs20b080", "cs20b081", "cs20b082", "cs20b083", "cs20b084", "cs20b085", "cs20b086", "cs20b087" ]
# ~ 7 C Capsed
# ~ 20,27,52,54,56,62,79 CSB Capsed
# seq -f "cs20b%03g" 87 #shell trick



def getRollNumbers(number):
  List = []
  for i in range(number):
    List.append( prefixBatch + "%03d" % (i+1))
  return List

def main(args):
  global dryRun;
  global rollNos;

  import webbrowser
  import time #sleep
  import platform #for os info

  import os
  from os import path #for path.exists

  chromePath = ""

  if not rollNos and totalOnRoll > 0: # if list is empty generate
    print(f"Generating..\nTotal rollNums: {totalOnRoll} Using prefix: {prefixBatch}")
    rollNos = getRollNumbers(totalOnRoll)

  for i in range(len(rollNos)):
    teamName = teamsList[i//8] # + "CS1111"
    rollNum  = rollNos[i]
    url = f"https://replit.com/@{teamName}/{projectName}-{rollNum}.zip"
    #~https://replit.com/@LambdaCS1111/SoloCoding2Princes-Quest-cs20b087.zip

    # ~ if(i%8 == 0):
      # ~ time.sleep(2)

    osType = platform.system().upper()
    if osType == "LINUX" :
      chromePath = "/usr/bin/google-chrome"
    elif osType == "WINDOWS" :
      chromePath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s" # assuming default install location
    elif osType == "DARWIN" :
      chromePath = "/usr/bin/google-chrome" ## //TODO find out

    if not dryRun:
      if path.exists(chromePath) :
        webbrowser.get(chromePath).open(url)
      else :
        webbrowser.open_new_tab(url) #default browser tab
    print(rollNum + " - Done")

  return 0

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
