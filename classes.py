class Father():
    """
        Manual da Classe Father()

        Parâmetros:
            - name => Nome completo
            - age => Idade
    """
    name = ''
    age = 0
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
    num_friends = 0

    def __init__(self, num_friends, **kwargs):
        self.num_friends = num_friends
        super().__init__(**kwargs)
    
    def walk(self):
        print("I'm running")