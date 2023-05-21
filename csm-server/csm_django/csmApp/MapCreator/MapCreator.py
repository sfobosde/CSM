from .models import *

# Create map with genetic algoritm.
# At ends saving best generation as map.
def create_map(material, details: list, generations_count: int = 10):
    # Details is chromosomes.
    # Some details arrange an indibidual.
    # Individual arrange generation.
    
    # Creating original generation.
    original_generation = create_original_generation(details)

# Creating original population.
# Generate individuals with random choromosmes.
def create_original_generation(details: list, individuals_count: int = 10) -> Generation:
    individuals: list = []

    for i in range(individuals_count):
        chromosomes: list = []

        for detail in details:
            chromosome = Chromosome(detail["detail_id"],detail["width"],detail["length"])

            # Mutate with probability 50 %.
            chromosome.mutate(30)

            chromosomes.append(chromosome)

        individual = Individual(chromosomes)

        individuals.append(individual)

    return Generation(individuals)

# Crossing all details.
def crossing(generation):
    # TODO
    pass
