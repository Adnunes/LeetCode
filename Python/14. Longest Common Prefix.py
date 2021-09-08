class Solution:
    def longest_common_prefix(self, strs):
        prefixo_comum = {}
        contador_de_palavras = 0
        contador=0
        palavra_cortada =""
        maior_prefixo = ""
        maior_numero = 0
        # acessando as palavras dentro da lista
        for palavra in strs:
            if palavra != "":
                while len(palavra_cortada)<len(palavra):
                    palavra_cortada += palavra[contador]

                    for palavra_segunda in strs:
                        if palavra.index(palavra_cortada) == palavra_segunda.index(palavra_cortada):
                            contador_de_palavras+=1
                        else:
                            break
                    if len(palavra_cortada)>len(maior_prefixo) and contador_de_palavras >= maior_numero:
                        maior_prefixo = palavra_cortada
                        maior_numero = contador_de_palavras
                    contador+=1
                    contador_de_palavras = 0
                return maior_prefixo

            else:
                return ""





strs = ["dog","racecar","car"]


teste = Solution()
teste.longest_common_prefix(strs)

