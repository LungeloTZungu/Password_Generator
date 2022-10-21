import  random

Upletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LowLetter= "abcdefghijklmnopqrstuvwxyz"
symbol = "!@#$%^&*()_+"
numbers = "0123456789"

String = Upletters +LowLetter+symbol+numbers
Length = 16
Password = "".join(random.sample(String,Length))

print("Your generated password is: " + Password)