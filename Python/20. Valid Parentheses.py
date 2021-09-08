class Solution:
    def isValid(self, s: str) -> bool:
        dicionario_parenteses_invertido = {')': '(', '}': '{', ']': '['}
        dicionario_parenteses = {'(': ')', '{': '}', '[': ']'}
        lista = []
        c = 0
        lista_aux = []
        resto_div = 0
        if len(s)>1 and len(s)%2==0:
            for i in s:
                lista.append(s[c])
                c += 1

            for chave in lista:

                if chave in dicionario_parenteses.keys():
                    if (dicionario_parenteses[chave] in lista):
                        lista_aux = lista[lista.index(chave):lista.index(dicionario_parenteses[chave]) + 1]
                        resto_div += len(lista_aux) % 2
                        lista.remove(dicionario_parenteses[chave])
                        lista.remove(chave)
                        if len(lista)%2 != 0:
                            return False
                    else:
                        return False
            if len(lista)!= 0:
                return False

        else: return False

        return True if resto_div == 0 else False

s="(){}}{"
teste = Solution()
print(teste.isValid(s))
