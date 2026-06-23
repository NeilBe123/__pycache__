from tkinter import *
from tkinter import ttk

task_count = 0
def productivity_tracker():

    #Creates a window instance
    window = Tk()
    #changes window size
    window.geometry("400x600")
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
    label.grid(row = 0)


    #A frame which contains the category list and entry
    listbox_frame = Frame(
        window
        )
    listbox_frame.grid(row = 1, column = 0)


    #The listbox for the user's categories
    listbox = Listbox(
        listbox_frame,
        background = "grey",
        foreground = "white"
    )
    listbox.grid(row=0, column = 0)


    #A frame which contains the Entry widget and button frame
    category_entry_frame = Frame(
        listbox_frame
    )
    category_entry_frame.grid(row = 0, column = 1)


    #The user can enter their category name here
    category_entry = Entry(
        category_entry_frame,
        background = "white",
        foreground = "black"
    )
    category_entry.grid(row = 0, column = 0)


    #A seperate frame for all the buttons
    listbutton_frame = Frame(
        category_entry_frame
    )
    listbutton_frame.grid(row=1)


    #When activated, a category is added to the list
    def add_category():

        #A frame is created inside the listbox
        listbox_item_frame = Frame(
            listbox,
            background = "white"
        )
        #listbox_item_frame.pack()


        #The category is titled here
        list_dropdown_label = Label(
            listbox_item_frame,
            text = category_entry.get(),
            background = "white",
            foreground = "Black"
        )
        #list_dropdown_label.pack()


        #Creates a dropdown menu inside the list        
        list_dropdown = ttk.Combobox(
            listbox_item_frame
        )
        #list_dropdown.pack()
        

    #When activated, a category is deleted from the list
    def delete_category():
        listbox.delete(listbox.size(), listbox.curselection())


    #The button tied to add_category function
    category_insert = Button(
        listbutton_frame,
        text = "+",
        background = "grey",
        foreground = "black",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 10),
        command = add_category,
    )
    category_insert.grid(row = 0, column = 0)


    #The button tied to delete_category function
    category_delete = Button(
        listbutton_frame,
        text = "-",
        background = "grey",
        foreground = "black",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 10),
        command = delete_category,
    )
    category_delete.grid(row = 0, column = 1)


    #Frame for task entry
    task_frame = Frame(
        window,
        background = "black",
        border = 5
    )
    task_frame.grid(row = 2, column = 0)

    #Entry() allows for user input
    task_entry = Entry(
        task_frame,
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
        bleh = task_display.configure(text = f"Task {task_count}: {new_task}")

    
    #Users can enter their own tasks for the category here
    task_submit = Button(
        task_frame,
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

