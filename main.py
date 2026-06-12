import os
import pyfiglet
os.system('cls')
fila_hospitalar = []
while True:
    #gera o texto ASCII
    texto_ascii =pyfiglet.figlet_format("Health Manager")
    #menu inicial
    print(texto_ascii)
    print("[1] começar triagem")
    print("[2] Lista de pacientes")
    print("[3] Proximo paciente ")
    print("[4] Sair")
    
    
    while True:
        try:
            resp = int(input("digite: "))
            break
        except ValueError:
            print("digite valores válidos")
        
    
    #nova triagem
    if resp == 1:
        os.system('cls')
        print(texto_ascii)
        
        while True:
            nome = input("nome do paciente: ").strip()
            if nome.isnumeric():
                print("digite de maneira correta")
            else:
                break

          
        while True:
            try:
                idade = int((input("idade do paciente: ")))
                break
            except ValueError:
                print("digite valores corretos")
            
            
        while True:
            sexo = input("sexo do paciente: ").strip().upper()

                        # Verifica se o que foi digitado está entre as opções válidas
            if sexo in ['M', 'F', 'N']:
                break  # Sai do laço se a entrada for válida
            else:
                print("Entrada inválida! Por favor, se refira ao sexo do paciente com M, F ou N (não binário).")

        # O código continua aqui com a variável 'sexo' garantidamente válida
        print(f"Sexo registrado: {sexo}")        
        sintomas = input("sintomas resumidos: ").strip()

        # Menu de cores
        print("selecione o tipo de prioridade:")
        print("[1] Vermelho")
        print("[2] Amarelo")
        print("[3] Verde")

        while True:
            try:
                cor = int(input("selecione o tipo de prioridade: "))
                if cor in [1, 2, 3]: # Garante que o número digitado seja válido
                    break
                print("Por favor, escolha uma opção válida (1, 2 ou 3).")
            except ValueError:
                print("digite valores corretos")

        # adiciona o peso das cores
        if cor == 1:
            cor = "Vermelho"
            peso_prioridade = 1

        elif cor == 2:
            cor = "Amarelo" # Corrigido de Laranja para Amarelo
            peso_prioridade = 2

        elif cor == 3:
            
            if idade >= 60:
                peso_prioridade = 2.50
            else:
                peso_prioridade = 3
                
            
            cor = "Verde"

        print(f"Cor selecionada: {cor} | Peso: {peso_prioridade}")
        #adiciona a lista de pacientes
        dados_do_paciente = (peso_prioridade, nome, idade, sexo, sintomas, cor)
        fila_hospitalar.append(dados_do_paciente)
        fila_hospitalar.sort()
        print(fila_hospitalar)
    #printa a lista
    if resp == 2:
        print("="*70)
        print(f"{'LISTA DE PACIENTES NA FILA':^70}")
        print("="*70)
        
        if len(fila_hospitalar) == 0:
            print(f"{'Não há pacientes na fila no momento.':^70}")
        else:
            # Mostra o cabeçalho das colunas
            print(f"{'NOME':<25} | {'IDADE':<5} | {'SEXO':<5} | {'PRIORIDADE':<12}")
            print("-"*70)
            
            # O truque está aqui: passamos por cada paciente, um por um
            for paciente in fila_hospitalar:
                # Desempacotamos os 6 elementos da tupla em variáveis
                peso, nome, idade, sexo, sintomas, cor = paciente
                
                # Printamos cada um em uma linha formatada
                print(f"{nome:<25} | {idade:<5} | {sexo:<5} | {cor:<12}")
                
        print("="*70)

    elif resp == 3:
        if len(fila_hospitalar) == 0:
            print("="*50)
            print("não há pacientes para chamar")
            print("="*50)
        else:
            print("="*50)
            print(f"Chamando agora {fila_hospitalar[0]}")
            print("="*50)
            fila_hospitalar.pop(0)      

    elif resp == 4:
        os.system('cls')
        break