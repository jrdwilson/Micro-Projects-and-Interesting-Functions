# Duck Typing and Easier to ask forgiveness than permission (EAFP)

# This code was copied from Corey Schafer's excellent video tutorials
# Source: https://youtu.be/x3v9zMX1s4s

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, flap')

class Person:

    def quack(self):
        print("I'm Quacking Like a Dcuk!")

    def fly(self):
        print("I'm Flapping my Arms!")

# Not duck-typed (Non-Pythonic)
def quack_and_fly_NDT(thing):
    if isinstance(thing, Duck):
        thing.quack()
        thing.fly()
    else:
        print('This has to be a Duck!')
    
    print() # For spacing results

d = Duck()
quack_and_fly_NDT(d)

p = Person()
quack_and_fly_NDT(p)

# Duck-Typed (Pythonic)
def quack_and_fly_DT(thing):
    thing.quack()
    thing.fly()

    print() # For spacing results

d = Duck()
quack_and_fly_DT(d)

p = Person()
quack_and_fly_DT(p)

# Look before you leap (LBYL)
def quack_and_fly_LBYL(thing):
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly()):
            thing.quack()

    print() # For spacing results

d = Duck()
quack_and_fly_LBYL(d)

p = Person()
quack_and_fly_LBYL(p)

# Easier to ask forgiveness than permission (EAFP)
def quack_and_fly_EAFP(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark() # Will throw an error
    except AttributeError as e:
        print(e)

    print() # For spacing results

d = Duck()
quack_and_fly_EAFP(d)

p = Person()
quack_and_fly_EAFP(p)