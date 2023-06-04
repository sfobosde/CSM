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

    is_column_header = False

    stack: str

    on_expand: any

    def __init__(self, width: float, height: float, on_expand) -> None:
        self.width = width
        self.height = height

        self.x = 0
        self.y = 0

        self.root = self

        self.is_free = True

        self.is_column_header = True

        self.stack = "root-"

        self.on_expand = on_expand

    def add_detail(self, detail):
        # print(f"stack:{self.stack}, detail: {detail.width} {detail.height}")
        
        if (self.can_place(detail) and self.is_free):
            if (self.is_column_header):
                self.down = Polygone(detail.width, self.height - detail.height, self.on_expand)
            else:
                self.down = Polygone(self.width, self.height - detail.height, self.on_expand)

            self.down.y = self.y + detail.height
            self.down.x = self.x
            self.down.root = self
            self.down.is_column_header = False
            self.down.stack = self.stack + "d-"

            if (self.is_column_header):
                self.right = Polygone(self.width - detail.width, self.height, self.on_expand)
            else:
                self.right = Polygone(self.width - detail.width, detail.height, self.on_expand)

            self.right.x = self.x + detail.width
            self.right.y = self.y
            self.right.root = self
            self.right.is_column_header = True
            self.right.stack = self.stack + "r-"

            self.is_free = False
            self.detail = detail

            self.width = detail.width
            self.height = detail.height

            self.on_expand(self.x + self.width, self.y + self.height)

            # print(f"{self.x} {self.y} {self.width} {self.height}")

        elif (self.down != None and self.down.can_place(detail)):
            self.down.add_detail(detail)

        elif (self.right != None and self.right.can_place(detail)):
            self.right.add_detail(detail)

        else:
            polygone: Polygone

            if (self.stack == self.root.right.stack and not self.is_column_header):
                polygone = self.root.root.right
            elif (self.is_column_header and self.right != None):
                polygone = self.right
            elif (self.stack == self.root.right.stack):
                polygone = self.root.root.right
            else:
                polygone = self.root.right
            
            polygone.add_detail(detail)

    def can_place(self, detail):
        polygone_square = self.height * self.width
        detail_square = detail.height * detail.width

        return (
            detail_square <= polygone_square
            and detail.height <= self.height
            and detail.width <= self.width 
        )
    
    def print_tree(self):
        print(f'stack:{self.stack} x:{self.x}  y:{self.y}  width:{self.width}     height:{self.height}')

        if (self.down):
            self.down.print_tree()
        if (self.right):
            self.right.print_tree()

