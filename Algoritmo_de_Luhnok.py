'''Algoritmo de Luhn/ validação de cartão de crédito'''

num = str(input("Digite o número do cartão: ")).strip()
numint = int(num)
rest1= 1
rest = numint//rest1 %10
lista = list()
cont = 0
while cont < len(num):   
    lista.insert(0,rest)
    rest1 = rest1*10
    rest = numint//rest1 %10  
    cont = cont + 1

lista1 = list()
lista1_1 = list ()
lista2 = list()
somalista1_1 = 0
for i, v in enumerate(lista):
    if i % 2 ==0:
        a = v*2
        if a > 9:
            lista1_1.append(a)
            somalista1_1 = 0
            for i, v  in enumerate(lista1_1):
                somalista1_1 = somalista1_1 + lista1_1[i]//1%10
                somalista1_1= somalista1_1 + lista1_1[i]//10%10
            
        else:
            lista1.append(a)
        
    elif i % 2 != 0:
            lista2.append(v)        
    
somalista1 = 0
for i, v in enumerate(lista1):
    somalista1 = somalista1+ v
    
somalista2 = 0
for i, v in enumerate(lista2):
    somalista2 = somalista2 + v
soma = somalista1 + somalista2 + somalista1_1
final = soma//1%10
print(f'O número digitado foi: {lista}')
if final == 0:
    print('Cartão Cadastrado com sucesso!')
else:
    while final != 0:
        print('Cartão inválido!')
        num = str(input("Digite o número do cartão: "))

if lista[0] == 4:
    print('Visa')

else:
    print(' ')

    
    
    



    