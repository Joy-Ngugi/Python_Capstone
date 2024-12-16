# import time

# def game():
#     print("Welcome to the Escape room game!")
#     print("The Forgotten Library")
#     print("You wake up in a dimly lit room, your head pounding. The air smells of metal and chemicals. As your eyes adjust, you notice strange symbols etched into the walls and blinking monitors displaying cryptic messages. A robotic voice echoes: 'Welcome, Test Subject. You have been chosen for a series of trials. Escape within the given time, or remain here forever. Your intelligence will determine your fate.'")
#     print()
    
    
# inventory = []

# def check_inventory():
#     if inventory:
#         print(f"Inventory: {','.join(inventory)}")
#     else:
#         print("Your inventory is empty")
        
# def use(item):
#     if item in inventory:
#         print(f"Use use {item}")
#         inventory.remove(item)
#         return True
#     else:
#         print(f"You dont have {item} in yor inventory")
#         return False
    
    
# def room_1():
#     print( "______Room 1: The Beginning._____")
#     print("Hints of past struggles are visible — scratches on the table, faded footprints on the floor. Nearby, you spot a clock ticking ominously, counting down.There is a box with a note")
#     print("The note reads: The more there is, the less you see.")
    
#     while True:
#         answer = input("Enter your answer: ").lower()
#         if answer == "darkness":
#             print("Correct! The box opens revealing a key")
#             inventory.append("key")
#             print("Pick the key and move to the next room")
#             print("")
#             return True
            
#         else:
#             print("Incorrect! Try again!")
            
# def room_2():
#     print("_____Room 2: The code room______")
#     print("Walls are covered in equations and diagrams, as if left behind by a mad scientist. In the center is a keypad with a screen that reads: 'Only the worthy can decode this puzzle. Solve the puzzle:'")
#     print("2 +10 = 24 " )  
#     print("3 + 6=27")  
#     print("7 + 2=63")
#     print("5 + 3 = ??") 
    
#     while True:
#         answer = input("Enter your answer: ")
#         if answer == "40":
#             print("Good job! Your door is unlocked")
#             print("Proceed to the next room")
#             print("")
#             return True
#         else:
#             print("Incorrect! Try again!")
            
# def room_3():
#     print("_____Room 3: Light_____")
#     print("The room is pitch dark. You fumble around and find a flashlight, but it’s missing batteries. On the far wall, glowing letters say:")
#     print("'Sometimes you need to illuminate the truth to find your way.' You must search for the batteries, solve a riddle about light, and find the switch to power the next door.")
    
#     action = input("Do you want to search for batteries? (yes/no): ").lower()
    
#     if action == "yes":
#         print("You found a pair of batteries! Flash light added to your inventory!")
#         inventory.append("flashlight")
#         action2= input("Type 'use flashlight' to light the room: ").strip().lower()
#         if action2 == "use flashlight":
#             if "flashlight" in inventory:
#                 print("You lit the room and found a key! Key added to your inventory")
#                 inventory.append("key")
#                 print("")
#                 return True
#             else:
#                 print("You don't have a flashlight")
#                 return False
#         else:
#             print("Without a flashlight, you can't proceed!")
#             retry = input("Doy you want to try again? (yes/no): ").strip().lower()
#             if retry == "no":
#                 print("You gave up on lighting the room")
#                 return False
            
#     else:
#         print("You decided to not use flashlight. The room remains dark!")
#         retry = input("Doy you want to try again? (yes/no): ").strip().lower()
#         if retry == "no":
#             print("You gave up on searching for the batteries")
#             return False
#         else:
#             print("Batteries found")
#             return True
        
# def room_4():
#     print("_____Room 4: Dark chamber______")
#     print("The room is eerily silent. It’s circular, with walls that bounce sound. A robotic voice says: 'Speak wisely, for I have no mouth yet speak without words.'")
#     print("There’s an old microphone and a dusty speaker. The room seems to be testing your ability to solve auditory riddles.")
    
#     while True:
#         answer = input("Enter the answer: ").lower()
#         if answer == "echo":
#             print("Correct. The door opens and you moved to the final room")
#             print("")
#             return True
#         else:
#             print("Incorrect, Try again!")
            
# def room_5():
#     print("_____Room 5: The Locked door_____")
#     print("You encounter a locked door and you need to open it. You need a key!")
#     action = input("Type 'use key' or 'search'  to find a key: ")
#     if action == "use key":
#         if use("key"):
#             print("The door unlocked and you proceed to the next room!")
#             print("")
#             return True
#         else:
#             print("You don't have a key.")
#     elif action == "search":
#        print("You found nothing of interest")
#     else:
#         print("Invalid action. Try again!") 
#     return False


# def room_6():
#     print("_____Room 6: Countdown_____")
#     print("You enter the final room. A console displays a 10-second countdown!")
#     print("The message reads: 'To escape, enter the correct sequence: 4, 8, 15, 16, 23, 42.'")
    
#     sequence = ["4", "8", "15", "16", "23", "42"]
#     user_sequence = []
    
#     countdown = 10
#     start_time = time.time()
#     while time.time()- start_time < 10:
#         elapsed_time = int(time.time() - start_time)
#         remaining_time = countdown - elapsed_time
#         print(f"\nTime left: {remaining_time} seconds")
#         time.sleep(1)
#         if remaining_time<=0:
#              break
        
#         number = input("Enter the next number in the sequence: ")
#         user_sequence.append(number)
#         if user_sequence == sequence:
#             print("Correct! The door has unlocked")
#             print("Congratulations! You have escaped the laboratory successfully!")
#             print("")
#             return True
        
#     print("Time's up! You've been locked in the laboratory forever! Game over.")
#     return False


# def play():
#     game()
#     if room_1():
#         if room_2():
#             if room_3():
#                 if room_4():
#                     if room_5():
#                         if room_6():
                            
#                            print("You survived 'The Forggotten Libary'")
#                         else:
                            
#                             print("You failed in the final room.")
#                     else:
#                         print("You failed in room 5")
#                 else:
#                     print("You failed in room 4")
#             else:
#                 print("You failed in room 3")
#         else:
#             print("You failed in room 2")
#     else:
#         print("You failed in room 1")
#     print("Thank you for playing")
    
# if __name__=="__main__":
#     play()