Algoritmo de Luhn
# Validador_cartao_de_credito
Testa números para saber se o cartão é válido.
Fórmula matemática: Ex: 4024007137015284
[4, 0, 2, 4, 0, 0, 7, 1, 3, 7, 0, 1, 5, 2, 8, 4] Multiplica os numeros na posição par, por 2:
[14, 10, 16] se o resultado possuir dois dígitos, soma um digito com o outro.
[8, 4, 0, 6, 0] 
[0, 4, 0, 1, 7, 1, 2, 4] soma os digitos da posição impar.
Se o resultado final possuir o ultimo dígito 0: o cartão é válido.
