import random
rannum = random.randrange(0, 100)
#print("The random numer is", rannum)
#masternum=[0,1,2,3,4,5,6]
#guesnum=["guesnum0", "guesnum1", "guesnum2", "guesnum3", "guesnum4", "guesnum5", "guesnum6"]

for n in range(1,8):
  print(str(n) +". Versuch")
  #def guesinput(n):
  guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))

  if guesnum==rannum:
    print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten.")
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


#for n in range(1,7):
  #if n < 8:
   # guesinput(n)
 # else:
  #  break

print("code end")