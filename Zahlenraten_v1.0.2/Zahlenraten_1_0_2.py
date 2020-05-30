import random
#
rannum = random.randrange(0, 100)
#print("The random numer is", rannum)
i=1

choose=input('Drück "P" um zu spielen oder "H" um den Highscore anzuzeigen')
if choose=="p":
  while i==1:
    for n in range(1,8):
      print(str(n) + ". Versuch")
      #def guesinput(n):
      guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
      if guesnum==rannum:
        print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten.")
        print("Die gesuchte Zahl ist", str(rannum))
        name=input('Bitte gib deinen Namen eingeben.')
        
        f = open('completeName', 'a')
        f.write('\n' + name + ' -- ' + str(n) + ' Versuche')
        break
      elif guesnum>rannum:
        print("Die Zahl ist kleiner als", str(guesnum))
      elif guesnum<rannum:
        print("Die Zahl ist größer als", str(guesnum))
      else:
        print("ungültige Eingabe")
      
      if n==7:
        print('Die gesuchte Zahl war' + str(rannum) +'.')
        print("Game Over")
    
    print("Danke fürs spielen.")
    
    again=input('Press "J" to play again. Press any other key to close the window.')
    if again!="j":
      break
elif choose=="h":
 # print(Highscore)
  input('Press any key to close the window.')