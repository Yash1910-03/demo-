
from math import pow
from math import sqrt
from math import cbrt

number=int(input("enter the number"))
print(f"value is:{pow(number,5)}")
print(f"value is:{sqrt(number)}")
print(f"value is:{cbrt(number)}")

password=input("enter your password")
if (len(password)<=8):
    print(f'apke account se paisa gayab ho sakta he')
else:
    print('will check and revert')

password_data=input("enter number")
if(password_data.isalnum()):
    print("pass has both num and alphabets")
else:
    print("others")
    