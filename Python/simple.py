list_function_data=[]
list_function_name=[]
list_maindata=[]
operations = ["+","-","*","=","&&","||"]


def find_function():
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


def find_mainfunction():
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
                print("Burda:{0}".format(y))
                temp_text = y
                temp_text = temp_text.replace(temp_text[:temp_text.find("(")], "")
                temp_text = temp_text.replace("(", "").replace(")", "").replace("\n", "").replace(";", "").replace(" ", "")
                while temp_text.find(",") != -1:
                    number1 = (temp_text[:temp_text.find(",")])
                    temp_text = temp_text.replace(temp_text[:temp_text.find(",") + 1], "")
                if 'number1' in locals():
                    number2 = temp_text
                    file.write("\tMOV.B   #"+number2+", R13\n\tMOV.B   #"+number1+", R12\n")
                    file.write("\tCALL    #" + z + "(int, int)\n\tMOV.W   R12, -" + str((temp * 2)) + "(R4)\n")

    if temp == 0:
        file.write("\tMOV.B   #0, R12\n\tADD.W   #4, R1\n\tPOPM.W  #1, r4\n\tRET\n")
    else:
        file.write("\tMOV.B   #0, R12\n\tADD.W   #"+str((temp*2))+"  R1\n\tPOPM.W  #1, r4\n\tRET\n")



file = open("all.cpp","r")
data = file.readlines()
file = open("output.txt","w")

for x in data:
    if x.find("#include") != -1:
        data.pop(data.index(x))
# DATA HAZIR
print("--------------------------------")

find_function()
find_mainfunction()

print("Function name:")
print(list_function_name)
print("Function data:")
print(list_function_data)
if list_function_data[0] == ['']:
    print("yesssss")
print("Main data :")
print(list_maindata)
file.close()
