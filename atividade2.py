import math
#Passo 1: Definir a classe circulo
class Circulo:
    #Passo 2: Criar uma constante estática de PI
    PI = math.pi


    #Passo 3: Criar o construtor padrão e os atributos
    def __int__(self, raio=1.0, cor="Branco"):
        """
        Construtor padrão. Se nenhum valor for passado, assume raio=1.0 e cor=Branco
        """
        self.raio = raio # Atributo raio
        self.cor = cor # Atributo cor
        self.circunference = self.calcCircunferencia() # Calcula a circunferência ao iniciar 
