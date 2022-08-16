import owoify

print("1: Owofiy\n2: Decode")
x = input("Pick a option:")
print("------------------------------")

if x == "1":
   e = input("Text you want to owoify:\n")
   print("------------------------------\nOwoifyed Version:")
   print(owoify.owoify(e))
elif x == "2":
   e = input("Text you want to decode:\n")
   print("------------------------------\nDecoded Version:")
   print(owoify.decode(e))
else:
   print("That's not an option, try again")