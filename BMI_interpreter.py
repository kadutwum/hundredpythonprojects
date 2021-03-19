print("\t\t\t\t bmi calculator and interpreter".upper())
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/(height**2))

'''if bmi >=35:
  print('Your bmi is {}, you are clinically obese'.format(bmi))
elif bmi >=30 and bmi < 35:
   print('Your bmi is {}, you are obese'.format(bmi))
elif bmi >=25 and bmi < 30:
  print('Your bmi is {}, you are slightly overweight'.format(bmi))
elif bmi >=18.5 and bmi < 25:
  print('Your bmi is {}, you have a normal weight'.format(bmi))
else:
  print('Your bmi is {}, you are underweight'.format(bmi))
  '''

print(f'\nYour BMI is {bmi}\n')

print("interpretation".upper())
 
if bmi < 18.5:
  print(f'Your BMI of {bmi} means you are underweight.')
elif bmi < 25:
  print(f'Your BMI of {bmi} means you have a normal weight')
elif bmi < 30:
  print(f'Your BMI of {bmi} means you are slightly overweight')
elif bmi < 35:
  print(f'Your BMI of {bmi} means you are obese')
else:
  print(f'Your BMI of {bmi} means you are clinically obese')
