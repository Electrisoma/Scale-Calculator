"""
Template Major Key Signature Calculator - Calculates a major key signature by how many flats it has
"""

scalename = 'Template'
print("Source scale: " + scalename)

import sys
sys.path.append("utils")
import math
from collections import deque
from calcutils import scaleA
from calcutils import scaleB
from calcutils import invalid
from calcutils import colors


print(f"{colors.Y}select scale{colors.END}") #scales and modes
print(f"{colors.LG}1.Mode 1{colors.END}")
print(f"{colors.LG}2.Mode 2{colors.END}")
print(f"{colors.LG}3.Mode 3{colors.END}")
print(f"{colors.LG}4.Mode 4{colors.END}")
print(f"{colors.LG}5.Mode 5{colors.END}")
print(f"{colors.LG}6.Mode 6{colors.END}")
print(f"{colors.LG}7.Mode 7{colors.END}")
scale = scaleA
while True:
  choice = input(f"{colors.LP}>Enter scale: {colors.END}")
  firstPrompt = input(f"{colors.R}>Sharps or flats(1/2): {colors.END}")
  if firstPrompt in ['1','2']:
    if firstPrompt == '1':
      scale = scaleA
    elif firstPrompt == '2':
      scale = scaleB 
  if choice in ['1','2','3','4','5','6','7']:
      try:
        if choice == '1':
          print(f"{colors.LG}{colors.BOLD}>>Mode 1{colors.END}")
        if choice == '2':
          print(f"{colors.LG}{colors.BOLD}>>Mode 2{colors.END}")
        if choice == '3':
          print(f"{colors.LG}{colors.BOLD}>>Mode 3{colors.END}")
        if choice == '4':
          print(f"{colors.LG}{colors.BOLD}>>Mode 4{colors.END}")
        if choice == '5':
          print(f"{colors.LG}{colors.BOLD}>>Mode 5{colors.END}")
        if choice == '6':
          print(f"{colors.LG}{colors.BOLD}>>Mode 6{colors.END}")
        if choice == '7':
          print(f"{colors.LG}{colors.BOLD}>>Mode 7{colors.END}")
        if firstPrompt == '1':
          inp = int(input(f"{colors.R}>Enter number of sharps(>1): {colors.END}"))
        elif firstPrompt == '2':
          inp = int(input(f"{colors.R}>Enter number of flats: {colors.END}"))
        else:
          inp = 1
        if inp & 1: #circle of fifths calculator
          flats = int(inp) * 4
        else:
          flats = int(inp) - 1 * 3
      except ValueError:
           print(invalid)
           continue
      if choice == '1': #major
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats)
          newscale = list(scaleshifter)
          newscale.pop(-4)
          newscale.pop(1)
          newscale.pop(2)
          newscale.pop(4)
          newscale.pop(6)
          return newscale        
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Major" + f"{colors.END}")
      elif choice == '2': #dorian
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-2)
          newscale = list(scaleshifter)
          newscale.pop(-1)
          newscale.pop(1)
          newscale.pop(3)
          newscale.pop(4)
          newscale.pop(5)
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Dorian" + f"{colors.END}")
      elif choice == '3': #phrygian
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-3)
          newscale = list(scaleshifter)
          newscale.pop(-2)
          newscale.pop(0)
          newscale.pop(2)
          newscale.pop(3)
          newscale.pop(4)
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Phrygian" + f"{colors.END}")
      elif choice == '4': #lydian
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-5)
          newscale = list(scaleshifter)
          newscale.pop(-2)
          newscale.pop(1)
          newscale.pop(2)
          newscale.pop(3)
          newscale.pop(5)        
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Lydian" + f"{colors.END}")
      elif choice == '5': #mixolydian
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-6)
          newscale = list(scaleshifter)
          newscale.pop(0)
          newscale.pop(1)
          newscale.pop(2)
          newscale.pop(4)
          newscale.pop(5)
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Mixolydian" + f"{colors.END}")       
      elif choice == '6': #minor
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-8)
          newscale = list(scaleshifter)
          newscale.pop(0)
          newscale.pop(1)
          newscale.pop(3)
          newscale.pop(4)            
          newscale.pop(6)
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Minor" + f"{colors.END}")         
      elif choice == '7': #locrian
        def shiftscale(scale,flats):
          scaleshifter = deque(scale)
          scaleshifter.rotate(flats-10)
          newscale = list(scaleshifter)
          newscale.pop(-2)
          newscale.pop(0)
          newscale.pop(2)
          newscale.pop(3)            
          newscale.pop(5)
          return newscale 
        print(f"{colors.Y}" + str(shiftscale(scale,flats)) + f"{colors.END}")
        print(f"{colors.LG}" + shiftscale(scale,flats)[0] + " " + "Locrian" + f"{colors.END}") 
  else:
    print(invalid)