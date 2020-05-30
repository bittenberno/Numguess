import random

#print("The random numer is", rannum)

o=1


while o==1:
  choose=input('Press P to Play\nPress H to show Highscore\nPress E to exit')
  if choose=="p": 
    i=1                # IF choose Play or show Highscore
    while i==1:                   # WHILE Play
      rannum = random.randrange(0, 100)  
      print("The random numer is", rannum)
      for n in range(1,8):
        print(str(n) + ". Versuch")
        guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
        if guesnum==rannum:       # IF Eraten
          print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten.")
          print("Die gesuchte Zahl ist", str(rannum))
          name=input('Bitte gib deinen Namen eingeben.')
          
          f = open('Highscore', 'a')
          f.write('\n' + name + ' -- ' + str(n) + ' Versuche')
          break
        elif guesnum>rannum:      # IF kleiner
          print("Die Zahl ist kleiner als", str(guesnum))
        elif guesnum<rannum:      # IF größer
          print("Die Zahl ist größer als", str(guesnum))
        else:
          print("ungültige Eingabe")
        
        if n==7:                  # IF Game Over
          print('Die gesuchte Zahl war' + str(rannum) +'.')
          print("Game Over")
          break
      print("Danke fürs spielen.")
      
      again=input('Press Enter to play again. Press any other key to close the window.')
      if again!="":
        break

  elif choose=="h":
    Highscore=open('Highscore', 'r')
    print(Highscore.read())
    chooseh=input('Press any key to go back to menu.')
  
  elif choose == 'e':
    break