/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

 
 var twoSum = function(nums, target) {
        let values= new Array()
        let positionNum = new Array()
        const reducer = (acumulador, valorAtual) => acumulador + valorAtual
        
        for (i=0; i<nums.length;i++){
        
            //verifica se existe o valor do target na lista 
            if (nums.indexOf(target,0)>=0) {
                positionNum.push(nums.indexOf(target,0))
                values.push(nums[nums.indexOf(target,0)])
                break
            } 
            // verifica se a lista está vazia ou se o elemento a ser inserido é menor que o target            
            else if(values == 0 || nums[i]<target){
                values.push(nums[i])  // neste caso todos os valores menores do que o target serão inseridos na lista  
            } 
                
                if (values.reduce(reducer)>=target){
                    for(c=0;c<values.length;c++){
                        let soma = values.reduce(reducer)
                        if(soma == target)
                        {
                            //laço para obter as posicoes dos numeros
                            for(x=0;x<values.length;x++){
                                positionNum.push(nums.indexOf(values[x]))
                            }
                            break
                        }
                        values.shift()
                    }
                    break
                }

        }
        // apos inseridos os valores menores do que o target, um novo laço deve ser criado para verificar quais somados serão iguais ao target
        
        return console.log(positionNum)
    
    }

twoSum([3,3], 6)

