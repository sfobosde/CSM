from .models import *

# Create map with genetic algoritm.
# At ends saving best generation as map.
def create_map(material: Material, details: list, generations_count: int = 10, individuals_count: int = 2, unused_limit: float = 15) -> Individual:
    # Details is chromosomes.
    # Some details arrange an indibidual.
    # Individual arrange generation.
    
    # Creating original generation.
    generation = create_original_generation(details, individuals_count)

    index = 0

    best_unused = unused_limit

    first_best = None
    second_best = None

    # Execute procedures for any generations.
    while (index < generations_count
            and best_unused >= unused_limit):
        generation.crossing()

        generation.mutate()

        generation.calculate_individuals_fitness(material.width, material.height)

        generation.remove_lifeless()

        if (first_best == None):
            first_best = generation.find_best()
            second_best = first_best
        else:
            second_best = generation.find_best()

        if (second_best.unused_area_part < first_best.unused_area_part):
            first_best = second_best
            best_unused = first_best.unused_area_part

        index += 1

    print(first_best.unused_area_part)
    input()
    print_details(first_best)
        
    return first_best


# Creating original population.
# Generate individuals with random choromosmes.
def create_original_generation(details: list, individuals_count) -> Generation:
    individuals: list = []

    for i in range(individuals_count):
        chromosomes: list = []

        for detail in details:
            chromosome = Chromosome(detail_id=detail["detail_id"],
                                    width=detail["width"],
                                    height=detail["length"])

            # Mutate with probability 50 %.
            chromosome.mutate(100)

            chromosomes.append(chromosome)

        individual = Individual(chromosomes)

        individuals.append(individual)

    return Generation(individuals)

def print_details(best: Individual):
    best.polygone.print_tree()