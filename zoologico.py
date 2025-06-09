from abc import ABC, abstractmethod

# Interface Animal
class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass  

    @abstractmethod
    def interagir(self, pessoa):
        pass

# Classes concretas de animais

class Girafa(Animal):
    def emitir_som(self):
        print("A girafa assobia: IIIIRRRÍ!")

    def interagir(self, pessoa):
        print("A girafa se aproxima calmamente.")
        pessoa.reagir(self)

class Rinoceronte(Animal):
    def emitir_som(self):
        print("O rinoceronte bufa: GROON-GROON!")

    def interagir(self, pessoa):
        print("O rinoceronte parece desconfiado.")
        pessoa.reagir(self)

class Macaco(Animal):
    def emitir_som(self):
        print("O macaco chia: UGA-UGA!")

    def interagir(self, pessoa):
        print("O macaco balança nos galhos animado.")
        pessoa.reagir(self)

class Leao(Animal):
    def emitir_som(self):
        print("O leão ruge: ROOOOARRR!")

    def interagir(self, pessoa):
        if isinstance(pessoa, Pai):
            print("O leão fareja o Pai... e então SALTA NELE!")
            print("O Pai foi COMIDO pelo leão! \n")

# Interface Pessoa
class Pessoa(ABC):

    @abstractmethod
    def reagir(self, animal):
        pass

# Classes concretas de visitantes
class Pai(Pessoa):
    def reagir(self, animal):
        print(f"O Pai se aproxima do {animal.__class__.__name__} com curiosidade.\n")

class Mae(Pessoa):
    def reagir(self, animal):
        print(f"A Mãe tira várias fotos do {animal.__class__.__name__} com entusiasmo.\n")

class Filho(Pessoa):
    def reagir(self, animal):
        print(f"O Filho pula de alegria ao ver o {animal.__class__.__name__}!\n")

class Filha(Pessoa):
    def reagir(self, animal):
        print(f"A Filha observa o {animal.__class__.__name__} com cautela e mantém distância.\n")

# ------------------------------
# Teste de polimorfismo no Zoológico
# ------------------------------

# Família
mae = Mae()
filho = Filho()
filha = Filha()
pai = Pai()

# Animais
girafa = Girafa()
rinoceronte = Rinoceronte()
macaco = Macaco()
leao = Leao()

# Visitas
visitas = [
    (mae, girafa),
    (filho, macaco),
    (filha, rinoceronte),
    (pai, leao),

]

for pessoa, animal in visitas:
    print(f"=== {pessoa.__class__.__name__} visita o {animal.__class__.__name__} ===")
    animal.emitir_som()
    animal.interagir(pessoa)
    print("\n")
