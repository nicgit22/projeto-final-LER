import os
import pyfiglet
texto_ascii = pyfiglet.figlet_format("Health Manager")
print(texto_ascii)

pacientes = {}

print("[1] começar triagem")
print("[2] sair")
resp = int(input("digite: "))
if resp == 1:
    os.system('cls')
    print(texto_ascii)
    nome = input("nome do paciente: ")
    idade = input("idade do paciente")
    sexo = input("sexo do paciente")
    sintomas = input("sintomas: ")
    tempo = input("quando começou:")
    pacientes.append(nome)
    os.system('cls')
    print(texto_ascii)
    print("selecione o tipo de prioridade:")
    print("[1]")
    print("[2]")
    print("[3]")
    print("[4]")
    print(pacientes)
    