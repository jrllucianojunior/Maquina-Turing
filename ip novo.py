class MaquinaTuringIPv4Validator:
    def __init__(self, quintuplas):
        self.quintuplas = quintuplas
        self.estado_atual = quintuplas['q0']
        self.cabecote_posicao = 0
        self.fita = ['B'] * 100
        self.erro = None
        self.QuantidadePontos = 0
    
    def executar_passo(self):
        estado = self.estado_atual
        simbolo_lido = self.fita[self.cabecote_posicao]

        if ((estado) in ('q1','q2','q3')) and (simbolo_lido == '.'):#adicionado
            self.QuantidadePontos = self.QuantidadePontos + 1

        if (self.QuantidadePontos < 4):  #adicionado
         print(f"Atual posição do cabeçote: {self.cabecote_posicao}, Estado: {estado}, Símbolo lido: {simbolo_lido}")
        # print(self.QuantidadePontos)
         if (estado, simbolo_lido) not in self.quintuplas['δ']:
             self.erro = f"Transição não definida para o estado {estado} e símbolo {simbolo_lido}"
             return False
         
         nova_config = self.quintuplas['δ'][(estado, simbolo_lido)]
         self.estado_atual = nova_config[0]
         self.fita[self.cabecote_posicao] = nova_config[1]
        
         if nova_config[2] == 'R':
               self.cabecote_posicao += 1
         elif nova_config[2] == 'L':
               self.cabecote_posicao -= 1
         
         return True
        else:
           print('Já foram encontrados mais de 3 pontos dos octetos, IP inválido')
           return False

    def executar(self, entrada):
        self.fita[:len(entrada)] = entrada
           
        
        while self.estado_atual not in self.quintuplas['qf'] and self.estado_atual not in self.quintuplas['qErro']:
            if not self.executar_passo():
                print("Erro:", self.erro)
                return False
        
        if self.QuantidadePontos != 3:
         print(f"IP inválido: encontrado(s) {self.QuantidadePontos} ponto(s). Exatamente 3 pontos são necessários.")
         return False

        return self.estado_atual in self.quintuplas['qf']


# Definição das quintuplas para validar endereços IPv
quintuplas_ipv4_validator = {
    'Q': {'q0', 'q1', 'q2', 'q3','q15','qErro','qteste1', 'qteste1', 'qteste2','qteste1.1', 'qteste1.2', 
          'qteste1.3', 'qteste1.1veseeh5'
          'qteste1.13veseeh5'
          },  # Conjunto de estados
    'Σ': {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'},  # Alfabeto de entrada
    'Γ': {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'B'},  # Alfabeto da fita
    'δ': {
        ('q0', '0'): ('q1', '0', 'R'), 
        ('q0', '1'): ('q1', '1', 'R'), 
        ('q0', '2'): ('q1', '2', 'R'), 
        ('q0', '3'): ('q1', '3', 'R'), 
        ('q0', '4'): ('q1', '4', 'R'), 
        ('q0', '5'): ('q1', '5', 'R'), 
        ('q0', '6'): ('q1', '6', 'R'), 
        ('q0', '7'): ('q1', '7', 'R'), 
        ('q0', '8'): ('q1', '8', 'R'), 
        ('q0', '9'): ('q1', '9', 'R'), 

        ('q1', 'B'): ('q31', 'B', 'R'), #Adicionado
        ('q1', '.'): ('q0', '.', 'R'),
        ('q1', '0'): ('q2', '0', 'R'), 
        ('q1', '1'): ('q2', '1', 'R'), 
        ('q1', '2'): ('q2', '2', 'R'), 
        ('q1', '3'): ('q2', '3', 'R'), 
        ('q1', '4'): ('q2', '4', 'R'), 
        ('q1', '5'): ('q2', '5', 'R'), 
        ('q1', '6'): ('q2', '6', 'R'), 
        ('q1', '7'): ('q2', '7', 'R'), 
        ('q1', '8'): ('q2', '8', 'R'), 
        ('q1', '9'): ('q2', '9', 'R'), 
        
        
        ('q2', 'B'): ('q31', 'B', 'R'), #Adicionado
        ('q2', '.'): ('q0', '.', 'R'),
        ('q2', '0'): ('q3', '0', 'R'), 
        ('q2', '1'): ('q3', '1', 'R'), 
        ('q2', '2'): ('q3', '2', 'R'), 
        ('q2', '3'): ('q3', '3', 'R'), 
        ('q2', '4'): ('q3', '4', 'R'), 
        ('q2', '5'): ('q3', '5', 'R'), 
        ('q2', '6'): ('q3', '6', 'R'), 
        ('q2', '7'): ('q3', '7', 'R'), 
        ('q2', '8'): ('q3', '8', 'R'), 
        ('q2', '9'): ('q3', '9', 'R'), 
        ('q3', '.'): ('qteste2', '.', 'L'),
       
        #('q3', 'B'): ('q31', 'B','R'), #Adicionado
        ('q3', 'B'): ('qteste2', 'B','L'),

       
        ('qteste2', '0') : ('qteste1', '0', 'L'),
        ('qteste2', '1') : ('qteste1', '1', 'L'),
        ('qteste2', '2') : ('qteste1', '2', 'L'),
        ('qteste2', '3') : ('qteste1', '3', 'L'),
        ('qteste2', '4') : ('qteste1', '4', 'L'),
        ('qteste2', '5') : ('qteste1', '5', 'L'),
        ('qteste2', '6') : ('qteste1', '6', 'L'),
        ('qteste2', '7') : ('qteste1', '7', 'L'),
        ('qteste2', '8') : ('qteste1', '8', 'L'),
        ('qteste2', '9') : ('qteste1', '9', 'L'),
        ('qteste1', '0') : ('qteste0', '0', 'L'),
        ('qteste1', '1') : ('qteste0', '1', 'L'),
        ('qteste1', '2') : ('qteste0', '2', 'L'),
        ('qteste1', '3') : ('qteste0', '3', 'L'),
        ('qteste1', '4') : ('qteste0', '4', 'L'),  
        ('qteste1', '5') : ('qteste0', '5', 'L'),
        ('qteste1', '6') : ('qteste0', '6', 'L'),
        ('qteste1', '7') : ('qteste0', '7', 'L'),
        ('qteste1', '8') : ('qteste0', '8', 'L'),
        ('qteste1', '9') : ('qteste0', '9', 'L'),
        ('qteste0', '0') : ('qteste1.1', '0', 'R'),
        ('qteste0', '1') : ('qteste1.1', '1', 'R'),
        ('qteste0', '2') : ('qteste1.1veseeh5', '2', 'R'),

        ('qteste1.1veseeh5','0'): ('qteste1.2veseeh5','0','R'),
        ('qteste1.1veseeh5','1'): ('qteste1.2veseeh5','1','R'),
        ('qteste1.1veseeh5','2'): ('qteste1.2veseeh5','2','R'),
        ('qteste1.1veseeh5','3'): ('qteste1.2veseeh5','3','R'),
        ('qteste1.1veseeh5','4'): ('qteste1.2veseeh5','4','R'),
        ('qteste1.1veseeh5','5'): ('qteste1.2veseeh5','5','R'),
        ('qteste1.1veseeh5','6'): ('qErro','6','R'),
        ('qteste1.1veseeh5','7'): ('qErro','7','R'),
        ('qteste1.1veseeh5','8'): ('qErro','8','R'),
        ('qteste1.1veseeh5','9'): ('qErro','9','R'),

        ('qteste1.2veseeh5','0') : ('qteste1.3', '0','R'),         
        ('qteste1.2veseeh5','1') : ('qteste1.3', '1','R'),
        ('qteste1.2veseeh5','2') : ('qteste1.3', '2','R'),
        ('qteste1.2veseeh5','3') : ('qteste1.3', '3','R'),
        ('qteste1.2veseeh5','4') : ('qteste1.3', '4','R'),
        ('qteste1.2veseeh5','5') : ('qteste1.3', '5','R'),
        ('qteste1.2veseeh5', '6') : ('qErro', 'Erro','R'),
        ('qteste1.2veseeh5', '7') : ('qErro', 'Erro','R'),
        ('qteste1.2veseeh5', '8') : ('qErro', 'Erro','R'),
        ('qteste1.2veseeh5', '9') : ('qErro', 'Erro','R'),


        ('qteste0', '3') : ('qErro', 'Erro', 'R'),
        ('qteste0', '4') : ('qErro', 'Erro', 'R'),
        ('qteste0', '5') : ('qErro', 'Erro', 'R'),
        ('qteste0', '6') : ('qErro', 'Erro', 'R'),
        ('qteste0', '7') : ('qErro', 'Erro', 'R'),
        ('qteste0', '8') : ('qErro', 'Erro', 'R'),
        ('qteste0', '9') : ('qErro', 'Erro', 'R'),
        ('qteste1.1', '0') : ('qteste1.2', '0', 'R'),
        ('qteste1.1', '1') : ('qteste1.2', '1', 'R'),
        ('qteste1.1', '2') : ('qteste1.2', '2', 'R'),
        ('qteste1.1', '3') : ('qteste1.2', '3', 'R'),
        ('qteste1.1', '4') : ('qteste1.2', '4', 'R'),
        ('qteste1.1', '5') : ('qteste1.2', '5', 'R'),
        ('qteste1.1', '6') : ('qteste1.2', '6', 'R'),
        ('qteste1.1', '7') : ('qteste1.2', '7', 'R'),
        ('qteste1.1', '8') : ('qteste1.2', '8', 'R'),
        ('qteste1.1', '9') : ('qteste1.2', '9', 'R'),
        ('qteste1.2', '.') : ('qteste1.3', '.', 'R'),
        ('qteste1.2', '0') : ('qteste1.3', '0', 'R'),
        ('qteste1.2', '1') : ('qteste1.3', '1', 'R'),
        ('qteste1.2', '2') : ('qteste1.3', '2', 'R'),
        ('qteste1.2', '3') : ('qteste1.3', '3', 'R'),
        ('qteste1.2', '4') : ('qteste1.3', '4', 'R'),
        ('qteste1.2', '5') : ('qteste1.3', '5', 'R'),
        ('qteste1.2', '6') : ('qteste1.3', '6', 'R'),
        ('qteste1.2', '7') : ('qteste1.3', '7', 'R'),
        ('qteste1.2', '8') : ('qteste1.3', '8', 'R'),
        ('qteste1.2', '9') : ('qteste1.3', '9', 'R'),
        ('qteste1.3', '.') : ('q0', '.', 'R'),
        ('qteste1.3','B')  : ('q31','B', 'R'),

        
        ('q15', 'B'): ('q31', 'B', 'L'),  # Chega ao fim do ip pelo lado direito


        #Verifica se tem 3 pontos 
        ('31', 'B'): ('qf', 'B', 'S'),
        
        
    },
    'q0': 'q0', 
    'qf': {'q31'},  # Conjunto de estados finais
    'qErro': {'qErro'},  # Definir estado de erro
   
}



def validar_ipv4(ipv4):
    mt_ipv4 = MaquinaTuringIPv4Validator(quintuplas_ipv4_validator)
    return mt_ipv4.executar(ipv4)

# Teste do validador de IPv4
ipv4_valido = "122.2.2"

print("IPv4 válido:", validar_ipv4(ipv4_valido))
