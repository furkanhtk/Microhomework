
"""
Program yazılırken satır satır okunulmasına karar verilmiştir.
"""

# Bu program ile cpp dosya içeri okunup parse edilcektir.
list=[]
list_firstbracket=[]
list_lastbracket=[]
list_function_index=[]
list_function_name=[]
list_function_variable=[]

file = open("sum.cpp","r")
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
        print("formatlanan {}".format(text))
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
        print(function_name_temp)




        # list_function_variable.append(text[text.find("(")+1:text.find(",")])
        # text = text.replace(text[:text.find(",")], "")
        # print(text)






find_bracket()
find_function()
# print(list_firstbracket)
# print(list_lastbracket)
# print(list_function_index)
print(list_function_name)
print(list_function_variable)



