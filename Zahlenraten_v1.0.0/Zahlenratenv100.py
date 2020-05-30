import random

rannum = random.randrange(0, 100)
#print("The random numer is", rannum)
guesnum0=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))

if guesnum0==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim ersten Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum0>rannum:
  print("Die Zahl ist kleiner als", guesnum0)
elif guesnum0<rannum:
  print("Die Zahl ist größer als", guesnum0)
else:
  print("ungültige Eingabe")

guesnum1=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum1==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim zweiten Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum1>rannum:
  print("Die Zahl ist kleiner als", guesnum1)
elif guesnum1<rannum:
  print("Die Zahl ist größer als", guesnum1)
else:
  print("ungültige Eingabe")

guesnum2=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum2==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim dritten Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum2>rannum:
  print("Die Zahl ist kleiner als", guesnum2)
elif guesnum2<rannum:
  print("Die Zahl ist größer als", guesnum2)
else:
  print("ungültige Eingabe")

guesnum3=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum3==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim vierten Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum3>rannum:
  print("Die Zahl ist kleiner als", guesnum3)
elif guesnum3<rannum:
  print("Die Zahl ist größer als", guesnum3)
else:
  print("ungültige Eingabe")

guesnum4=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum4==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim fünften Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum4>rannum:
  print("Die Zahl ist kleiner als", guesnum4)
elif guesnum4<rannum:
  print("Die Zahl ist größer als", guesnum4)
else:
  print("ungültige Eingabe")

guesnum5=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum5==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim fünften Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum5>rannum:
  print("Die Zahl ist kleiner als", guesnum5)
elif guesnum5<rannum:
  print("Die Zahl ist größer als", guesnum5)
else:
  print("ungültige Eingabe")

guesnum6=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
if guesnum6==rannum:
  print("Herzlichen Glückwunsch du hast die Zahl beim fünften Versunch erraten.")
  print("Die gesuchte Zahl ist", rannum)
elif guesnum6>rannum:
  print("Die Zahl ist kleiner als", guesnum6)
  print("Schade leider sind deine 7 Versuche um.")
  print("Die gesuchte Zahl war", rannum)
elif guesnum6<rannum:
  print("Die Zahl ist größer als", guesnum6)
  print("Schade leider sind deine 7 Versuche um.")
  print("Die gesuchte Zahl war", rannum)
else:
  print("ungültige Eingabe")