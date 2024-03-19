from experta import *

class Animales(KnowledgeEngine):
    @Rule(OR(
           AND(Fact('dientes afilados'),Fact('garras'),Fact('ojos mirando hacia adelante')),
           Fact('come carne')))
    def carnivoro(self):
        self.declare(Fact('carnívoro'))

    @Rule(OR(Fact('pelaje'),Fact('da leche')))
    def mamifero(self):
        self.declare(Fact('mamífero'))

    @Rule(Fact('mamífero'),
          OR(Fact('tiene pezuñas'),Fact('rumia')))
    def pezunas(self):
        self.declare(Fact('ungulado'))

    @Rule(OR(Fact('plumas'),AND(Fact('vuela'),Fact('pone huevos'))))
    def ave(self):
        self.declare(Fact('ave'))



    @Rule(Fact('mamífero'),Fact('carnívoro'),
          Fact(color='rojo-marrón'),
          Fact(pattern='manchas oscuras'))
    def mono(self):
        self.declare(Fact(animal='mono'))

    @Rule(Fact('mamífero'),Fact('carnívoro'),
          Fact(color='rojo-marrón'),
          Fact(pattern='rayas oscuras'))
    def tigre(self):
        self.declare(Fact(animal='tigre'))

    @Rule(Fact('mamífero'),
       Fact('carnívoro'),
       Fact(color='marrón'),
       Fact(melena='presente'))
    def leon(self):
        self.declare(Fact(animal='león'))

    @Rule(Fact('mamífero'),
       Fact('carnívoro'),
       Fact(color='gris'),
       Fact(pelaje='grueso'))
    def lobo(self):
        self.declare(Fact(animal='lobo'))

    @Rule(Fact('mamífero'),
       Fact('herbívoro'),
       Fact(color='gris'),
       Fact(trompa='presente'))
    def elefante(self):
        self.declare(Fact(animal='elefante'))

    @Rule(Fact('reptil'),
       Fact('herbívoro'),
       Fact(caparazón='presente'),
       Fact(movimiento='lento'))
    def tortuga(self):
        self.declare(Fact(animal='tortuga'))

    @Rule(Fact('mamífero'),
       Fact('no vuela'),
       Fact(color='gris'),
       Fact(habitat='mar'))
    def delfin(self):
        self.declare(Fact(animal='delfín'))

    @Rule(Fact('mamífero'),
       Fact('omnívoro'),
       Fact(color='oso'),
       Fact(pelaje='grueso'))
    def oso(self):
        self.declare(Fact(animal='oso negro'))

    @Rule(Fact('mamífero'),
       Fact('omnívoro'),
       Fact(color='oso'),
       Fact(pelaje='grueso'))
    def oso(self):
        self.declare(Fact(animal='oso grizzly'))


    @Rule(Fact('mamífero'),
       Fact('carnívoro'),
       Fact(color='gris'),
       Fact(cola='larga'))
    def zorro(self):
        self.declare(Fact(animal='zorro'))

    @Rule(Fact('reptil'),
       Fact('carnívoro'),
       Fact(sin_patas='presente'),
       Fact(movimiento='reptar'))
    def serpiente(self):
        self.declare(Fact(animal='serpiente'))

    @Rule(Fact('ungulado'),
          Fact('cuello largo'),
          Fact('patas largas'),
          Fact(pattern='manchas oscuras'))
    def jirafa(self):
        self.declare(Fact(animal='jirafa'))

    @Rule(Fact('ungulado'),
          Fact(pattern='rayas oscuras'))
    def cebra(self):
        self.declare(Fact(animal='cebra'))

    @Rule(Fact('ave'),
          Fact('cuello largo'),
          Fact('no puede volar'),
          Fact(color='negro y blanco'))
    def avestruz(self):
        self.declare(Fact(animal='avestruz'))

    @Rule(Fact('ave'),
          Fact('nada'),
          Fact('no puede volar'),
          Fact(color='negro y blanco'))
    def pinguino(self):
        self.declare(Fact(animal='pingüino'))

    @Rule(Fact('ave'),
          Fact('vuela bien'))
    def albatros(self):
        self.declare(Fact(animal='albatros'))

    @Rule(Fact('ave'),
          Fact('nada'),
          Fact('puede volar'),
          )
    def pinguino(self):
        self.declare(Fact(animal='pato'))

    @Rule(Fact('ave'),
       Fact('vuela'),
       Fact(color='marrón' or 'blanco'),
       Fact(cresta='presente'))
    def gallina(self):
        self.declare(Fact(animal='gallina'))

    @Rule(Fact('insecto'),
       Fact(alas='presentes'),
       Fact(colorido='presente'),
       Fact(metamorfosis='presente'))
    def mariposa(self):
        self.declare(Fact(animal='mariposa'))


    @Rule(Fact('ave'),
          Fact('pequeña'),
          Fact('puede volar'),
          )
    def pinguino(self):
        self.declare(Fact(animal='colibri'))

    @Rule(Fact(animal=MATCH.a))
    def imprimir_resultado(self, a):
          print('El animal es {}'.format(a))

    def hechos(self, l):
        for x in l:
            self.declare(x)

ex1 = Animales()
ex1.reset()
ex1.hechos([
    Fact(color='rojo-marrón'),
    Fact(pattern='rayas oscuras'),
    Fact('dientes afilados'),
    Fact('garras'),
    Fact('ojos mirando hacia adelante'),
    Fact('da leche')])
ex1.run()
ex1.facts