class AFD:
    def __init__(self):

        self.estados = {'q0': 0, 'q1': 1, 'q2': 2}
        self.estado_inicial = 'q0'
        self.estado_atual = self.estado_inicial
        self.estados_finais = {'q2'}

        self.simbolos = {'a': 0, 'b': 1}
        
        # Cada linha é um estado (q0, q1, q2)
        # Cada coluna é um símbolo (a, b)
        self.matriz_transicao = [
            ['q1', 'q0'],  # Transições para q0
            ['q1', 'q2'],  # Transições para q1
            ['q2', 'q2']   # Transições para q2
        ]
    
    def transicionar(self, simbolo):
        #Faz uma transição baseada no símbolo de entrada usando matriz
        if simbolo in self.simbolos:
            estado_idx = self.estados[self.estado_atual]
            simbolo_idx = self.simbolos[simbolo]
            self.estado_atual = self.matriz_transicao[estado_idx][simbolo_idx]
        else:
            # Símbolo inválido
            self.estado_atual = None
    
    def reset(self):
        #Reseta para o estado inicial
        self.estado_atual = self.estado_inicial
    
    def processar_palavra(self, palavra):
        #Processa uma palavra inteira e retorna se é aceita ou não
        self.reset()
        for simbolo in palavra:
            if self.estado_atual is None:
                return False
            self.transicionar(simbolo)
        
        return self.estado_atual in self.estados_finais

def main():
    afd = AFD()
    print("Autômato Finito Determinístico (AFD) L = {W E {a,b}+ | W tem subpalavra ab}")
    print("Alfabeto válido: {a, b}")
    print("Digite 'sair' para encerrar o programa.")
    print("=======================================")
    
    while True:
        palavra = input("\nDigite uma palavra: ").strip().lower() #poe para minusculo 
        
        if palavra == 'sair':
            print("Tchau prof...")
            break
        
        # Verifica se a palavra contém apenas a e b
        if not all(c in {'a', 'b'} for c in palavra):
            print(f"Erro: A palavra '{palavra}' contém símbolos inválidos. Use apenas 'a' e 'b'.")
            continue
        
        resultado = afd.processar_palavra(palavra)
        
        if resultado:
            print(f"'{palavra}' foi ACEITA")
        else:
            print(f"'{palavra}' foi REJEITADA")

if __name__ == "__main__":
    main()