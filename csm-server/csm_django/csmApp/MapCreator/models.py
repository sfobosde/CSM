import uuid

# The generation model.
class Generation:
    individuals: list

# The individual.
class Individual:
    chromosomes: list

class Chromosome:
    detail_id: uuid.uuid4
    width: float
    height: float
    rotation: float