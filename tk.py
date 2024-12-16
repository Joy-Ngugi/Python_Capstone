import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import PhotoImage


class EscapeRoomGame(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Escape Room Game")
        self.geometry("600x450")
        self.inventory = []
        self.current_frame = None
        self.timer_duration = 300 
        
        self.remaining_time = 0 
        self.timer_id = None  

        
        self.timer_label = tk.Label(self, text="", font=("Helvetica", 14))
        self.timer_label.pack(pady=5)

        self.switch_frame(MainMenu)

    
    def start_timer(self, duration=None):
   
        if hasattr(self, 'timer_id') and self.timer_id is not None:
            self.after_cancel(self.timer_id)  
        
        if duration:
            self.remaining_time = duration
        else:
            self.remaining_time = self.timer_duration
            
        self.timer_id=None
        self.update_timer()

    def update_timer(self):
        
        if self.remaining_time > 0:
            self.remaining_time -= 1
            mins, secs = divmod(self.remaining_time, 60)
            timer_text = f"Time Left: {mins:02}:{secs:02}"
            self.timer_label.config(text=timer_text)
            self.timer_id= self.after(1000, self.update_timer)
        else:
            self.game_over()

    def game_over(self):
        if self.timer_id is not None:
            self.after_cancel(self.timer_id)
            
        messagebox.showinfo("Game Over", "Time's up! You did not complete the game in time.")
        self.switch_frame(MainMenu)
        self.start_timer(300)

    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)
  

    def add_to_inventory(self, item):
        """Add an item to the inventory and show a message."""
        if item not in self.inventory:
            self.inventory.append(item)
            messagebox.showinfo("Inventory Updated", f"{item} added to your inventory!")
        else:
            messagebox.showinfo("Inventory", f"{item} is already in your inventory.")

    def check_inventory(self):
        """Display the inventory."""
        if self.inventory:
            messagebox.showinfo("Inventory", f"Your Inventory: {', '.join(self.inventory)}")
        else:
            messagebox.showinfo("Inventory", "Your inventory is empty!")


class MainMenu(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.bg_image = PhotoImage(file = r"images/HauntedHouse-1030x525.png")
        bg_label = tk.Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
            
        
        tk.Label(self, text="ROOMS & EXITS", font=("Times New roman", 28), bg="#273746", fg="white").pack(pady=20)
        tk.Label(self, text="Can you excape the room?", font=("Times New roman", 20), bg="#273746", fg="white").pack()
       
    
        text_widget = tk.Text(self, width=50, height=7, wrap="word", bg="#415a77")
        text_widget.pack(pady=20, padx=20)

   
        text_widget.tag_configure("title", font=("Helvetica", 17, "bold"), foreground="#e0e1dd")
        text_widget.tag_configure("highlight", font=("Arial", 13, "italic"), foreground="white")
        text_widget.tag_configure("default", font=("Times New Roman", 13))

   
        text_widget.insert("1.0", "The Forgotten Library\n", "title")  
        text_widget.insert("2.0", "You wake up in a dimly lit room. The air smells of chemicals.\n", "default") 
        text_widget.insert("3.0", "Your intelligence will determine your fate.", "highlight")  
   
        text_widget.config(state="disabled")
        
        frame_buttons = tk.Frame(self) 
        frame_buttons.pack(pady=5) 
        tk.Button(self, text="Start Game", command=lambda: master.switch_frame(Room1)).pack(side="left", padx=30,)
        
        tk.Button(self, text="Quit", command=master.quit).pack(side="left", padx=30)
        
    def start_game(self):
        """Start the game and reset the timer."""
       
        self.master.switch_frame(Room1)
    
class Room1(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.bg_image = PhotoImage(file = r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\Untitled design.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        self.master.start_timer()
        
        tk.Label(self, text="Room 1: The Beginning", font=("Times New Roman", 18) , bg="white" , fg="black").pack(pady=50)
     
        
        self.label = tk.Label(self, text="", font=("Times New Roman", 14), wraplength=500, justify="left", bg="#6a040f", fg="white")
        self.label.pack(pady=5) 
        self.story_text = "Hints of past struggles are visible — scratches on the table, faded footprints on the floor. Nearby, you spot a clock ticking ominously, counting down. There is a box with a note written: \n 'The more there is, the less you see.'"
        self.index = 0
        self.type_text()
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=20)
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        inventory_button.pack(side="right", pady=10, padx=20)
        
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
       
        
    def show_inventory(self):
        """Display inventory in a pop-up window."""
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            tk.Button(frame, text="Use", command=lambda i=item: self.use_item(i, inventory_window)).pack(side="right", padx=5)
            

    def use_item(self, item, inventory_window):
        """Handle using an item."""
        self.master.inventory.remove(item)  
        inventory_window.destroy()  
        messagebox.showinfo("Item Used", f"You used {item}!")
        
    
    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(20, self.type_text)

    def check_answer(self, event=None):
        answer = self.answer_entry.get().lower()
        if answer == "darkness":
            messagebox.showinfo("Correct!", "You found a key!")
            self.master.add_to_inventory("key")
            self.master.switch_frame(Room2)
        else:
            messagebox.showerror("Wrong Answer", "Try again!")
   

class Room2(tk.Frame):
    """Room 2."""
    def __init__(self, master):
        super().__init__(master)
        self.bg_image = PhotoImage(file = r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-photo-14000469.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self, text="Room 2: The Code Room", font=("Helvetica", 18)).pack(pady=10)
        self.label = tk.Label(self, text="", font=("Times New Roman", 14), wraplength=500, justify="left", bg="#6a040f", fg="white")
        self.label.pack(pady=10) 
        self.story_text = "Walls are covered in equations and diagrams, as if left behind by a mad scientist. In the center is a keypad with a screen that reads: 'Only the worthy can decode this puzzle. Solve the puzzle: \n Solve the puzzle:\n2 + 10 = 24\n3 + 6 = 27\n7 + 2 = 63\n5 + 3 = ?"
        self.index = 0
        self.type_text()
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=20)
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        inventory_button.pack(side="right", pady=10, padx=20)
        
               
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
    def show_inventory(self):
       
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            
            tk.Button(frame , text="Use").pack(side="right", padx=5)
            

    def use_item(self, item, inventory_window):
        """Handle using an item."""
        self.master.inventory.remove(item)  
        inventory_window.destroy()  
        messagebox.showinfo("Item Used", f"You used {item}!")
        
    
    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(20, self.type_text)
     

    def check_answer(self):
        answer = self.answer_entry.get()
        if answer == "40":
            messagebox.showinfo("Correct!", "The door unlocked!")
            self.master.switch_frame(Room3)
        else:
            messagebox.showerror("Wrong Answer", "Try again!")



class Room3(tk.Frame):
    """Room 3."""
    # def __init__(self, master):
    #     super().__init__(master)
        
    #     self.bg_image = PhotoImage(file=r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-photo-4888431.png")
    #     bg_label = Label(self, image=self.bg_image)
    #     bg_label.place(relwidth=1, relheight=1)
        
    #     tk.Label(self, text="Room 3: Light", font=("Helvetica", 18)).pack(pady=10)
    #     self.label = tk.Label(self, text="", font=("Times New Roman", 13), wraplength=500, justify="left", bg="white", fg="black")
    #     self.label.pack(pady=10) 
    #     self.story_text = "The room is pitch dark. You fumble around and find a flashlight \nOn the far wall, glowing letters say: 'Sometimes you need to illuminate the truth to find your way.' You must search for the batteries to power the next door."
    #     self.index = 0
    #     self.type_text()
        
       
        
    #     self.find_batteries_button = tk.Button(self, text="Search for Batteries", command=self.find_batteries)
    #     self.find_batteries_button.pack(pady=30)
              
        
    #     self.inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
    #     self.inventory_button.pack(side="right", pady=10, padx=20)
        
        
        
    #     back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
    #     back_button.pack(side="left", pady=10, padx=20)
        
    # def show_inventory(self):
    #     """Display inventory in a pop-up window."""
    #     inventory_items = self.master.inventory  
    #     if not inventory_items:
    #         messagebox.showinfo("Inventory", "Your inventory is empty!")
    #         return

    #     inventory_window = tk.Toplevel(self)
    #     inventory_window.title("Inventory")
    #     inventory_window.geometry("300x300")

    #     tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

    #     for item in inventory_items:
    #         frame = tk.Frame(inventory_window)
    #         frame.pack(fill="x", pady=5)

    #         tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
    #         tk.Button(frame, text="Use", command=lambda i=item: self.use_item(i, inventory_window)).pack(side="right", padx=5)

    # def use_item(self, item, inventory_window):
    #     if item == "flashlight":
    #         self.master.inventory.remove(item)  
    #         inventory_window.destroy()  
    #         messagebox.showinfo("Item Used", f"You used {item}! Moving to the next room.")
    #         self.master.switch_frame(Room4)
        
    # def type_text(self):
    #     if self.index <= len(self.story_text):
    #         self.label.config(text=self.story_text[:self.index])
    #         self.index += 1
    #         self.after(20, self.type_text)
       
   
    # def find_batteries(self):
    #     messagebox.showinfo("You found the batteries and inserted them in your flashlight! Flashlight added to inventory.")
    #     self.master.add_to_inventory("flashlight")
        
    #     self.inventory_button.pack(pady=10)
    #     self.find_batteries_button.pack_forget()

    def __init__(self, master):
        super().__init__(master)
        
        self.bg_image = PhotoImage(file=r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-photo-4888431.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self, text="Room 3: Light", font=("Helvetica", 18)).pack(pady=10)
        self.label = tk.Label(self, text="", font=("Times New Roman", 13), wraplength=500, justify="left", bg="white", fg="black")
        self.label.pack(pady=10) 
        self.story_text = "The room is pitch dark. You fumble around and find a locked chest with a keypad on it. There’s a riddle written on a scroll next to the chest. Solve the riddle to find the 4-digit code that opens the lock. \nI am a 4-digit number. \nMy first digit is twice the second digit. \nThe sum of all my digits is 14. \nThe last digit is the square of the second digit. \nWhat am I?"
        self.index = 0
        self.type_text()
               
                
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=20)
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        self.inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        self.inventory_button.pack(side="right", pady=10, padx=20)
        
        
        
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
    def show_inventory(self):
        """Display inventory in a pop-up window."""
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            tk.Button(frame, text="Use", command=lambda i=item: self.use_item(i, inventory_window)).pack(side="right", padx=5)

    def use_item(self, item, inventory_window):
        if item == "flashlight":
            self.master.inventory.remove(item)  
            inventory_window.destroy()  
            messagebox.showinfo("Item Used", f"You used {item}! Moving to the next room.")
            self.master.switch_frame(Room4)
        
    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(20, self.type_text)
            
    def check_answer(self):
        answer = self.answer_entry.get().lower()
        if answer == "4244":
            messagebox.showinfo("Correct!", "The door unlocked!")
            self.master.switch_frame(Room5)
        else:
            messagebox.showerror("Wrong Answer", "Try again!") 
   
  
class Room4(tk.Frame):
    """Room 4."""
    def __init__(self, master):
        super().__init__(master)
        
        self.bg_image = PhotoImage(file = r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-photo-9862516.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self, text="Room 4: Dark Chamber", font=("Helvetica", 18)).pack(pady=10)
        self.label = tk.Label(self, text="", font=("Times New Roman", 14), wraplength=500, justify="left", bg="black", fg="white")
        self.label.pack(pady=10) 
        self.story_text = "The room is eerily silent. It’s circular, with walls that bounce sound. A robotic voice says: \n 'Speak wisely, for I have no mouth yet speak without words.'\n There’s an old microphone and a dusty speaker. The room seems to be testing your ability to solve auditory riddles."
        self.index = 0
        self.type_text()
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=20)
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        inventory_button.pack(side="right", pady=10, padx=20)
                      
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
    def show_inventory(self):
        """Display inventory in a pop-up window."""
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            tk.Button(frame , text="Use").pack(side="right", padx=5)
            

    def use_item(self, item, inventory_window):
        """Handle using an item."""
        self.master.inventory.remove(item)  
        inventory_window.destroy()  
        messagebox.showinfo("Item Used", f"You used {item}!")
        
    
    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(20, self.type_text)
      
    def check_answer(self):
        answer = self.answer_entry.get().lower()
        if answer == "echo":
            messagebox.showinfo("Correct!", "The door unlocked!")
            self.master.switch_frame(Room5)
        else:
            messagebox.showerror("Wrong Answer", "Try again!")

class Room5(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        
        self.bg_image = PhotoImage(file = r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-rolan3d-285669.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self, text="Room 5: The Locked Door", font=("Helvetica", 18)).pack(pady=10)
        self.label = tk.Label(self, text="", font=("Times New Roman", 14), wraplength=500, justify="left", bg="black", fg="white")
        self.label.pack(pady=10) 
        self.story_text = "You enter a room with a strange clock on the wall. The clock has numbers from 1 to 12, but something seems off about its hands. The following riddle is engraved beneath it: \n'I am a time you cannot see, But add me, subtract me, and I'll still be me.' \nWhat am I? \nThere is also a locked door and you need to open it. You need a key! "
        self.index = 0
        self.type_text()
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=20)
        # self.answer_entry.delete(0, tk.END)

        
        tk.Button(self, text="Submit", command=self.check_answer).pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_answer())
        inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        inventory_button.pack(side="right", pady=10, padx=20)
        
          
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
    def show_inventory(self):
        """Display inventory in a pop-up window."""
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            tk.Button(frame, text="Use", command=lambda i=item: self.use_item(i, inventory_window)).pack(side="right", padx=5)
           
    def use_item(self, item, inventory_window):
        if item=="key":
            self.master.inventory.remove(item)  
            inventory_window.destroy()  
            messagebox.showinfo("Item Used", f"You used the {item} to unlock the door! Moving to the next room.")
            self.master.switch_frame(Room6)
       
        
        
    
    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(20, self.type_text)
       

    def check_answer(self):
        answer = self.answer_entry.get().lower()
   
        if answer=="12" or "noon" or "midnight" or "afternoon":
            messagebox.showinfo("Correct! You can continue.")
        else:
            messagebox.showerror("Invalid answer", "Try again!")



class Room6(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.sequence = ["4", "8", "15", "16", "23", "42"] 
        self.user_sequence = [] 
        self.index = 0  
        self.timer = None  
        self.timer_started = False
        
        self.bg_image = PhotoImage(file = r"C:\Users\ZBOOK WORKSTATION\Desktop\zindua\Python.py\Capstone\images\pexels-photo-7662602.png")
        bg_label = Label(self, image=self.bg_image)
        bg_label.place(relwidth=1, relheight=1)
        
        tk.Label(self, text="Room 6: The Countdown", font=("Helvetica", 18)).pack(pady=10)
        self.label = tk.Label(self, text="", font=("Times New Roman", 14), wraplength=500, justify="left", bg="white", fg="black")
        self.label.pack(pady=10)
        self.story_text = "You enter the final room. A console displays a 10-second countdown! \nThe message reads: 'To escape, enter the correct sequence: 4, 8, 15, 16, 23, 42.'"
        self.index = 0
        self.type_text()
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=30, padx=20)
        self.answer_entry.bind("<FocusIn>", self.start_timer)
        self.button= tk.Button(self, text="Submit", command=self.check_sequence)
        self.button.pack(pady=10)
        self.answer_entry.bind("<Return>", lambda event: self.check_sequence())
        
        self.timer_label = tk.Label(self, text="Time left: 10 seconds", font=("Helvetica", 14), fg="red")
        self.timer_label.pack(pady=10)
        inventory_button = tk.Button(self, text="Inventory", command=self.show_inventory)
        inventory_button.pack(side="right", pady=10, padx=20)
        
              
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: master.switch_frame(MainMenu))
        back_button.pack(side="left", pady=10, padx=20)
        
        self.time_left = 10
        
    def show_inventory(self):
        
        inventory_items = self.master.inventory  
        if not inventory_items:
            messagebox.showinfo("Inventory", "Your inventory is empty!")
            return

        inventory_window = tk.Toplevel(self)
        inventory_window.title("Inventory")
        inventory_window.geometry("300x300")

        tk.Label(inventory_window, text="Your Inventory", font=("Helvetica", 14)).pack(pady=10)

        for item in inventory_items:
            frame = tk.Frame(inventory_window)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=item, font=("Times New Roman", 12)).pack(side="left", padx=10)
            tk.Button(frame , text="Use", command=lambda i=item: self.use_item(i, inventory_window)).pack(side="right", padx=5)
            tk.Button(frame, text="Cancel", command=inventory_window.destroy).pack(side="right")

    def use_item(self, item, inventory_window):
        """Handle using an item."""
        self.master.inventory.remove(item)  
        inventory_window.destroy()  
        messagebox.showinfo("Item Used", f"You used {item}!")

    def type_text(self):
        if self.index <= len(self.story_text):
            self.label.config(text=self.story_text[:self.index])
            self.index += 1
            self.after(10, self.type_text)
        else:
            self.start_timer()
            
    def start_timer(self, event=None):
        
        if not self.timer_started:
            self.timer_started = True
            self.time_left = 10
            self.update_timer()
            
    def update_timer(self):
       
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            self.time_left -= 1
            self.timer = self.after(1000, self.update_timer)  
        else:
            self.game_over("Time's up! You failed to escape.")
    
    def check_sequence(self):
        number = self.answer_entry.get()
        self.answer_entry.delete(0, tk.END)

        if not number:
            messagebox.showwarning("Input Error", "Please enter a number.")
            return

        if number == self.sequence[len(self.user_sequence)]:
            self.user_sequence.append(number)
            if len(self.user_sequence) == len(self.sequence):
                self.after_cancel(self.timer) 
                messagebox.showinfo("Congratulations!", "You escaped the lab!")
                self.master.switch_frame(MainMenu) 
                self.master.start_timer()
        else:
            self.game_over("Wrong sequence! You failed to escape.")

    def game_over(self, message):
        if self.timer:
             self.after_cancel(self.timer)  
        messagebox.showerror("Game Over", message)
        self.master.switch_frame(MainMenu)
        self.master.start_timer()



if __name__ == "__main__":
    app = EscapeRoomGame()
    app.mainloop()
