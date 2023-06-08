import uuid
import random
from binaryTree import Polygone

# The generation model.
class Generation:
    individuals: list

    individual_square: float

    def __init__(self, individuals: list) -> None:
        self.individuals = individuals

    def mutate(self):
        for individual in self.individuals:
            individual.mutate()

    # Crossing all details.
    def crossing(self):
        free_parents = self.individuals.copy()

        while len(free_parents) > 1:
            first_parent: Individual = random.choice(free_parents)
            free_parents.remove(first_parent)

            second_parent: Individual = random.choice(free_parents)
            free_parents.remove(second_parent)

            child = first_parent.cross(second_parent)

            self.individuals.append(child)

    # Calculate fitness for every individual.
    def calculate_individuals_fitness(self, max_width, max_height):
        for individ in self.individuals:
            individ.calculate_fitness(max_width, max_height)

    def remove_lifeless(self):
        if (not hasattr(self, "individuals") or len(self.individuals) < 2):
            raise Exception("Все особи неживые")
        
        for individ in self.individuals:
            if (not individ.adapted or individ.unused_area_part > 25):
                index = self.individuals.index(individ)
                self.individuals.pop(index)

        if (not hasattr(self, "individuals") or len(self.individuals) < 2):
            raise Exception("Все особи неживые")

    def find_best(self):
        best = self.individuals[0]

        for individ in self.individuals:
            if (individ.adapted and individ.unused_area_part < best.unused_area_part):
                best = individ

        # print(f'The best: {best.unused_area_part}')

        return best

# The individual.
class Individual:
    chromosomes: list

    x_max: float
    y_max: float

    details_square: float

    occupied_area_square: float
    unused_area_square: float

    useful_part: float
    unused_area_part: float

    adapted: bool

    polygone: Polygone

    def __init__(self, chromosomes: list) -> None:
        self.chromosomes = chromosomes

        self.details_square = 0

        self.occupied_area_square = 0
        self.unused_area_square = 0

        self.useful_part = 0
        self.unused_area_part = 100

        self.x_max = 0
        self.y_max = 0

        self.adapted = True

        for detail in self.chromosomes:
            self.details_square += detail.square

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

    # Calculate individual fitness.
    def calculate_fitness(self, max_width, max_height):
        sorted = self.sort()

        polygone = Polygone(max_width, max_height, self.expand_square)

        try:
            for detail in sorted:
                polygone.add_detail(detail)
                #print(f'Current polygone:{self.x_max} {self.y_max}')
            #print("================================================================")

            self.calculate_fitness_params(max_width, max_height)
            self.polygone = polygone

        except Exception as err:
            self.adapted = False
            print(err)
            print()
        
        #polygone.print_tree()

    def calculate_fitness_params(self, max_width, max_height):
        if (not self.adapted):
            self.unused_area_part = 100
            self.useful_part = 0
            self.__remain_square = 0
        else:
            self.occupied_area_square = self.x_max*self.y_max

            self.useful_part = 100 * self.details_square / self.occupied_area_square

            self.unused_area_square = self.occupied_area_square - self.details_square
            self.unused_area_part = 100 * self.unused_area_square / self.occupied_area_square

            self.__remainX = self.x_max
            self.__remainY = self.y_max

            self.__remain_width = max_width - self.x_max
            self.__remain_height = max_height

            self.__remain_square = self.__remain_width * self.__remain_height

        # print(f'Area start at: 0, 0')
        # print(f'Area end at: {self.x_max}, {self.y_max}')

        # print(f'Occupied area: {self.occupied_area_square}')

        # print(f'Details area square:{self.details_square}')
        # print(f'Details area part {self.useful_part} %')

        # print(f'Unused area square: {self.unused_area_square}')
        print(f'Unused area part: {self.unused_area_part}')

        # print(f'Remain: x,y:({self.__remainX} {self.__remainY}) size:({self.__remain_width} {self.__remain_height})')
        # print()

    # Soritng details by square.
    def sort(self):
        sorted = self.chromosomes.copy()

        sorted.sort(key=get_square, reverse=True)

        return sorted
    
    # On polygons border expand.
    def expand_square(self, x: float, y:float):
        if (self.x_max < x):
            self.x_max = x
        if (self.y_max < y):
            self.y_max = y

        #print(f'Polygone expand: {self.x_max} {self.y_max}')

def get_square(chromosome):
        return chromosome.height * chromosome.width

# Chromosome equals detail.
class Chromosome:
    detail_id: uuid.uuid4
    width: float
    height: float
    rotation: float

    square: float
    
    def __init__(self, 
                detail_id: uuid.uuid4,
                width: float,
                height: float) -> None:
        self.detail_id = detail_id
        self.width = width
        self.height = height

        self.square = self.height * self.width

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