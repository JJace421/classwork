#2
total_minutes = int(input("Total minutes: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes}mins is {hours :02d}:{minutes :02d}")


#3
frame_count = int(input("Insert frame count. "))
shot = frame_count % 60
print((frame_count // 60), "shots so far.")

if shot == 0:
    print("Shoot at this frame.")
else:
    print("Can't shoot at this frame.")


#4
total_cents = int(input("Total cents: "))
dollars = total_cents // 100
cents = total_cents % 100
print (f"${dollars}.{cents}")

#5
toonie = dollars // 2
loonie = dollars - 2 * toonie
quartre = cents // 25
dime = (cents - 25 * quartre) // 10
nickle = (cents - (25 * quartre + 10 * dime)) // 5
penny = (cents - (25 * quartre + 10 * dime + 5 * dime)) // 1

print(f"{toonie} - toonie")
print(f"{loonie} - loonie")
print(f"{quartre} - quartre")
print(f"{dime} - dime")
print(f"{nickle} - nickle")
print(f"{penny} - penny")


#6
Groups = ['#0', '#1', '#2', '#3', '#4']
student_id = int(input("Student id: "))
num = student_id % 10
group = num - 5

print(f"You are in group {Groups[group]}")

#7 The output is either 0 or 1

#8 When inputing a number % 3/4, you will determne either the number is a multiple of 3/4 with the result is 0.
