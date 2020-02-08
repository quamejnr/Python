while True:
 print('Options')
 print('Type "add" to add numbers')
 print('Type "subtract" to subtract numbers')
 print ('Type "multiply" to multiply numbers')
 print ('Type "divide" to divide numbers')
 print ('Type "quit" to quit this application')

 s=input()

 if s=="quit":
  break
  
 elif s=="add":
  Num_1 = float(input('\nEnter first number: '))
  Num_2 =float(input('Enter second number: '))
  result= str(Num_1 + Num_2)
  print ('The answer is ' + result)
  print ("")
 
 elif s=="multiply":
  Num_1 = float(input('\nEnter first number: '))
  Num_2 =float(input('Enter second number: '))
  result= str(Num_1 * Num_2)
  print ('The answer is ' + result) 
  print ("")
 
 elif s=="divide":
  Num_1 = float(input('\nEnter first number: '))
  Num_2 =float(input('Enter second number: '))
  result= str(Num_1 / Num_2)
  print ('The answer is ' + result) 
  print ("")
 
 elif s=="subtract":
  Num_1 = float(input('\nEnter first number: '))
  Num_2 =float(input('Enter second number: '))
  result= str(Num_1 - Num_2)
  print ('The answer is ' + result) 
  print ("")
 

 



