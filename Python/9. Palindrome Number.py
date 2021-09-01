class Solution:
    def IsPalindrome(self, x):
        limite_superior = 2 ** 31 - 1
        limite_inferior = -(limite_superior + 1)

        if x < limite_superior and x > limite_inferior:
            # transforma em string
            numero_string = str(x)
            aux = str(x)
            # fatia e coloca em uma lista
            lista = [i for i in numero_string]

            # reverse
            lista.reverse()

            # transforma em int
            numero_string = ''
            for i in lista:
                numero_string += f'{i}'

                # compara se sao iguais (return True/false)
                return True if aux == numero_string else False

        else:
            return False
