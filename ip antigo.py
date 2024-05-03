class MaquinaTuringIPv4Validator:
    def __init__(self, quintuplas):
        self.quintuplas = quintuplas
        self.estado_atual = quintuplas['q0']
        self.cabecote_posicao = 0
        self.fita = ['B'] * 100
        self.erro = None
      
    def executar_passo(self):
         estado = self.estado_atual
         simbolo_lido = self.fita[self.cabecote_posicao]

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
    
    def executar(self, entrada):
        self.fita[:len(entrada)] = entrada
           
        
        while self.estado_atual not in self.quintuplas['qf'] and self.estado_atual not in self.quintuplas['qErro']:
            if not self.executar_passo():
                print("Erro:", self.erro)
                return False
        
        return self.estado_atual in self.quintuplas['qf']


# Definição das quintuplas para validar endereços IPv
quintuplas_ipv4_validator = {
    'Q': {'q0', 'q1', 'q2', 'q3','q15','qErro','qteste1', 'qteste1', 'qteste2', 'q16','q17','q18', 'q19','qteste1.1', 'qteste1.2', 
          'q20', 'q21', 'q22','q23','q24','q25','q26','q27','qteste1.3', 'qteste1.1veseeh5'
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

        ('q1', 'B'): ('q16', 'B', 'L'), #Adicionado
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
        
        
        ('q2', 'B'): ('q16', 'B', 'L'), 
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
       
        ('q3', 'B'): ('q16', 'B','L'), 
       
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
        ('qteste1', '0') : ('qteste1', '0', 'L'),
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


        ('qteste0', '3') : ('qf', 'Erro', 'R'),
        ('qteste0', '4') : ('qf', 'Erro', 'R'),
        ('qteste0', '5') : ('qf', 'Erro', 'R'),
        ('qteste0', '6') : ('qf', 'Erro', 'R'),
        ('qteste0', '7') : ('qf', 'Erro', 'R'),
        ('qteste0', '8') : ('qf', 'Erro', 'R'),
        ('qteste0', '9') : ('qf', 'Erro', 'R'),
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

        
        ('q15', 'B'): ('q16', 'B', 'L'),  

        ('q16', '0'): ('q17', '0', 'L'),
        ('q16', '1'): ('q17', '1', 'L'),
        ('q16', '2'): ('q17', '2', 'L'),
        ('q16', '3'): ('q17', '3', 'L'),
        ('q16', '4'): ('q17', '4', 'L'),
        ('q16', '5'): ('q17', '5', 'L'),
        ('q16', '6'): ('q17', '6', 'L'),
        ('q16', '7'): ('q17', '7', 'L'),
        ('q16', '8'): ('q17', '8', 'L'),
        ('q16', '9'): ('q17', '9', 'L'),

        ('q17', '.'): ('q18', '.', 'L'),
        ('q17', '0'): ('q18', '0', 'L'),
        ('q17', '1'): ('q18', '1', 'L'),
        ('q17', '2'): ('q18', '2', 'L'),
        ('q17', '3'): ('q18', '3', 'L'),
        ('q17', '4'): ('q18', '4', 'L'),
        ('q17', '5'): ('q18', '5', 'L'),
        ('q17', '6'): ('q18', '6', 'L'),
        ('q17', '7'): ('q18', '7', 'L'),
        ('q17', '8'): ('q18', '8', 'L'),
        ('q17', '9'): ('q18', '9', 'L'),


        ('q18', '.'): ('q19', '.', 'L'),
        ('q18', '0'): ('q19','0','L'),
        ('q18', '1'): ('q19','1','L'),
        ('q18', '2'): ('q19','2','L'),
        ('q18', '3'): ('q19','3','L'),
        ('q18', '4'): ('q19','4','L'),
        ('q18', '5'): ('q19','5','L'),
        ('q18', '6'): ('q19','6','L'),
        ('q18', '7'): ('q19','7','L'),
        ('q18', '8'): ('q19','8','L'),
        ('q18', '9'): ('q19','9','L'),


        ('q19', '.'): ('q20', '.', 'L'),
        ('q19', '0'): ('q20','0','L'),
        ('q19', '1'): ('q20','1','L'),
        ('q19', '2'): ('q20','2','L'),
        ('q19', '3'): ('q20','3','L'),
        ('q19', '4'): ('q20','4','L'),
        ('q19', '5'): ('q20','5','L'),
        ('q19', '6'): ('q20','6','L'),
        ('q19', '7'): ('q20','7','L'),
        ('q19', '8'): ('q20','8','L'),
        ('q19', '9'): ('q20','9','L'),


        ('q20', '.'): ('q21', '.', 'L'),
        ('q20', '0'): ('q21','0','L'),
        ('q20', '1'): ('q21','1','L'),
        ('q20', '2'): ('q21','2','L'),
        ('q20', '3'): ('q21','3','L'),
        ('q20', '4'): ('q21','4','L'),
        ('q20', '5'): ('q21','5','L'),
        ('q20', '6'): ('q21','6','L'),
        ('q20', '7'): ('q21','7','L'),
        ('q20', '8'): ('q21','8','L'),
        ('q20', '9'): ('q21','9','L'),
        
        
        ('q21', '.'): ('q22', '.', 'L'),
        ('q21', '0'): ('q22','0','L'),
        ('q21', '1'): ('q22','1','L'),
        ('q21', '2'): ('q22','2','L'),
        ('q21', '3'): ('q22','3','L'),
        ('q21', '4'): ('q22','4','L'),
        ('q21', '5'): ('q22','5','L'),
        ('q21', '6'): ('q22','6','L'),
        ('q21', '7'): ('q22','7','L'),
        ('q21', '8'): ('q22','8','L'),
        ('q21', '9'): ('q22','9','L'), 


        ('q22', '.'): ('q23', '.', 'L'),
        ('q22','B'): ('q31','B','L'),
        ('q22','0'): ('q23','0','L'),
        ('q22','1'): ('q23','1','L'),
        ('q22','2'): ('q23','2','L'),
        ('q22','3'): ('q23','3','L'),
        ('q22','4'): ('q23','4','L'),
        ('q22','5'): ('q23','5','L'),
        ('q22','6'): ('q23','6','L'),
        ('q22','7'): ('q23','7','L'),
        ('q22','8'): ('q23','8','L'),
        ('q22','9'): ('q23','9','L'),


        ('q23', '.'): ('q24', '.', 'L'),
        ('q23','B'): ('q31','B','L'),
        ('q23','0'): ('q24','0','L'),
        ('q23','1'): ('q24','1','L'),
        ('q23','2'): ('q24','2','L'),
        ('q23','3'): ('q24','3','L'),
        ('q23','4'): ('q24','4','L'),
        ('q23','5'): ('q24','5','L'),
        ('q23','6'): ('q24','6','L'),
        ('q23','7'): ('q24','7','L'),
        ('q23','8'): ('q24','8','L'),
        ('q23','9'): ('q24','9','L'),
        
        
        ('q24', '.'): ('q25', '.', 'L'),
        ('q24','B'): ('q31','B','L'),
        ('q24','0'): ('q25','0','L'),
        ('q24','1'): ('q25','1','L'),
        ('q24','2'): ('q25','2','L'),
        ('q24','3'): ('q25','3','L'),
        ('q24','4'): ('q25','4','L'),
        ('q24','5'): ('q25','5','L'),
        ('q24','6'): ('q25','6','L'),
        ('q24','7'): ('q25','7','L'),
        ('q24','8'): ('q25','8','L'),
        ('q24','9'): ('q25','9','L'),
        
        
        ('q25', '.'): ('q26', '.', 'L'),
        ('q25','B'): ('q31','B','L'),
        ('q25','0'):('q26','0','L'),
        ('q25','1'):('q26','1','L'),
        ('q25','2'):('q26','2','L'),
        ('q25','3'):('q26','3','L'),
        ('q25','4'):('q26','4','L'),
        ('q25','5'):('q26','5','L'),
        ('q25','6'):('q26','6','L'),
        ('q25','7'):('q26','7','L'),
        ('q25','8'):('q26','8','L'),
        ('q25','9'):('q26','9','L'),

        
        ('q26', '.'): ('q27', '.', 'L'),
        ('q26','B'): ('q31','B','L'),
        ('q26','0'): ('q27','0','L'),
        ('q26','1'): ('q27','1','L'),
        ('q26','2'): ('q27','2','L'),
        ('q26','3'): ('q27','3','L'),
        ('q26','4'): ('q27','4','L'),
        ('q26','5'): ('q27','5','L'),
        ('q26','6'): ('q27','6','L'),
        ('q26','7'): ('q27','7','L'),
        ('q26','8'): ('q27','8','L'),
        ('q26','9'): ('q27','9','L'),

        
        ('q27', '.'): ('q28', '.', 'L'),
        ('q27','B'): ('q31','B','L'), 
        ('q27','0'): ('q28','0','L'),
        ('q27','1'): ('q28','1','L'),
        ('q27','2'): ('q28','2','L'),
        ('q27','3'): ('q28','3','L'),
        ('q27','4'): ('q28','4','L'),
        ('q27','5'): ('q28','5','L'),
        ('q27','6'): ('q28','6','L'),
        ('q27','7'): ('q28','7','L'),
        ('q27','8'): ('q28','8','L'),
        ('q27','9'): ('q28','9','L'),

        
        ('q28', '.'): ('q29', '.', 'L'),
        ('q28','B'): ('q31','B','L'),
        ('q28','0'): ('q29','0','L'),
        ('q28','1'): ('q29','1','L'),
        ('q28','2'): ('q29','2','L'),
        ('q28','3'): ('q29','3','L'),
        ('q28','4'): ('q29','4','L'),
        ('q28','5'): ('q29','5','L'),
        ('q28','6'): ('q29','6','L'),
        ('q28','7'): ('q29','7','L'),
        ('q28','8'): ('q29','8','L'),
        ('q28','9'): ('q29','9','L'),

        
        ('q29', '.'): ('q30', '.', 'L'),
        ('q29','B'): ('q31','B','L'),
        ('q29','0'): ('q30','0','L'),
        ('q29','1'): ('q30','1','L'),
        ('q29','2'): ('q30','2','L'),
        ('q29','3'): ('q30','3','L'),
        ('q29','4'): ('q30','4','L'),
        ('q29','5'): ('q30','5','L'),
        ('q29','6'): ('q30','6','L'),
        ('q29','7'): ('q30','7','L'),
        ('q29','8'): ('q30','8','L'),
        ('q29','9'): ('q30','9','L'),

        
        ('q30', '.'): ('q31', '.', 'L'),
        ('q30', 'B'): ('q31','B','L'),
        ('q30', '0'): ('q31','0','L'),
        ('q30', '1'): ('q31','1','L'),
        ('q30', '2'): ('q31','2','L'),
        ('q30', '3'): ('q31','3','L'),
        ('q30', '4'): ('q31','4','L'),
        ('q30', '5'): ('q31','5','L'),
        ('q30', '6'): ('q31','6','L'),
        ('q30', '7'): ('q31','7','L'),
        ('q30', '8'): ('q31','8','L'),
        ('q30', '9'): ('q31','9','L'),

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
ipv4_valido = "191.2.22.9.3.3.3"

print("IPv4 válido:", validar_ipv4(ipv4_valido))