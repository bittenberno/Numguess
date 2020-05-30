import random
rannum = random.randrange(0, 100)
#print("The random numer is", rannum)
i=1
while i==1:
  for n in range(1,8):
    print(str(n) +". Versuch")
    #def guesinput(n):
    guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))

    if guesnum==rannum:
      print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten. **********")
      print("Die gesuchte Zahl ist", rannum)
      break
    elif guesnum>rannum:
      print("Die Zahl ist kleiner als", guesnum)
    elif guesnum<rannum:
      print("Die Zahl ist größer als", guesnum)
    else:
      print("ungültige Eingabe")
    
    if n==7:
      print("Game Over")
  
  print("Danke fürs spielen.")
  again=input('Press "J" to play again. Press any other key to close the Window.')
  if again!="j":
    break