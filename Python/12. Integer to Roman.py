class Solution:
    def intToRoman(self, num):
        unidade = {'0': '',
                   '1': 'I',
                   '2': 'II',
                   '3': 'III',
                   '4': 'IV',
                   '5': 'V',
                   '6': 'VI',
                   '7': 'VII',
                   '8': 'VIII',
                   '9': 'IX'}

        dezena = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L',
                  '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}

        centena = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D',
                   '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}

        milhar = {'0': '', '1': 'M', '2': 'MM', '3': 'MMM'}
        numero_romano = ''


        # converto para string
        numero_string = str(num)

        # corto e coloco numa lista

        lista = [i for i in numero_string]

        # verificar se o tamano é igual a 4
        if len(lista) == 4:

            numero_romano += milhar[f'{lista[0]}']
            numero_romano += centena[f'{lista[1]}']
            numero_romano += dezena[f'{lista[2]}']
            numero_romano += unidade[f'{lista[3]}']

        # verificar se o tamano é igual a 3
        elif len(lista) == 3:
            numero_romano += centena[f'{lista[0]}']
            numero_romano += dezena[f'{lista[1]}']
            numero_romano += unidade[f'{lista[2]}']

        # verificar se o tamano é igual a 2
        elif len(lista) == 2:
            numero_romano += dezena[f'{lista[0]}']
            numero_romano += unidade[f'{lista[1]}']

        # verificar se o tamano é igual a 1
        elif len(lista) == 1:
            numero_romano += unidade[f'{lista[0]}']


        return numero_romano

