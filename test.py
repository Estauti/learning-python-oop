from classes import Father, Son

if __name__ == "__main__":
    Father.live()
    f = Father(name="Victor", age=21)
    print(f.name)
    print(f.age)
    f.eat('pizza')
    f.walk()
    del f

    s = Son(name='Ana', age=18, num_friends=2)
    print(s.name)
    print(s.age)
    s.eat('a cake')
    s.walk()
    print('my str is: ', str(s))
    print('my repr is: ', repr(s))
    del s