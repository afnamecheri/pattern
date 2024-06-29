def print_hexagon_grid(rows, cols): 
    print(" " + " ___ " * cols)
    for r in range(rows): 
        print(" " + "/ \\" * cols) 
        print(" " + "\\___/" * cols) 
inputs1 = (4, 7)
inputs2 = (3, 5)

print(f"inputs :- {inputs1[0]} {inputs1[1]}")
print_hexagon_grid(inputs1[0], inputs1[1])

print(f"\ninputs :- {inputs2[0]} {inputs2[1]}")
print_hexagon_grid(inputs2[0], inputs2[1])
