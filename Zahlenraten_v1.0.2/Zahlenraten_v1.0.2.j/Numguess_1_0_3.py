import random
o=1
while o==1:
  choose=input('Press P to Play\nPress H to show Highscore\nPress C to show Credits\nPress E to exit\n')
  if choose=="p": 
    i=1 # IF choose Play or show Highscore
    while i==1: # WHILE Play
      rannum = random.randrange(0, 100)  
      print("The random numer is", rannum)
      for n in range(1,8):
        print('\n' + str(n) + ". Versuch")
        guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben"))
        if guesnum==rannum: # IF Eraten
          print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten.")
          print("Die gesuchte Zahl war", str(rannum))
          name=input('\nBitte gib deinen Namen eingeben.')
          f = open('Highscore', 'a')
          if n==1:
            f.write('\n' + name + ' -- ' + str(n) + ' Versuch')
          else:
            f.write('\n' + name + ' -- ' + str(n) + ' Versuche')
          break
        elif guesnum>rannum: # IF kleiner
          print("Die gesuchte Zahl ist kleiner als", str(guesnum))
        elif guesnum<rannum: # IF größer
          print("Die gesuchte Zahl ist größer als", str(guesnum))
        else:
          print("ungültige Eingabe")
        
        if n==7: # IF Game Over
          print("\nGame Over")
          print('Die gesuchte Zahl war' + str(rannum) +'.')
          break
      print("\nDanke fürs spielen.")
      
      again=input('\nPress Enter to play again. Press any other key to go back to mainmenu.')
      if again!="":
        break

  elif choose=="h":
    Highscore=open('Highscore', 'r')
    print(Highscore.read())
    input('\nPress any key to go back to mainmenu.')
  
  elif choose == 'c':
    print('\nMaincreator: Bernhard Lorenz\n\nSpezieller Gruß geht raus an Jakob. Wie gehts beim Einhell so?\nIch werd dich beim Niedermaier vermissen. ;-)')
    input('\nPress any key to go back to mainmenu.')

  elif choose == 'e':
    break