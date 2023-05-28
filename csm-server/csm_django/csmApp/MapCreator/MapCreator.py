from models import *

# Create map with genetic algoritm.
# At ends saving best generation as map.
def create_map(material: Material, details: list, generations_count: int = 10):
    # Details is chromosomes.
    # Some details arrange an indibidual.
    # Individual arrange generation.
    
    # Creating original generation.
    generation = create_original_generation(details)

    # Execute procedures for any generations.
    for index in range(generations_count):
        generation = crossing(generation)

        mutate(generation)

        calculate_fitness(generation, material.width)
        
    return generation


# Creating original population.
# Generate individuals with random choromosmes.
def create_original_generation(details: list, individuals_count: int = 2) -> Generation:
    individuals: list = []

    for i in range(individuals_count):
        chromosomes: list = []

        for detail in details:
            chromosome = Chromosome(detail_id=detail["detail_id"],
                                    width=detail["width"],
                                    height=detail["length"])

            # Mutate with probability 50 %.
            chromosome.mutate(30)

            chromosomes.append(chromosome)

        individual = Individual(chromosomes)

        individuals.append(individual)

    return Generation(individuals)

# Crossing all details.
def crossing(generation: Generation) -> Generation:
    individuals = generation.individuals.copy()

    free_parents = individuals.copy()

    while len(free_parents) > 1:
        first_parent: Individual = random.choice(free_parents)
        free_parents.remove(first_parent)

        second_parent: Individual = random.choice(free_parents)
        free_parents.remove(second_parent)

        child = first_parent.cross(second_parent)

        individuals.append(child)

        return Generation(individuals)

# Mutations,
def mutate(generation: Generation):
    for individual in generation.individuals:
        individual.mutate()

def calculate_fitness(generation: Generation, max_width):
    generation = generation.calculate_individuals_fitness(max_width)
