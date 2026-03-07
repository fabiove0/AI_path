import csv
poder_cavaleiro={}

with open('poder_cavaleiro.csv','r',encoding='utf-8') as file:
    poder_cavaleiros_csv=csv.reader(file,delimiter=',')
    for i in poder_cavaleiros_csv:
        poder_cavaleiro[i[0]]=i[1]

with open('mapa.csv','r',encoding='utf-8') as file:
    mapa=csv.reader(file,delimiter=',')
    for i in mapa:
        for j in i:
            print(j, end=' ')
        print()
