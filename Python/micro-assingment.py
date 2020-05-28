


file = open("all.cpp","r")
data = file.readlines()

list_function_index=[]
list_function_name=[]
list_function_variable=[]


list_firstbracket=[]
list_lastbracket=[]
list_maindata=[]

list_initalization_index=[]





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
        if x.find("int") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find("main") == -1 and x.find(";") == -1:
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

def find_mainfunction():
    control = 0
    for x in data:
        if control == 1:
            list_maindata.append(x)
        if x.find("main") != -1 and x.find("(") != -1 and x.find(")") != -1 and x.find(";") == -1:
            control = 1
    print(list_maindata)
    for y in list_maindata:
        for z in list_function_name:
            if y.find(z) != -1:
                print(y)

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





find_function()
find_bracket()
find_mainfunction()


print("Function index:")
print(list_function_index)
# print("Function name:")
# print(list_function_name)
print("Bracket index:")
print(list_firstbracket)
print("Bracket index:")
print(list_lastbracket)
