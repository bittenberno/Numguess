import random
o=1
while o==1:
  choose=input('Press P to Play \nPress H to show Highscore \nPress C to show Credits \nPress E to exitp\n')
  if choose=="p": 
    i=1 # IF choose Play or show Highscore
    while i==1: # WHILE Play
      rannum = random.randrange(1, 101)  
      #print("The random numer is", rannum)
      for n in range(1,8):
        print('\n' + str(n) + ". Versuch")
        guesnum=int(input("Bitte eine Zahl zwischen 1 - 100 eingeben\n"))
        if guesnum==rannum: # IF Eraten
          print("Herzlichen Glückwunsch du hast die Zahl beim " + str(n) + ". Versunch erraten.")
          print("Die gesuchte Zahl war ", str(rannum))
          name=input('\nBitte gib deinen Namen eingeben.\n')
          f = open('Highscore', 'a')
          if n==1:
            f.write('\n' + name + ' -- ' + str(n) + ' Versuch')
          else:
            f.write('\n' + name + ' -- ' + str(n) + ' Versuche')
          break
        elif guesnum>rannum: # IF kleiner
          print("Die gesuchte Zahl ist kleiner als ", str(guesnum))
        elif guesnum<rannum: # IF größer
          print("Die gesuchte Zahl ist größer als ", str(guesnum))
        else:
          print("ungültige Eingabe")
        
        if n==7: # IF Game Over
          print("\nGame Over ")
          print('Die gesuchte Zahl war ' + str(rannum) +'.')
          break
      print("\nDanke fürs spielen. ")
      
      again=input('\nPress Enter to play again. Press any other key to go back to mainmenu.\n')
      if again!="":
        break

  elif choose=="h":
    Highscore=open('Highscore', 'r')
    print(Highscore.read())
    input('\nPress any key to go back to mainmenu.\n')
  
  elif choose == 'c':
    print('\nMaincreator: Bernhard Lorenz')
    input('\nPress any key to go back to mainmenu.\n')

  elif choose == 'e':
    break