#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  getDown.py
#  Author: Rajesh Pandian M | mrpaj@gmail.com |  @mrprajesh
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
# ~ v0.1 - Tue, 14-Jun-2021, 21:29:12 IST
# ~ * Basic Module to open tab done

projectName = "SoloCoding2Princes-Quest"



# ~ For testing purpose only
# ~ ===========================
rollNos     = [ "cs20b001" ] #single number
dryRun      = False

## CS1111 - 2021  - Do NOT edit below!
# ~ rollNos = [ "cs20b001", "cs20b002", "cs20b003", "cs20b004", "cs20b005", "cs20b006", "CS20B007", "cs20b008", "cs20b009", "cs20b010", "cs20b011", "cs20b012", "cs20b013", "cs20b014", "cs20b015", "cs20b016", "cs20b017", "cs20b018", "cs20b019", "CS20B020", "cs20b021", "cs20b022", "cs20b023", "cs20b024", "cs20b025", "cs20b026", "CS20B027", "cs20b028", "cs20b029", "cs20b030", "cs20b031", "cs20b032", "cs20b033", "cs20b034", "cs20b035", "cs20b036", "cs20b037", "cs20b038", "cs20b039", "Cs20b040", "cs20b041", "cs20b042", "cs20b043", "cs20b044", "cs20b045", "cs20b046", "cs20b047", "cs20b048", "cs20b049", "cs20b050", "cs20b051", "CS20B052", "cs20b053", "CS20B054", "cs20b055", "CS20B056", "cs20b057", "cs20b058", "cs20b059", "cs20b060", "cs20b061", "CS20B062", "cs20b063", "cs20b064", "cs20b065", "cs20b066", "cs20b067", "cs20b068", "cs20b069", "cs20b070", "cs20b071", "cs20b072", "cs20b073", "cs20b074", "cs20b075", "cs20b076", "cs20b077", "cs20b078", "CS20B079", "cs20b080", "cs20b081", "cs20b082", "cs20b083", "cs20b084", "cs20b085", "cs20b086", "cs20b087" ]
# ~ 7 C Capsed
# ~ 20,27,52,54,56,62,79 CSB Capsed
# seq -f "cs20b%03g" 87 #shell trick

teamsList = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda']


def main(args):

  import webbrowser
  import time #sleep
  import platform #for os info

  import os
  from os import path #for path.exists

  chromePath = "/usr/bin/google-chrome"


  for i in range(len(rollNos)):
    teamName = teamsList[i//8] + "CS1111"
    rollNum  = rollNos[i]
    url = f"https://replit.com/@{teamName}/{projectName}-{rollNum}.zip"
    #~https://replit.com/@LambdaCS1111/SoloCoding2Princes-Quest-cs20b087.zip

    # ~ if(i%8 == 0):
      # ~ time.sleep(2)
    webbrowser.get(chromePath).open(url)
    print(rollNum + " - Done")

  return 0

if __name__ == '__main__':
  import sys
  sys.exit(main(sys.argv))
