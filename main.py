import csv,math
def conf_inicial(mapa):
    for indice1,linhas in enumerate(mapa):
        for indice2,elemento in enumerate(linhas):
            if(elemento=='13'):
                coords_objetivo=[int(indice1),int(indice2)]
                # print('♕ ',end='')
            # elif(elemento=='14'):
            #     print('■ ',end='')
            # elif(elemento=='15'):
            #     print('□ ',end='')
            # elif(elemento=='16'):
            #     print('⊞ ',end='')
            # elif(elemento=='17'):
            #     print('✘ ',end='')
            elif(elemento=='00'):
                local_atual=[int(indice1),int(indice2)]
            #     print('ꚰ ',end='') #♟
            # else:
            #     print(elemento,end='')
        # print()
    return coords_objetivo,local_atual


def imprime_mapa(mapa):
    for indice1,linhas in enumerate(mapa):
        for indice2,elemento in enumerate(linhas):
            if(elemento=='13'):
                print('♕ ',end='')
            elif(elemento=='14'):
                print('■ ',end='')
            elif(elemento=='15'):
                print('□ ',end='')
            elif(elemento=='16'):
                print('⊞ ',end='')
            elif(elemento=='17'):
                print('✘ ',end='')
            elif(elemento=='18'):
                print('♟ ',end='')    
            elif(elemento=='00'):
                print('ꚰ ',end='')
            else:
                print(elemento,end='')
        print()


def distancia(local1,local2):
    return math.sqrt((local1[0]-local2[0])**2+(local1[1]-local2[1])**2)

poder_cavaleiro={}
with open('poder_cavaleiro.csv','r',encoding='utf-8') as file:
    poder_cavaleiros_csv=csv.reader(file,delimiter=',')
    for i in poder_cavaleiros_csv:
        poder_cavaleiro[i[0]]=i[1]
        
coords_mapa=[]
with open('mapa.csv','r',encoding='utf-8') as file:
    mapa=csv.reader(file,delimiter=',')
    for i in mapa:
        coords_mapa.append(i)

local_atual=[]
coords_objetivo=[]

coords_objetivo,local_atual=conf_inicial(coords_mapa)

def mover(local,mapa):
    preferencia=['15','16','17','14']
    escolher=''
    for i in preferencia:
        if(local[0]-1>0 and mapa[local[0]-1][local[1]]==i):
            escolher='cima'
            break
        elif(local[1]-1>0 and mapa[local[0]][local[1]-1]==i):
            escolher="esq"
            break
        elif(local[0]+1<len(mapa) and mapa[local[0]+1][local[1]]==i):
            escolher="baixo"
            break
        elif(local[1]+1<len(mapa) and mapa[local[0]][local[1]+1]==i):
            escolher='dir'
            break
    match(escolher):
        case 'cima':
            local[0]=local[0]-1
            mapa[local[0]][local[1]]='18'
            mapa[local[0]+1][local[1]]='17'
        case 'esq':
            local[1]=local[1]-1
            mapa[local[0]][local[1]]='18'
            mapa[local[0]][local[1]+1]='17'
        case 'baixo':
            local[0]=local[0]+1
            mapa[local[0]][local[1]]='18'
            mapa[local[0]-1][local[1]]='17'
        case 'dir':
            local[1]=local[1]+1
            mapa[local[0]][local[1]]='18'
            mapa[local[0]][local[1]-1]='17'

# while(distancia(coords_objetivo,local_atual)!=0.0):
#     mover(local_atual,mapa)
#     coords_objetivo,local_atual=imprime_mapa(coords_mapa)

for i in range(65):
    mover(local_atual,coords_mapa)
    imprime_mapa(coords_mapa)
