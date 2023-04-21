from ZoologicoDAO import ZoologicoDAO
from Animal import Animal
from Cuidador import Cuidador
from Habitat import Habitat

from database import Database

db = Database(database="Zoologico", collection="Animais") #Inicializando o banco de dados chamado Zoologico e com a collections chamada Animais
db.resetDatabase() #Resetando o banco de dados
Animal_model = ZoologicoDAO(db) #Inicializando o CRUD do BD


index = 0 #Index que serve como id do cuidador atual
id_animal = 1 #guarda o valor do i-ésimo animal a ser criado
animal_obj = [] #Lista dos objetos
animal_obj_id = [] #Lista dos id´s dos objetos
animal_obj_name = [] #Lista dos nomes dos animais

cuidador_habitat = None #Variável que recebe o objeto a ser inserido no collections
cuidador_obj: Cuidador #Variável que recebe o objeto do Cuidador

def Menu():
    print("Seja muito bem vindo !!")
    print("Qual o seu nome cuidador ?")

    nome_cuidador = input() #Entrando com o nome do cuidador

    print(f"Qual o seu documento {nome_cuidador} ? RG ou CPF")

    documento = input() #Entrando com o documento do cuidador

    global cuidador_obj
    cuidador_obj = Cuidador(nome_cuidador, documento) #Inicializando o objeto do Cuidador

    global index
    cuidador_obj.id = index #Atualizando id do cuidador

    index = index + 1

    global cuidador_habitat
    cuidador_habitat = {"nome": cuidador_obj.nome, "documento": cuidador_obj.documento} #Guardando o objeto a ser inserido no collections


def create_Animal():
    global id_animal

    print(f"Vamos criar os habitats do animal {id_animal}")
    print("Quantos habitats voce quer criar ?")

    habitat = [] #Lista de habitates
    qnt = int(input()) #Quantidade dos habitats que o animal pode ficar

    for i in range(0, qnt):
        print(f"Qual o nome do habitat {i+1} que o animal vai ficar ?")
        nome_habitat = input() #Entrando com o nome do habitat
        print(f"Qual o tipo do habitat {i+1} ?")
        tipo_habitat = input() #Entrando com o tipo do habitat

        x = Habitat(nome_habitat, tipo_habitat, cuidador_obj) #Inicializando o objeto do Habitat

        x.id = len(habitat) #Atualizando o id do Habitat

        habitat.append({"nome": x.nome, "tipo" : x.tipoAmbiente, "cuidador": x.cuidador.nome}) #Inserindo na lista de habitats o Habitat criado



    print(f"Qual o nome do animal ?")
    nome_animal = input() #Inserindo o nome do animal
    print(f"Qual a especie desse animal ?")
    especie_animal = input() #Inserindo a especie do animal
    print(f"Qual a idade desse animal ?")
    idade_animal = int(input()) #Inserindo a idade do animal


    animal_criado = Animal(nome_animal, especie_animal, idade_animal, habitat) #Inicializando o objeto do Animal
    id = Animal_model.createAnimal(animal_criado) # Variável que guarda o ID criado pelo Collection
    animal_criado.id = id #Atualizando o id do animal

    animal_obj.append(animal_criado) #Inserindo o objeto do animal na lista de objetos de animais
    animal_obj_id.append(id) #Inserindo o id do objeto na lista de Id´s
    animal_obj_name.append(nome_animal) #Inserindo o nome do animal recém criado na lista de nomes

    id_animal = id_animal + 1

def readAnimal(id: str):
    Animal_model.readAnimal(id) #Chamando o método para ler o objeto guardado no collection

def updateAnimal(animal: Animal, nome: str):
    Animal_model.updateAnimal(animal, nome)#Chamando o método para atualizar o nome do objeto guardado no collection

def deleteAnimal(id: str):
    Animal_model.deleteAnimal(id) #Chamando o método para deletar o objeto guardado no collection pelo id
