#valor absoluto
def abs_if_else(valor):
       if valor < 0:
           return -valor
       else:
           return valor
       
#Método usando operador ternário
def abs_ternario(valor):
     return -valor if valor < 0 else valor

#Método para calcular somatório de 0 com for
def somatorio_for(n):
     soma = 0
     for i in range (n+1):
          soma += i
     return soma

#Método para calcular somatório de 0 com while
def somatorio_while(n):
     soma = 0
     i = 0
     while i <= n:
          soma += i
          i += 1
     return soma

#Método para calcular somatório de 0 até n usando do-while
def somatorio_do_while(n):
     soma = 0
     i = 0
     while True:
          soma += i
          i += 1
          if i > n:
               break
     return soma

#testes 
print("Valor absoluto (if-else): ", abs_if_else(-10))
print("Valor absoluto (ternário): ", abs_ternario(-10))
print("Valor absoluto (for): ", somatorio_for(10))
print("Valor absoluto (while): ", somatorio_while(10))
print("Valor absoluto (do-while): ", somatorio_do_while(10))