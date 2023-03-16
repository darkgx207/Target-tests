print("======= Invesor de Strings ======= \n")
string = input('Digite uma string para ser invertida: ')
temp = []
for i in range(len(string)):
    temp.insert(0,string[i])

string = ''.join(temp)
print(string)