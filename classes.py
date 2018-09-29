class Father():
    """
        Manual da Classe Father()

        Parâmetros:
            - name => Nome completo
            - age => Idade
    """

    def __init__(self, name, age):
        print("I'm being created!")
        self.name = name
        self.age = age


    def __del__(self):
        print("I'm being destroyed!")


    def eat(self, food):
        print("I'm eating {}".format(food))


    def walk(self):
        print("I'm walking")


class Son(Father):
    """
        Manual da Classe Son()

        Parâmetros:
            num_friends => Número de Amigos
        
        kwargs (Father):
            - name [string]
            - age [int+]
    """
    __num_sons = 0

    def __init__(self, num_friends, **kwargs):
        Son.__num_sons += 1
        self.num_friends = num_friends
        super().__init__(**kwargs)
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Son(num_friends={self.getNumSons()}, name={self.name}, age={self.age})'
    
    def walk(self):
        print("I'm running")
        
    def getNumSons(self):
        return Son.__num_sons