file_path = "C:/Users/BT_4N2_18/PycharmProjects/pythonProject/input.txt"
with open(file_path, "r") as f:
    content = f.read()



twoDArray = []
array = []
safeCount = 0
for i in content:
    if i != "\n":
        array.append(i)
    else:
        twoDArray.append(array)
        array = []


sum = 0

#forwards(normal) and backwards
sum += content.count("XMAS")
sum += content.count("SAMX")


for i in twoDArray:
    for b in range(len(i)):
        if twoDArray[b] == "X" and b 








print(sum)