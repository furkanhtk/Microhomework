# Bu program ile cpp dosya içeri okunup parse edilcektir.
file = open("denem1.cpp","r")
data = file.read()



# list.append()
print(type(data))

for x in  range(36,50):
    print("{0} index:{1}".format(x,data[x]))

