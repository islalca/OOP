# 1
def print_line():
    print("+ - - - - + - - - - +")

def print_row():
    print("|         |         |")

def draw_grid_2x2():
    print_line()
    for i in range(4):
        print_row()
    print_line()
    for i in range(4):
        print_row()
    print_line()

draw_grid_2x2()

# 2
def print_line():
    print("+ - - - - + - - - - + - - - - + - - - - +")

def print_row():
    print("|         |         |         |         |")

def draw_grid_4x4():
    for i in range(4):
        print_line()
        for j in range(4):
            print_row()
    print_line()

draw_grid_4x4()