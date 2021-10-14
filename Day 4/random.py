import random
import test_module


random_integer = random.randint(1,10)
print(random_integer)

random_float = random.random()
print(random_float)

# permite multiplicar por um valor maximo que queremos sem chegar a essa valor
random_float = random.random() * 5 # vai de 0 a 4.99999
print(random_float)