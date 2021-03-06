from utils import findAreas, generate, printMap
import os

def clear():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def main():
  quit = False
  isGenerated = False

  while not quit:
    clear()
    option = input("What do you want to do? \n1. Generate a map 1000x1000 \n2. Generate a map nxn \n3. Try with the example image \n4. Quit \n")
    
    if option == '1':
      newMap = generate()
      isGenerated = True

      while isGenerated:
        option = input("What do you want to do with the map? \n1. Find areas (Can generate more of 30000 results!) \n2. Print map \n3. Quit \n")
        if option == '1':
          areas = findAreas(newMap)
          print("Areas: ")
          for i in range(len(areas)):
            print(f"\t{i + 1}. {areas[i]} mt2")

          input("Press enter to continue...")  

        elif option == '2':
          printMap(newMap)
          input("Press enter to continue...")

        elif option == '3':
          isGenerated = False
          break

    elif option == '2':
      try: 
        size = int(input("Enter the size (greater than one) of the map: "))
        if size == 0 or size == 1:
          raise ValueError
      except ValueError:
        print("Invalid size!")
        input("Press enter to continue...")
        continue
      newMap = generate(size)

      isGenerated = True
      while isGenerated:
        option = input("What do you want to do with the map? \n1. Find areas \n2. Print map \n3. Quit \n")
        if option == '1':
          areas = findAreas(newMap)
          print("Areas: ")
          for i in range(len(areas)):
            print(f"\t{i + 1}. {areas[i]} mt2")

          input("Press enter to continue...")

          isGenerated = False
          break

        elif option == '2':
          printMap(newMap)
          input("Press enter to continue...")

        elif option == '3':
          isGenerated = False
          break
    
    elif option == '3':
      newMap = [
        [ 2,  1,  3,  5,  8],
        [ 0, -1,  0,  2,  5],
        [ 1, -1, -2,  1,  2],
        [ 1, -2,  2, -1, -2]
      ]

      printMap(newMap)
      areas = findAreas(newMap)
      print("Areas: ")
      for i in range(len(areas)):
        print(f"\t{i + 1}. {areas[i]} mt2") 

      input("Press enter to continue...")

    elif option == '4':
      quit = True

    else:
      print("Invalid option")
      input("Press enter to continue...")

if __name__ == "__main__":
  main()
