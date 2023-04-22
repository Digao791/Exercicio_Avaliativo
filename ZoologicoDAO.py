
from bson.objectid import ObjectId
from pymongo import collection

import ZoologicoCLI
from Animal import Animal


class ZoologicoDAO:

    def __init__(self, database):
        self.db = database
        self.collection = database.collection


    def createAnimal(self, animal:Animal) -> str: #Criando a collection
        try:
            result = self.collection.insert_one({"Animal": animal.nome,"Habitat" : animal.habitat, "Cuidador": ZoologicoCLI.cuidador_habitat})
            animal_id = str(result.inserted_id)
            print(f"animal {animal.nome} created with id: {animal_id}")
            return animal_id
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")
            return None

    def readAnimal(self, animal_id: str) -> None: #Fazendo a leitura da collection
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")
            return None

    def updateAnimal(self, animal: Animal, nome: str) -> None: #Fazendo a atualização da collection
        try:
            result = self.collection.update_one({"_id": ObjectId(animal.id)}, {"$set": {"Animal": nome}})
            if result.modified_count:
                print(f"Animal {animal.nome} updated with name {nome}")
            else:
                print(f"No animal found with id {animal.id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None

    def deleteAnimal(self, animal_id: str) -> None: #Deletando o objeto na collection
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting animal: {error}")
            return None