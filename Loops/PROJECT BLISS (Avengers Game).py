print('WELCOME TO PROJECT BLISS')
input('To Start This Game, Press Enter')
print('YOU ARE GOING TO FACE THANOS, THE FATE OF THE WORLD IS ON YOU')
print ('\nTHANOS APPROACHING..')
print("\nTO ASSEMBLE THE AVENGERS, PRESS 'a'\n TO PLAY THE ENDGAME, PRESS 'e'")

s=input()

if s=='a':
 print('AVENGERS ASSEMBLE!')
 print("\nThanos Approaches...")
 print("THANOS: I KNOW WHAT IT'S LIKE TO LOSE, TO FEEL SO DESPERATELY THAT YOU'RE RIGHT \nBUT TO FAIL NONETHELESS \nI ASK YOU, TO WHAT END?")
 print("DREAD IT, RUN FROM IT, DESTINY ARRIVES ALL THE SAME \nAND NOW IT'S HERE OR SHOUILD I SAY, I AM")
 print("\nGAME BEGINS")
 print("\nTo hit Thanos with Thor's Axe, press 'h'.\nTo hit him with Captain America's fist, press 'f'")

elif s=="e":
 print("WE'RE IN THE ENDGAME NOW")
 
Thanos_health = 30
Thors_hammer = 3
Captains_Fist= 2


while s=="a":
 x=input()
 if x=='h':
  Thanos_health-=3
  print ("Thor hits him with the Axebreaker, Go ON")
  print("Thanos Health =" + str(Thanos_health))
    
 if x=='f':
  Thanos_health-=2
  print ("Captain America smashes him, Go ON")
  print("Thanos Health = "+str(Thanos_health))

  
 if Thanos_health==15:
  print("He'S HALF-DEAD, KEEP FIGHTING!")
  
 if Thanos_health==5:
  print('YOU\'RE ALMOST THERE')
  
 if Thanos_health<=0:
  print("HE'S DEAD")
  print("THANOS IS DEFEATED, YOU SAVED THE EARTH")
  
  

 
  




