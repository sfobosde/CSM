from MapCreator import *
from models import *

def test():
    details = [
    {"detail_id": uuid.uuid4(), "width": 117, "length": 101},
    {"detail_id": uuid.uuid4(), "width": 117, "length": 101},
    {"detail_id": uuid.uuid4(), "width": 117, "length": 101},
    {"detail_id": uuid.uuid4(), "width": 117, "length": 101},
    {"detail_id": uuid.uuid4(), "width": 117, "length": 101},

    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},
    {"detail_id": uuid.uuid4(), "width": 47, "length": 131},

    {"detail_id": uuid.uuid4(), "width": 147, "length": 85},
    {"detail_id": uuid.uuid4(), "width": 147, "length": 85},
    {"detail_id": uuid.uuid4(), "width": 147, "length": 85},
    {"detail_id": uuid.uuid4(), "width": 147, "length": 85},

    {"detail_id": uuid.uuid4(), "width": 69, "length": 20},

    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
    {"detail_id": uuid.uuid4(), "width": 155, "length": 117},
]

    material = Material(width=890, height=510, sheet_id=None)

    generation: Generation = create_map(material=material, details=details, generations_count=10, individuals_count=100, unused_limit=10)

    for inivid in generation.individuals:
        individ: Individual = inivid
    
        for chromosome in individ.chromosomes:
            chrom: Chromosome = chromosome

            #print(f'{chrom.height}\t{chrom.width}\n')

        #print("=================")

if __name__ == '__main__':
    test()