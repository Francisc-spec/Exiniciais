tipoValor = input('digite algo')
print('O tipo primitivo desse valor é', type(tipoValor))
print('Só tem espaços?', tipoValor.isspace())
print('É um número?', tipoValor.isnumeric())
print('É alfabético?', tipoValor.isalpha())
print('É alfanumérico?', tipoValor.isalnum())
print('Está em maiúscula?', tipoValor.isupper())
print('Está em minúscula?', tipoValor.islower())
print('Está capitalizada?', tipoValor.istitle())
