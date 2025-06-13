import os
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')
import msvcrt
def getkey():
  return msvcrt.getch().decode('utf-8').lower()

Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m"

print("Welcome to Escape Room")
print(Blue + "By - Shakya")
print()
print(Green + "HOW TO PLAY:")
print('''
D: go right
A: go left
W: go forward
ENTER: go back

if something is interactable
a ">" will be there
''' + White)
print(White + "Press Enter to Start...")
input("> ")

clear()
import images


def room1():
  noKey = True
  dresserOpened = False
  doorClosed = True
  inventory = ""
  while doorClosed:
    print(images.middle)
    print(inventory)
    direction = getkey()
    clear()

    if direction == 'd':
      if dresserOpened:
        print(images.dresserOpened)
        print(inventory)
        getkey()
      else:
        while True:
          print(images.dresserClosed)
          print(inventory)
          code = input("> ").lower()
          clear()
          if code == 'lost':  # If lost is entered u get the key
            dresserOpened = True
            noKey = False
            inventory += images.keyItem
            print(images.dresserOpen)
            print(inventory)
            getkey()
            break
          elif not code:  # If no code is entered leave the room
            break

    elif direction == 'a':
      print(images.painting)
      print(inventory)
      getkey()

    elif direction == 'w':
      if noKey:
        print(images.doorClosed)
        print(inventory)
        getkey()
      else:
        print(images.doorClosed)
        print(inventory)
        input("> ")
        clear()
        print(images.doorOpen)
        input("> ")
        clear()
        print(images.complete)
        input("> ")
        clear()
        break
    clear()


room1()

# ------------------------------------------------------- Room 2 ---------------------------------------------------------------
import images2


def room2():
  hasKey = False
  hasWire = False
  lightOn = False
  lightFixed = False
  inventory = "\n"
  Complete = False
  while not Complete:
    print(images2.lightMiddle) if lightOn else print(images2.darkMiddle)
    print(inventory)
    direction = getkey()
    clear()
    if direction == 'd':
      while True:
        clear()
        print(images2.lightDresser) if lightOn else print(images2.darkDresser)
        print(inventory)
        choice = getkey()
        if choice == '1':
          clear()
          print(images2.lightDrawer1) if lightOn else print(
              images2.darkDrawer1)
          print(inventory)
          password = input('> ')
          clear()
          if password == '1936':
            (print(images2.lightOpenDrawer1) if lightOn else print(
                images2.darkOpenDrawer1)) if not hasKey else (
                    print(images2.lightOpenedDrawer1)
                    if lightOn else print(images2.darkOpenedDrawer1))
            print(inventory)
            if not hasKey:
              hasKey = True
              inventory = "|" + Orange + "O-.-" + White + "|" + inventory
            getkey()
        elif choice == '2':
          clear()
          (print(images2.lightOpenDrawer2) if lightOn else print(
              images2.darkOpenDrawer2)) if not hasWire else (
                  print(images2.lightOpenedDrawer2)
                  if lightOn else print(images2.darkOpenedDrawer2))
          print(inventory)
          if not hasWire:
            hasWire = True
            inventory = "|" + Red + "--" + White + "|"
          getkey()
        elif choice == '3':
          clear()
          print(images2.lightDrawer3) if lightOn else print(
              images2.darkDrawer3)
          print(inventory)
          getkey()
        else:
          break

    elif direction == 'a':
      print(images2.lightPainting) if lightOn else print(images2.darkPainting)
      print(inventory)
      getkey()

    elif direction == 'w':
      while True:
        clear()
        print(images2.lightDoorClosed) if lightOn else print(
            images2.darkDoorClosed)
        print(inventory)
        option = getkey()
        if option == '\n':
          break
        elif option == '1':
          if lightFixed:
            lightOn = not lightOn
          elif hasWire:
            lightFixed = True
            inventory = "\n"
        elif option == '2':
          if hasKey:
            clear()
            print(images2.lightDoorOpen) if lightOn else print(
                images2.darkDoorOpen)
            input("> ")
            Complete = True
            break

    clear()
  print(images.complete)
  input("> ")


# ------------------------------------------------------- Room 2 ---------------------------------------------------------------
import images3 as imgs


def room3():
  hasKey = False  # define objects in objects file and check using "if in" in the inventory
  hasHandle = False
  hasWireCutters = False
  lightOn = True
  fuseOn = True
  inventory = "\n"
  Complete = False
  while not Complete:
    print(imgs.lightMiddle) if lightOn else print(imgs.darkMiddle)
    print(inventory)
    direction = getkey()
    clear()
    if direction == 'd':  # ==========DRESSER==========
      while True:
        clear()
        print(imgs.lightDresser) if lightOn else print(imgs.darkDresser)
        print(inventory)
        choice = getkey()
        if choice == '1':
          clear()
          print(imgs.lightDrawer1) if lightOn else print(imgs.darkDrawer1)
          print(inventory)
          password = input('> ').upper()
          clear()
          if password == 'JULY':
            (print(imgs.lightOpenDrawer1)
             if lightOn else print(imgs.darkOpenDrawer1)) if not hasKey else (
                 print(imgs.lightOpenedDrawer1)
                 if lightOn else print(imgs.darkOpenedDrawer1))
            print(inventory)
            if not hasKey:
              hasKey = True
              inventory = imgs.key + inventory
            getkey()
        elif choice == '2':
          clear()
          print(imgs.lightDrawer2) if lightOn else print(imgs.darkDrawer2)
          print(inventory)
          getkey()
        elif choice == '3':
          clear()
          (print(imgs.lightOpenDrawer3) if lightOn else print(
              imgs.darkOpenDrawer3)) if not hasWireCutters else (
                  print(imgs.lightOpenedDrawer3)
                  if lightOn else print(imgs.darkOpenedDrawer3))
          print(inventory)
          if not hasWireCutters:
            hasWireCutters = True
            inventory += imgs.wireCutters
          getkey()

        else:
          break

    elif direction == 'a':  # ==========LEFT SIDE==========
      while True:
        clear()
        print(imgs.lightLeftSide) if lightOn else print(imgs.darkLeftSide)
        print(inventory)
        choice = getkey()
        if choice == '1':
          clear()
          print(imgs.lightPic) if lightOn else print(imgs.darkPic)
          print(inventory)
          getkey()
        elif choice == '2':
          clear()
          if imgs.handle in inventory:
            print(imgs.FuseBox)
          else:
            print(imgs.lightFuseNoHandle) if lightOn else print(
                imgs.darkFuseNoHandle)
            getkey()
        elif choice == '\n':
          break

    elif direction == 'w':  # ==========Door and Switch==========
      while True:
        clear()
        print(imgs.lightDoorClosed) if lightOn else print(imgs.darkDoorClosed)
        print(inventory)
        option = getkey()
        if option == '\n':
          break
        elif option == '1':
          if fuseOn:
            lightOn = not lightOn
        elif option == '2':
          if hasKey and not fuseOn:
            clear()
            print(images2.lightDoorOpen) if lightOn else print(
                images2.darkDoorOpen)
            input("> ")
            Complete = True
            break
        elif option == '3':
          if fuseOn:
            clear()
            print(imgs.lightKeypad) if lightOn else print(imgs.darkKeypad)
            input("> ")

    clear()
  print(images.complete)
  input("> ")


room2()
room3()