import uuid
import random

# The generation model.
class Generation:
    individuals: list

# The individual.
class Individual:
    list_width: float
    list_height: float

    chromosomes: list

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
        self.detail_id: detail_id
        self.width: width
        self.height: height

    # Make mutation of inividual.
    # probability - probability of mutation occuring. Default: 10%.
    def mutate(self, probability: int = 10):
        if random.randint(0, 100) < probability:
            self.rotate()
    
    # Rotate detail.
    def rotate(self):
        self.width, self.height = self.height, self.width

