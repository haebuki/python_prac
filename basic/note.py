f= open('myfile.txt','r', encoding='UTF8')

while True:
    line = f.readline()
    if not line:
        break
    raw = line
    print(raw)
f.close()


with open('myfile.txt',encoding='UTF8')as file:
    for line in file.readlines():
        print(line.strip().split('\t'))