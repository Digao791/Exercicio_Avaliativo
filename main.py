import ZoologicoCLI
from ZoologicoDAO import ZoologicoDAO

print("Vamos comecar !")

action = ZoologicoCLI #Incializando a classe ZoologicoCLI

action.Menu() #Chamando método para criar o cuidador

while True:
    print("O que voce deseja fazer ?")
    print("Criar animal - C")
    print("Ler registro do animal - R")
    print("Atualizar registro do animal - U")
    print("Deletar registro do animal - D")
    print("Criar novo Cuidador - T")
    print("Sair - S")

    resposta = input()

    if resposta == "C":
        action.create_Animal() #Chamando o método para criar o Animal
    elif resposta == "R":
        if action.returnQuantityDocuments() == 0: #Se eu não tenho animal nenhum no collections
            print("Crie um animal primeiro")
        else:
            print("Qual animal voce quer ler ?")
            for i in range(0, len(action.animal_obj_id)):
                print(f"{i} = {action.animal_obj[i].nome}")
            id = int(input()) #Entrando com o id
            action.readAnimal(action.animal_obj_id[id]) #Chamando o método para Ler o animal com o id escolhido

    elif resposta == "U":
        if action.returnQuantityDocuments() == 0:
            print("Crie um animal primeiro")
        else:
            print("Qual animal voce quer atuaizar ?")
            for i in range(0, len(action.animal_obj_id)):
                print(f"{i} = {action.animal_obj_name[i]}")

            id = int(input())
            print("Qual o novo nome dele ?")
            nome = input()

            action.updateAnimal(action.animal_obj[id], nome) #Chamando o método para atualizar o nome do animal
            action.animal_obj[id].nome = nome #Atualizandoo o nome do animal com o id esolhido diretamente no objeto
            action.animal_obj_name[id] = nome #Atualizando o  nome do animal com o id escolhido na lista dos nomes

    elif resposta == "D":
        if action.returnQuantityDocuments() == 0:
            print("Crie um animal primeiro")
        else:
            print("Qual animal voce quer deletar ?")
            for i in range(len(action.animal_obj_id)):
                print(f"{i} = {action.animal_obj_name[i]}")
            id = int(input())
            action.deleteAnimal(action.animal_obj_id[id]) #Chamando o método para deletar o animal da coleção

            action.animal_obj.pop(id) #Removendo o objeto animal da lista dos objetos
            action.animal_obj_name.pop(id) #Removendo o nome do objeto removido da lista dos nomes
            action.animal_obj_id.pop(id) #Removendo o id do objeto escolhido da lista de id´s

    elif resposta == "T":
        action.Menu() #Chamando o método para criar o cuidador

    elif resposta == "S": #Saindo do programa
        break
