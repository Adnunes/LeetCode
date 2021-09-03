class Solution:
    def roman_to_integer(self,s):
        lista = []
        sistema_numeracao_romana = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        excecoes = {4: ['IV', 4], 9: ['IX', 9], 40: ['XL', 40], 90: ['XC', 90], 400: ['CD', 400],
                    900: ['CM', 900]}

        # um laço procurando as excecoes
        for i in excecoes.keys():
            numero_romano = excecoes[i][0]
            numero = excecoes[i][1]

            if s.find(numero_romano) != -1:
                lista.append(numero)
                s = s.replace(numero_romano, '')

        if s != '':
            for i in s:
                lista.append(sistema_numeracao_romana[i])
                s = s.replace(i, '')

        return sum(lista)

teste = Solution()
print(teste.roman_to_integer('CMXCIII'))