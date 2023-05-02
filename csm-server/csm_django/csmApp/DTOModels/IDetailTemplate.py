# Interface to serialize DetailTemplate from json.
class IDetailTemplate():
    id: str
    file_link: str
    name: str
    length: int
    width: int
    fitness: int
    additional_data: str