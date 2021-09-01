''' Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).'''

class Solution:
    def reverse(self, x:int)->int:
        limite = 2 ** 31
        limite_superior = limite - 1
        limite_inferior = -limite
        lista = []

        # verifica se é 32bits
        if x < limite_superior and x > limite_inferior:
            numero_string = str(abs(x))

            # corta e coloca em uma lista
            for i in numero_string:
                lista.append(i)

            # inverte o numero
            lista.reverse()
            numero_string = ''

            # concatena numa string
            for i in lista:
                numero_string += i

            # verifica se o numero é negativo
            if x > 0:
            # converte em inteiro
                numero = int(numero_string)
                return numero if numero<limite_superior else 0
            else:
                # converte em inteiro negativo
                numero = -(int(numero_string))
                return numero if numero > limite_inferior else 0
        else:
            return 0


teste = Solution()
print(teste.reverse(1534236469))