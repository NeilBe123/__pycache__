from tkinter import *

count = 0
def productivity_tracker():

    #Creates a window instance
    window = Tk()

    #changes window size
    window.geometry("400x400")

    #changes window title
    window.title("Productivity Tracker")
    
    window.config(background = "#000000")

    label = Label(
        window,
        text = "How much have you done?",
        
        # font = (font type, size, type)
        font = ('Arial', 20, "bold"),
        
        #text color
        foreground = "white",
        
        #backgroud color
        background = "#000000",
        
        #padding between the text and border
        padx = 20,
        pady = 20
    )
    #packs the label for use, using .place allows for specific input.
    label.pack()

    
    #Entry() allows for user input
    task_entry = Entry()
    
    #configures font, background, and foreground
    task_entry.config (
        font = ('Arial', 10, "italic"),
        background = "black",
        foreground = "white",
    )
    task_entry.insert(0, "Enter your task here: ")   
    task_entry.pack()

    
    #allows for the submit button to work
    def submit():
        global count

        #sets an integer value to x
        x = IntVar()

        #When the checkbutton is clicked, the task is deleted
        def delete():
            global count
            #retrieves x variable
            if x.get() == 1:
                #destroys task_display and subtracts from task count
                task_display.destroy()
                count -= 1

        #creates a check button next to every task
        task_display = Checkbutton(
        window,
        font = ("monospace", 10),
        background = "black",
        foreground = "white",
        activebackground = "black",
        activeforeground = "white",
        variable = x,
        onvalue = 1,
        offvalue = 0,
        command = delete
        )
        count += 1
        new_task = task_entry.get()
        task_display.configure(text = f"Task {count}: {new_task}")
        
        task_display.pack()

    
    #Users can enter their own tasks here
    task_submit = Button(
        window,
        text = "+",
        font = ('Arial', 15, "bold"),
        #command is tied into a premade function
        command = submit,
        background = "black",
        foreground = "white",
        activebackground = "black",
        activeforeground = "red"
        )
    #side right places down the button
    task_submit.pack(side = RIGHT)


    #places window on screen
    window.mainloop()

productivity_tracker()
