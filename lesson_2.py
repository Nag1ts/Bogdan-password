from random import choice

symbols = "+-/*!&$№:#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lenght_password = int(input("Enter lenght password"))
box = ""

for i in range(lenght_password):
    box += choice(symbols)

print(box)