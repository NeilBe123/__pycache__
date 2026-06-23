<!DOCTYPE html>
<html lang = "en">

<head>
    <meta http=equiv = "Content-Type" content = "text/html; charset = "UTF-8">
    <link rel = "stylesheet" href = "https://pyscript.net/latest/pyscrip.css">
    <script defer src = "https://pyscript.net/latest/pyscript.js"></script>
</head>

<body>
<py-config>
packages = ["tkinter"]
</py-config>


<py-script>
from tkinter import *
from tkinter import ttk

def productivity_tracker():

    #Creates a window instance
    window = Tk()
    #changes window size
    window.geometry("400x600")
    #changes window title
    window.title("Productivity Tracker")    
    window.config(background = "#1A312C")
 
    #Header label
    Header_label = Label(
        window,
        text = "How much have you done?",

        # font = (font type, size, type)
        font = ('Arial', 20, "bold"),

        #text color
        foreground = "#FFF4E1",

        #backgroud color
        background = "#1A312C",

        #padding between the text and border
        padx = 20,
        pady = 20
    )
    Header_label.grid(row = 0)


    #A frame which contains the category list and entry
    main_frame = Frame(
        window,
        background = "#428475"
    )
    main_frame.grid(row = 1, column = 0)


    #The listbox for all the user's categories
    Category_frame = Frame(
        main_frame
    )
    Category_frame.grid(row=0, column = 0)


    #A frame which contains the Entry widget and button frame
    category_entry_frame = Frame(
        main_frame,
        background = '#428475'
    )
    category_entry_frame.grid(row = 0, column = 1)


    #The user can enter their category name here
    category_entry = Entry(
        category_entry_frame,
        background = "#B1D3B9",
        foreground = "#303841",
        font = ('monospace', 12)
    )
    category_entry.grid(row = 0, column = 0)


    #A seperate frame for all the buttons
    listbutton_frame = Frame(
        category_entry_frame,
        background = "#FFAE6E"
    )
    listbutton_frame.grid(row=1)



    #When activated, a new category is added to the list
    def add_category():

        #When the user double clicks on one of the frames, the frame disappears
        def on_double_click():
            listbox_item_frame.destroy()

        #A frame is created inside the Category frame
        listbox_item_frame = Frame(
            Category_frame,
            background = "#428475",
            highlightthickness = 2,
            highlightbackground = "#24B1B1"
        )
        listbox_item_frame.pack()
        listbox_item_frame.bind("Double-1", on_double_click)


        #The category is titled here
        list_dropdown_label = Label(
            listbox_item_frame,
            text = category_entry.get(),
            background = "#88BDA4",
            foreground = "#303841",
            font = ('monospace', 12)
        )
        list_dropdown_label.grid(row = 0, column = 0)

        #Entry() allows for the user to input their own tasks
        task_entry = Entry(
            listbox_item_frame,
            #configures font, background, and foreground
            font = ('monospace', 12),
            background = "#B1D3B9",
            foreground = "#303841",
        )
        task_entry.grid(row = 2, column = 0) 

        #Creates a separate frame inside the listbox frame so, tasks can be stored here
        list_dropdown = Frame(
            listbox_item_frame,
            background = "#88BDA4"
            )
        list_dropdown.grid(row = 1, column = 0)

        #allows for the submit button to work
        def submit():

            #sets an integer value to x
            x = IntVar()

            #When the checkbutton is clicked, the task is deleted
            def delete():
                #retrieves x variable
                if x.get() == 1:
                    #destroys task_display and subtracts from task count
                    task_display.destroy()

            #creates a check button next to every task
            task_display = Checkbutton(
            list_dropdown, 
            font = ("monospace", 12),
            background = "#B1D3B9",
            foreground = "#303841",
            activebackground = "black",
            activeforeground = "white",
            variable = x,
            onvalue = 1,
            offvalue = 0,
            command = delete
            )

            #retrieves the task_entry input
            new_task = task_entry.get()

            #Appends each checkbutton to contain the new input
            task_display.configure(text =f"{new_task}")
            task_display.pack()

        #The user can enter their own tasks for the category here
        task_submit = Button(
        listbox_item_frame,
        text = "+",
        font = ('Arial', 12, "bold"),
        #command is tied into a premade function
        command = submit,
        background = "#B1D3B9",
        foreground = "white",
        activebackground = "grey",
        activeforeground = "red",
        )
        task_submit.grid(row = 2, column = 1)

        #the listbox_item_frame is returned so, another button can delete the category later (doesn't work just yet)
        return listbox_item_frame

        

    #When activated, a category is deleted from the list
    def delete_category():
        listbox_item_frame = add_category()
        listbox_item_frame.destroy()


    #The button tied to add_category function
    category_insert = Button(
        listbutton_frame,
        text = "+",
        background = "#B1D3B9",
        foreground = "white",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 12),
        command = add_category,
    )
    category_insert.grid(row = 0, column = 0)


    #The button tied to delete_category function
    category_delete = Button(
        listbutton_frame,
        text = "-",
        background = "#B1D3B9",
        foreground = "white",
        activebackground = "grey",
        activeforeground = "red",
        font = ("Aerial", 12),
        command = delete_category)
    category_delete.grid(row = 0, column = 1)


    #places window on screen
    window.mainloop()

    
productivity_tracker()
</py-script>
</body>
</html>
