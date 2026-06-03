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
    
    try:#tratamento de erros

        resp = int(input("digite: "))
    except ValueError:
        print("Opcção invalida, digite apenas numeros do menu")
        continue
    #nova triagem
    if resp == 1:
        os.system('cls')
        print(texto_ascii)
        try:#tratamento de erros
            
            nome = input("nome do paciente: ").strip()
        except SyntaxError:
            print("digite apenas o nome")
            continue
        try:
            idade = int(input("idade do paciente: "))
        except ValueError:
            print("digite apenas a idade do paciente")
        try:
            sexo = input("sexo do paciente: ").strip()
        except ValueError:
            print("Se refira ao sexo do paciente com M, F ou N (não binario)")
        try:
            sintomas = input("sintomas resumidos: ").strip()
        except ValueError:
            print("digite os sintomas corretos")

        #cores
        print("selecione o tipo de prioridade:")
        print("[1] Vermelho")
        print("[2] Amarelo")
        print("[3] Verde")
        cor = int(input("selecine o tipo de prioridade: "))
        #adiciona o peso das cores
        if cor == 1:
            cor = "vermelho"
            peso_prioridade = 1
        elif cor == 2:
            cor = "Laranja"
            peso_prioridade = 2
        elif cor == 3:
            cor = "Verde"
            peso_prioridade = 3
            if cor == 3 and idade <= 60:
                peso_prioridade = 3.50
        #adiciona a lista de pacientes
        dados_do_paciente = (peso_prioridade, nome, idade, sexo, sintomas, cor)
        fila_hospitalar.append(dados_do_paciente)
        fila_hospitalar.sort()
        print(fila_hospitalar)
    #printa a lista
    if resp == 2:
        if len(fila_hospitalar) >=1:    
            print("="*50)
            print("             Lista de Pacientes")
            print("="*50)
            print(fila_hospitalar)
            print("="*50)
        if len(fila_hospitalar) == 0:
            print("="*50)
            print("             Lista de Pacientes")
            print("="*50)
            print("Não há pacientes na fila")
            print("="*50) 

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