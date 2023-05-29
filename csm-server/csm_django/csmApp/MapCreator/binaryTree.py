class Polygone:
    x: float
    y: float

    width: float
    height: float

    detail = None

    down = None
    right = None
    root = None

    is_free: bool

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

        self.x = 0
        self.y = 0

        self.root = None

        self.is_free = True

    def add_detail(self, detail):
        if (self.can_place(detail) and self.is_free):
            self.down = Polygone(detail.width, self.height - detail.height)
            self.down.y = self.y + detail.height
            self.down.x = self.x
            self.down.root = self

            self.right = Polygone(self.width - detail.width, self.height)
            self.right.x = self.x + detail.width
            self.right.y = self.y
            self.right.root = self

            self.is_free = False
            self.detail = detail

            self.width = detail.width
            self.height = detail.height
            print(f"{self.x} {self.y} {self.width} {self.height}")

        elif (self.down != None
            and self.down.can_place(detail) 
            and self.down.is_free):
            self.down.add_detail(detail)

        elif (self.right != None
            and self.right.can_place(detail) 
            and self.right.is_free):
            self.right.add_detail(detail)

        elif (self.root != None
              and self.root.right != None
              and self.root.right.can_place(detail)
              and self.root.right.is_free):
            self.root.right.add_detail(detail)

        else:
            raise Exception("Cant place")

    def can_place(self, detail):
        polygone_square = self.height * self.width
        detail_square = detail.height * detail.width

        return (
            detail_square <= polygone_square
            and detail.height <= self.height
            and detail.width <= self.width 
        )
    
    def print_tree(self):
        print(f'x:{self.x}  y:{self.y}  width:{self.width}     height:{self.height}')

        if (self.down):
            self.print_tree(self.down)
        if (self.right):
            self.print_tree(self.right)

