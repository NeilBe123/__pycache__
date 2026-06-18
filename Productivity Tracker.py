from tkinter import *

task_count = 0
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

    listbox_frame = Frame(
        window
        )
    listbox_frame.pack()

    listbox = Listbox(
        listbox_frame,
        background = "grey",
        foreground = "white"
    )
    listbox.pack(side = LEFT)

    category_entry = Entry(
        listbox_frame,
        background = "white",
        foreground = "black"
    )
    category_entry.pack()

    def add_category():
        listbox.insert(listbox.size(), category_entry.get())

    def delete_category():
        listbox.delete(listbox.curselection())

    category_insert = Button(
        listbox_frame,
        text = "+",
        background = "grey",
        foreground = "black",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 10),
        command = add_category,
    )
    category_insert.pack()

    category_delete = Button(
        listbox_frame,
        text = "-",
        background = "grey",
        foreground = "black",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 10),
        command = delete_category,
    )
    category_delete.pack()



    #Entry() allows for user input
    task_entry = Entry(
        #configures font, background, and foreground
        font = ('Arial', 10, "italic"),
        background = "black",
        foreground = "white",
    )
    task_entry.pack()  

    
    #allows for the submit button to work
    def submit():
        global task_count

        #sets an integer value to x
        x = IntVar()

        #When the checkbutton is clicked, the task is deleted
        def delete():
            global task_count
            #retrieves x variable
            if x.get() == 1:
                #destroys task_display and subtracts from task count
                task_display.destroy()
                task_count -= 1

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
        task_count += 1
        new_task = task_entry.get()
        task_display.configure(text = f"Task {task_count}: {new_task}")
        
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
        activeforeground = "red",
        )
    task_submit.pack()


    #places window on screen
    window.mainloop()

    
productivity_tracker()
