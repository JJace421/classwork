#1 
print("Cost         With Tax")
print("---------------------")


for x in range(10,55,5):

    print(f"${x}         ${x * 1.15}")


#2 
sub_total = 0
for x in range(5):
    cost = int(input("Cost: "))
    sub_total += cost

print(f"Subtotal: ${sub_total}")

tax = 0.13
tax_amount = sub_total * tax

print(f"Tax amount: ${tax_amount}")

print(f"Total: ${sub_total + tax_amount}")


#3
total = 0
print("Enter a number. To stop, enter nothing: ")

while True:
    num = input("Num: ")
    if num == "":
        break
    else:
        total += int(num)

print(total)
    
