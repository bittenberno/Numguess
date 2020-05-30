import random

rannum = random.randrange(0, 100)
#print("The random numer is", rannum)

guesnum=["guesnum0", "guesnum1", "guesnum2", "guesnum3", "guesnum4", "guesnum5", "guesnum6"]



def guesinput(n,Versuch):
  guesnum[(n)]=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))

  if guesnum[(n)]==rannum:
    print("Herzlichen Glückwunsch du hast die Zahl beim "+ (Versuch)+ " Versunch erraten.")
    print("Die gesuchte Zahl ist", rannum)
    quit()
  elif guesnum[(n)]>rannum:
    print("Die Zahl ist kleiner als", guesnum[(n)])
  elif guesnum[(n)]<rannum:
    print("Die Zahl ist größer als", guesnum[(n)])
  else:
    print("ungültige Eingabe")

def lastguesinput(n,Versuch):
  guesnum[(n)]=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))

  if guesnum[n]==rannum:
    print("Herzlichen Glückwunsch du hast die Zahl beim "+ (Versuch)+ " Versunch erraten.")
    print("Die gesuchte Zahl ist", rannum)
  elif guesnum[n]>rannum:
    print("Die Zahl ist kleiner als", guesnum[n])
    print("Schade leider sind deine 7 Versuche um.")
    print("Die gesuchte Zahl war", rannum)
  elif guesnum[n]<rannum:
    print("Die Zahl ist größer als", guesnum[n])
    print("Schade leider sind deine 7 Versuche um.")
    print("Die gesuchte Zahl war", rannum)
  else:
    print("ungültige Eingabe")

print(rannum)

guesinput(0, "ersten")

guesinput(1, "zweiten")

guesinput(2, "dritten")

guesinput(3, "vierten")

guesinput(4, "fünften")

guesinput(5, "sechsten")

lastguesinput(6, "siebten")

print("finish")