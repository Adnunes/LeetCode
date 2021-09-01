/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


 
 var twoSum = function(nums, target) {
        let values= new Array()
        let positionNum = new Array()
        const reducer = (acumulador, valorAtual) => acumulador + valorAtual
       
        let duplicatedNumbers = function(arrayNum){  
            let indexOfduplicatedNumber = new Array()

            for (i=0;i<arrayNum.length;i++){
              //pegar elemento por elemento e verificar cada posição
              let vereficarElemento = arrayNum[i]
              for(c=i+1; c<arrayNum.length; c++){
                  if(vereficarElemento == arrayNum[c] ){
                    if(indexOfduplicatedNumber.includes(i)==false){
                        indexOfduplicatedNumber.push(i)  
                        indexOfduplicatedNumber.push(c)      
        
                    }else if (indexOfduplicatedNumber.includes(c)==false)indexOfduplicatedNumber.push(c)
        
                  }
              }
        
            }
            return indexOfduplicatedNumber
        }

        
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
                                
                                if (duplicatedNumbers(values)!=0){
                                    if(x==0){
                                        positionNum.push(nums.indexOf(values[x]))
                                    }else {positionNum.push(nums.indexOf(values[x], -1))}

                                }else positionNum.push(nums.indexOf(values[x]))
                            }
                            break
                        }
                        values.shift()
                    }
                    break
                }

        }
        // apos inseridos os valores menores do que o target, um novo laço deve ser criado para verificar quais somados serão iguais ao target
        
        return positionNum
    
    }

twoSum([3,2,3], 6)
