import uuid
import random

# The generation model.
class Generation:
    individuals: list

    def __init__(self, individuals: list) -> None:
        self.individuals = individuals

# The individual.
class Individual:
    chromosomes: list

    def __init__(self, chromosomes: list) -> None:
        self.chromosomes = chromosomes

    # Cross with another individual.
    def cross(self, other):
        cross_point = random.randint(0, len(self.chromosomes))

        child_chromosomes = []

        for index in range(0, cross_point):
            child_chromosomes.append(self.chromosomes[index])
        for index in range(cross_point, len(self.chromosomes)):
            child_chromosomes.append(other.chromosomes[index])

        #child_chromosomes = self.chromosomes[0:cross_point].append(other.chromosomes[cross_point, len(self.chromosomes)])

        return Individual(child_chromosomes)
    
    def mutate(self):
        random.choice(self.chromosomes).mutate()

# Chromosome equals detail.
class Chromosome:
    detail_id: uuid.uuid4
    width: float
    height: float
    rotation: float

    def __init__(self, 
                detail_id: uuid.uuid4,
                width: float,
                height: float) -> None:
        self.detail_id = detail_id
        self.width = width
        self.height = height

    # Make mutation of inividual.
    # probability - probability of mutation occuring. Default: 10%.
    def mutate(self, probability: int = 10):
        if random.randint(0, 100) < probability:
            self.rotate()
    
    # Rotate detail.
    def rotate(self):
        (self.width, self.height) = (self.height, self.width)


class Material:
    width: float
    height: float
    sheet_id: uuid.uuid4

    def __init__(self, 
                width: float,
                height: float,
                sheet_id) -> None:
        self.height = height
        self.width = width
        self.sheet_id = sheet_id