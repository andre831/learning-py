class Carro:
    def __init__(self, cor, marca, ano, portas):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.portas = portas

    def entrar(self):
        print('entrei no carro')
    
    def ligar(self):
        print('carro está ligado')
    
    def andar(self,contador):
        if(contador >= 2):
          for contador in range(2,90):
            print('carro está andando')
            if (contador == 70):
                print('carro está na velocidade máxima')
            elif (contador == 72):
               while (contador == 72):
                contador = contador - 20
                print('desacelerando')


carro1 = Carro('Preto', 'Fiat', 2008, 2)
carro1.entrar()
carro1.ligar()
carro1.andar(3)
             
                   

              

            