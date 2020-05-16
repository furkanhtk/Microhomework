
"""
Program yazılırken satır satır okunulmasına karar verilmiştir.
"""

# Bu program ile cpp dosya içeri okunup parse edilcektir.
list=[]
list_firstbracket=[]
list_lastbracket=[]
# function
list_function_index=[]
list_function_name=[]
list_function_variable=[]

# for
list_for_index=[]
list_for_variable=[]
# if else else if



file = open("for.cpp","r")
data = file.readlines()

print(type(data))
# for x in data:
#     if x.find("main()") != -1:
#         print(data.index(x))


def find_bracket():
    for x in data:
        if x.find("{")!= -1:
            list_firstbracket.append(data.index(x))
    for x in data:
        if x.find("}")!= -1:
            list_lastbracket.append(data.index(x))

def find_function():
    for x in data:
        if x.find("int") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find("main") == -1:
            list_function_index.append(data.index(x))
    for x in list_function_index:
        text = data[x].replace("int", "").replace(" ", "").replace("\n", "")
        #print("formatlanan {}".format(text))
        function_name_temp = text[:text.find("(")]
        list_function_name.append(function_name_temp)
        function_name_temp = []
        text = text.replace(text[:text.find("(")], "")
        text = text.replace("(", "").replace(")", "")
        while text.find(",") != -1:
            list_function_variable.append(text[:text.find(",")])
            function_name_temp.append(text[:text.find(",")])
            text = text.replace(text[:text.find(",")+1], "")
        list_function_variable.append(text)
        function_name_temp.append(text)

def find_for():
    for x in data:
        if x.find("for") != -1 and x.find("(") != -1 and x.find(")") != -1:
            list_for_index.append(data.index(x))
    for x in list_for_index:
        text = data[x].replace("for", "").replace(" ", "").replace("\n", "")
        text = text.replace("(", "").replace(")", "")
        text=text.split(";")
        variable = text[0][:text[0].find("=")]
        variable_start=text[0][text[0].find("=")+1:]
        if text[1][text[0].find(variable) + 2].isnumeric() == True:
            variable_conditon = text[1][text[0].find(variable) + 1]
        else:
            variable_conditon = text[1][text[0].find(variable) + 1:text[0].find(variable) + 3]
        change = text[2].replace(variable, "")
        print("Variable : {0},variable_start : {1},variable_conditon : {2},change : {3} ".format(variable,variable_start,variable_conditon,change))








find_bracket()
find_function()
find_for()
# print(list_firstbracket)
# print(list_lastbracket)
# print(list_function_index)
# print(list_function_name)
# print(list_function_variable)




