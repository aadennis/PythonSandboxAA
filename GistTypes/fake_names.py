# https://faker.readthedocs.io/en/master/
# pip install Faker - from command line

from faker import Faker

# number of fakes to produce...
NO_OF_FAKES = 100

fake = Faker()

names = []
for _ in range(NO_OF_FAKES):
    names.append(fake.name())

idx = 0
for _ in names:
    print(names[idx])
    idx += 1



