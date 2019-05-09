#Social isolation
#chat box opened 

places = ['Tim Hortions', 'Mcdonald','Park','Starbucks','Mall']

print("Hello. Would you like to meet up?")
answer = input()

if answer == "yes":
    while True: #continues to loop until a time is agreed to force the people to meet 
        time = int(input("Input time: "))
        print(f"Would you like to meet at {time} o'clock?")
        meet = input()
        if meet == "yes":
            print(f"Here are the available places: {places}. Where would you want to meet?")
            meeting_place = input()     
            print (f"I will see you at the {meeting_place}.")
            break
        else:
        print("Would you like to choose a different time?")
else:
    print("Sorry, I don't have the time.")
    print("Goodbye.")
  
