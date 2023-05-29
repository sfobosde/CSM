from .models import *
from .binaryTree import Polygone

class Polygone:
    x: float
    y: float

    width: float
    height: float

    detail: Chromosome

    down: Polygone
    right: Polygone
    root: Polygone

    is_free: bool

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

        self.x = 0
        self.y = 0

        self.root = None

        is_free = True

    def add_detail(self, detail: Chromosome, polygone: Polygone = None):
        if polygone == None:
            polygone = self

        if polygone.can_place(detail) and polygone.is_free:
            polygone.width = detail.width
            polygone.height = detail.height

            polygone.down = Polygone(detail.width, polygone.height - detail.height)
            polygone.down.y = self.y + detail.height
            polygone.down.x = self.x
            polygone.down.root = self

            polygone.right = Polygone(polygone.width - detail.width, polygone.height)
            polygone.right.x = polygone.x + detail.width
            polygone
            polygone.right.root = self

            polygone.is_free = False
            polygone.detail = detail

        elif (polygone.down != None
            and polygone.down.can_place(detail) 
            and polygone.down.is_free):
            polygone.down.add_detail(detail, polygone.down)

        elif (polygone.right != None
            and polygone.right.can_place(detail) 
            and polygone.right.is_free):
            polygone.right.add_detail(detail, polygone.right)

        elif (polygone.root != None
              and polygone.root.right != None
              and polygone.root.right.can_place(detail)
              and polygone.root.right.is_free):
            polygone.root.right.add_detail(detail, polygone.root.right)

    def can_place(self, detail: Chromosome):
        polygone_square = self.height * self.width
        detail_square = detail.height * detail.width

        return (
            detail_square <= polygone_square
            and detail.height <= self.height
            and detail.width <= self.width 
        )