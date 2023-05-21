from .models import *

# Create map with genetic algoritm.
# At ends saving best generation as map.
async def create_map(material, details: list, generations_count: int = 10):
    # Creating original population.
    original_generation: Generation = create_original_generation(details, 10)

    for generation_index in range(generations_count):
        pass

# Creating original population.
# Generate individuals with random choromosmes.
def create_original_generation(details: list, individuals_count: int = 10) -> Generation:
    # TODO
    pass

# Crossing all details.
def crossing(generation):
    # TODO
    pass
