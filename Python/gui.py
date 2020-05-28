import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import os

root = tk.Tk()

text = tk.Label(root, text="EED3018 Microprocessor Systems Assigmnet")
text.pack(side=tk.TOP)

statusbar = tk.Label(root, text="Furkan Aslan HATIK", relief=tk.GROOVE)  # SUNKEN
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

list_files = []
path_files = []

# Assembly data
list_function_data=[]
list_function_name=[]
list_maindata=[]
operations = ["+","-","*","=","&&","||"]

# Functions

def about_me():
    tk.messagebox.showinfo("Contact", "Please contact via furkanhtk@gmail.com ")

def open_browser():
    file_path = tk.filedialog.askopenfilename(
        filetypes=(("C++ Source File", "*.cpp"), ("C Source File", "*.c"), ("all files", "*.*")))
    list_files.append(file_path)
    if list_files[-1] == '':
        list_files.pop(-1)
        information['text'] = " "
    else:
        information['text'] = "{0} added".format(os.path.basename(list_files[-1]))
        add_to_listbox()

def add_to_listbox():
    files_list_box1.insert(tk.END, os.path.basename(list_files[-1]))

def delete_from_listbox():
    selected_file = files_list_box1.curselection()
    selected_file_index = int(selected_file[0])
    list_files.pop(selected_file_index)
    files_list_box1.delete(selected_file)

def delete_all_listbox():
    list_files.clear()
    path_files.clear()
    files_list_box1.delete(0, tk.END)

def covert_files():
    selected_file = files_list_box1.curselection()
    selected_file_index = int(selected_file[0])
    file2 = open(list_files[selected_file_index], "r")
    data = file2.readlines()
    save_location = list_files[selected_file_index].replace(".cpp",".txt").replace(".c",".txt")
    file = open(save_location, "w")

    for x in data:
        if x.find("#include") != -1:
            data.pop(data.index(x))
    # DATA HAZIR
    for x in data:
        if x.find("int") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find("main") == -1 and x.find(";") == -1:
            text = x.replace("int", "").replace(" ", "").replace("\n", "")
            function_name_temp = text[:text.find("(")]
            file.write(function_name_temp + "(")
            list_function_name.append(function_name_temp)
            function_name_temp = []
            text = text.replace(text[:text.find("(")], "")
            text = text.replace("(", "").replace(")", "")
            while text.find(",") != -1:
                function_name_temp.append(text[:text.find(",")])
                text = text.replace(text[:text.find(",")+1], "")
            function_name_temp.append(text)
            list_function_data.append(function_name_temp)
            if list_function_data[0] != ['']:
                file.write("int, int):\n")
            else:
                file.write("):\n")
            file.write("\tPUSHM.W #1, R4\n\tMOV.W   R1, R4\n\tSUB.W   #4, R1\n\tMOV.W   R12, -2(R4)\n\tMOV.W   R13, -4(R4)\n")
        for y in operations:
            temp_forandor = 1
            if x.find(y) != -1:
                x = x.replace(" ", "").replace(";", "").replace("return", "")
                if y == "+":
                    temp1 = x[:x.find("+")]
                    x = x.replace(x[:x.find("+")], "")
                    x = x.replace("+", "")
                    temp2 = x
                    # TO DO
                    file.write("\tMOV.W   -2(R4), R12\n\tADD.W   -4(R4), R12\n")
                    file.write("\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
                elif y == "-":
                    temp1 = x[:x.find("-")]
                    x = x.replace(x[:x.find("-")], "")
                    x = x.replace("-", "")
                    temp2 = x
                    # TO DO
                    file.write("\tMOV.W   -2(R4), R12\n\tSUB.W   -4(R4), R12\n")
                    file.write("\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
                elif y == "*":
                    temp1 = x[:x.find("*")]
                    x = x.replace(x[:x.find("*")], "")
                    x = x.replace("*", "")
                    temp2 = x
                    # TO DO
                    # Function for write
                    file.write("\tMOV.W   -4(R4), R13\n\tMOV.W   -2(R4), R12\n\tCALL    #__mspabi_mpyi\n")
                    file.write("\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
                elif y == "&&":
                    temp_forandor += 1
                    temp1 = x[:x.find("&&")]
                    x = x.replace(x[:x.find("&&")], "")
                    x = x.replace("&&", "")
                    temp2 = x
                    # TO DO
                    file.write("\tCMP.W   #0, -2(R4) { JEQ      .L" + str(temp_forandor) + "\n")
                    file.write("\tCMP.W   #0, -4(R4) { JEQ      .L" + str(temp_forandor) + "\n")
                    file.write("\tMOV.B   #1, R12\n")
                    file.write("\tBR  # .L"+str(temp_forandor+1)+"\n")
                    file.write(".L" + str(temp_forandor) + ":\n")
                    file.write("\tMOV.B   #0, R12\n")
                    file.write(".L"+str(temp_forandor+1)+":\n")
                    file.write("\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
                elif y == "||":
                    temp_forandor += 5
                    temp1 = x[:x.find("||")]
                    x = x.replace(x[:x.find("||")], "")
                    x = x.replace("||", "")
                    temp2 = x
                    # TO DO
                    file.write("\tCMP.W   #0, -2(R4) { JNE      .L" + str(temp_forandor) + "\n")
                    file.write("\tCMP.W   #0, -4(R4) { JEQ      .L" + str(temp_forandor+1) + "\n")
                    file.write(".L" + str(temp_forandor) + ":\n")
                    file.write("\tMOV.B   #1, R12\n")
                    file.write("\tBR  # .L"+str(temp_forandor+2)+"\n")
                    file.write(".L" + str(temp_forandor+1) + ":\n")
                    file.write("\tMOV.B   #0, R12\n")
                    file.write(".L"+str(temp_forandor+2)+":\n")
                    file.write("\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
    file.write("main:\n\tPUSHM.W #1, R4\n\tMOV.W   R1, R4\n\tSUB.W   #4, R1\n")
    control = 0
    temp = 0
    for x in data:
        if control == 1:
            list_maindata.append(x)
        if x.find("main") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find(";") == -1:
            control = 1
    for y in list_maindata:
        for z in list_function_name:
            if y.find(z) != -1:
                temp += 1
                temp_text = y
                temp_text = temp_text.replace(temp_text[:temp_text.find("(")], "")
                temp_text = temp_text.replace("(", "").replace(")", "").replace("\n", "").replace(";", "").replace(" ",
                                                                                                                   "")
                while temp_text.find(",") != -1:
                    number1 = (temp_text[:temp_text.find(",")])
                    temp_text = temp_text.replace(temp_text[:temp_text.find(",") + 1], "")
                if 'number1' in locals():
                    number2 = temp_text
                    file.write("\tMOV.B   #" + number2 + ", R13\n\tMOV.B   #" + number1 + ", R12\n")
                    file.write("\tCALL    #" + z + "(int, int)\n\tMOV.W   R12, -" + str((temp * 2)) + "(R4)\n")

    if temp == 0:
        file.write("\tMOV.B   #0, R12\n\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
    else:
        file.write("\tMOV.B   #0, R12\n\tADD.W   #" + str((temp * 2)) + "  R1\n\tPOPM.W  #1, r4\n\tRET\n")

    file.close()
    file2.close()


# Layout

left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=30)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT)

# Create the menubar

menubar = tk.Menu(root)
root.config(menu=menubar)

# Create the submenu

subMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Exit", command=root.destroy)
subMenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About me", command=about_me)

# Configure size and icons

# root.geometry('800x500')  # set to size of program
root.title("EED 3018 Microprocessor Systems Term Homework")  # title of the program
#root.iconbitmap(r'./icons/pdf.ico')  # change icon of program



# Labels (RIGHT)

button_convert = tk.Button(right_frame, text="CONVERT", command=covert_files)
button_convert.pack()
varCheckButton = tkinter.IntVar()

# -----------------------------------------------------------------------------------------------------------------------------
if not list_files:
    information = tk.Label(right_frame, text="")
    information.pack(side=tk.BOTTOM, fill=tk.X)

    # List Box (LEFT)
    files_list_box1 = tk.Listbox(left_frame, selectmode=tk.EXTENDED)
    files_list_box1.pack()

# Buttons (LEFT)

button_add = tk.Button(left_frame, text="Open Browser", command=open_browser)
button_add.pack(side=tk.LEFT)
button_delete = tk.Button(left_frame, text="Delete" ,command=delete_from_listbox)
button_delete.pack(side=tk.LEFT)
button_delete2 = tk.Button(left_frame, text="Delete All", command=delete_all_listbox)
button_delete2.pack(side=tk.LEFT)


root.mainloop()
