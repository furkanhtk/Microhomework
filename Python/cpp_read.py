
"""
Program yazılırken satır satır okunulmasına karar verilmiştir.
"""

# Bu program ile cpp dosya içeri okunup parse edilcektir.
list=[]
list_maindata=[]

operataions = ["<",">","==","<=",">="]
ar_log_operations = ["+","-","*","&&","||","=","<",">"]
list_firstbracket=[]
list_lastbracket=[]
# function
list_function_index=[]
list_function_name=[]
list_function_variable=[]
# for
list_for_index=[]
list_for_data=[]
# if else else if
list_ifcondition_index=[]
list_ifcondition_data=[]

#operation condition
list_operation_data=[]

file = open("all.cpp","r")
data = file.readlines()

print(type(data))
# for x in data:
#     if x.find("main()") != -1:
#         print(data.index(x))

for x in data:
    if x.find("#include") != -1:
        data.pop(data.index(x))
# DATA HAZIR
print("--------------------------------")

def find_bracket():
    end_of_bracket = 0
    obj = enumerate(data)
    for i,x in obj:
        if x.find("{") != -1:
            end_of_bracket += 1
            list_firstbracket.append(i)
        elif x.find("}") != -1:
            list_lastbracket.append(i)
    print(end_of_bracket)

def find_function():
    for x in data:
        if x.find("int") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find("main") == -1 and x.find(
                ";") == -1:
            list_function_index.append(data.index(x))
    for x in list_function_index:
        text = data[x].replace("int", "").replace(" ", "").replace("\n", "")
        # print("formatlanan {}".format(text))
        function_name_temp = text[:text.find("(")]
        list_function_name.append(function_name_temp)
        function_name_temp = []
        text = text.replace(text[:text.find("(")], "")
        text = text.replace("(", "").replace(")", "")
        while text.find(",") != -1:
            list_function_variable.append(text[:text.find(",")])
            function_name_temp.append(text[:text.find(",")])
            text = text.replace(text[:text.find(",") + 1], "")
        list_function_variable.append(text)
        function_name_temp.append(text)

def find_mainfunction():
    control = 0
    for x in data:
        if control == 1:
            list_maindata.append(x)
        if x.find("main") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find(";") == -1:
            control = 1
    for y in list_maindata:
        for z in list_function_name:
            if y.find(z) != -1:
                print("buldum")

def find_initialization():
    for x in data:
        if x.find("int") != -1 and x.find(";") != -1:
            list_initalization_index.append(data.index(x))
        for x in list_function_index:
            text = data[x].replace("int", "").replace(" ", "").replace("\n", "").replace(";", "")
            # print("formatlanan {}".format(text))
            function_name_temp = text[:text.find("(")]
            list_function_name.append(function_name_temp)
            function_name_temp = []
            text = text.replace(text[:text.find("(")], "")
            text = text.replace("(", "").replace(")", "")
            while text.find(",") != -1:
                list_function_variable.append(text[:text.find(",")])
                function_name_temp.append(text[:text.find(",")])
                text = text.replace(text[:text.find(",") + 1], "")
            list_function_variable.append(text)
            function_name_temp.append(text)


def find_for():
    for x in data:
        if x.find("for") != -1 and x.find("(") != -1 and x.find(")") != -1:
            list_for_index.append(data.index(x))
    for x in list_for_index:
        text = data[x].replace("for", "").replace(" ", "").replace("\n", "")
        text = text.replace("(", "").replace(")", "")
        text = text.split(";")
        variable = text[0][:text[0].find("=")]
        list_for_data.append(variable)
        variable_start = text[0][text[0].find("=")+1:]
        list_for_data.append(variable_start)
        if text[1][text[0].find(variable) + 2].isnumeric() == True:
            variable_conditon = text[1][text[0].find(variable) + 1]
            list_for_data.append(variable_conditon)
        else:
            variable_conditon = text[1][text[0].find(variable) + 1:text[0].find(variable) + 3]
            list_for_data.append(variable_conditon)
        change = text[2].replace(variable, "")
        list_for_data.append(change)
        #print("Variable : {0},variable_start : {1},variable_conditon : {2},change : {3} ".format(variable,variable_start,variable_conditon,change))

def find_ifconditon():
    for x in data:
        if x.find("if") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find("else") ==-1:
            list_ifcondition_index.append(data.index(x))
    for x in list_ifcondition_index:
        text = data[x].replace("if", "").replace(" ", "").replace("\n", "").replace("{", "")
        text = text.replace("(", "").replace(")", "")
        for y in operataions:
            if text.find(y) != -1:
                list_ifcondition_data.append(y)
                temp=text.split(y)
                for z in temp:
                    list_ifcondition_data.append(z)

def find_Ar_Log_fundtions():
    for x in data:
        if x.find("#") != -1 and x.find("include") != -1 :
            data.pop(data.index(x))
    for x in data:
        for y in ar_log_operations:
            if x.find(y) != -1:
                x=x.replace(" ", "").replace(";", "").replace("return","")
                list_operation_data.append(y)






find_bracket()
find_function()
#find_for()
#find_ifconditon()
find_Ar_Log_fundtions()
find_mainfunction()
print(list_firstbracket)
print(list_lastbracket)
print("main data:")
print(list_maindata)
print("Function index:")
print(list_function_index)
print("Function name:")
print(list_function_name)
print("Function variable:")
print(list_function_variable)
# print("for data:")
# print(list_for_data)
# print("if else data:")
# print(list_ifcondition_data)
print("operation data:")
print(list_operation_data)



