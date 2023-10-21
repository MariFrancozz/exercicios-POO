from destino_viagem import Cadastro_Viagem

viagem_0 = Cadastro_Viagem("São Paulo")
viagem_1 = Cadastro_Viagem("Fortaleza")
viagem_2 = Cadastro_Viagem("Santa Catarina")
viagem_3 = Cadastro_Viagem("Balneário")

print("Sejam bem vindos! Para começarmos, por favor, insira seu nome.")
nome = input("Digite seu nome aqui para iniciarmos: ")

print(f"{nome} Escolha um dos quatro destinos disponiveis: "
'''
[0] São Paulo
[1] Fortaleza
[2] Santa Catarina
[3] Balneário ''')

destino = int(input("Selecione o número da opção desejada: "))
lista_destino = [viagem_0, viagem_1, viagem_2, viagem_3]

opcao_selecionada = int(destino)
for opcao in lista_destino:
    if opcao_selecionada >= 5:   
        print("Esta opção não está incluída em nossos destinos.")
        break
    if opcao_selecionada <= 4:   
        print(f"{nome} sua viagem para {lista_destino[opcao_selecionada].destino} está marcada.") 
        print("Volte sempre!")
        break
