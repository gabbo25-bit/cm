import math

def solve_hyper_grids(input_data):
    total_paths_sum = 0
    
    # Dividiamo l'input in righe
    lines = input_data.strip().split('\n')
    
    for line in lines:
        if not line.strip(): continue
        
        # Leggiamo Righe (R) e Colonne (C)
        r, c = map(int, line.split())
        
        # Numero di passi necessari per muoversi tra le celle
        # Se la griglia è R x C, i passi sono (R-1) e (C-1)
        steps_down = r - 1
        steps_right = c - 1
        n = steps_down + steps_right
        k = steps_down
        
        # Calcoliamo le combinazioni distinte: n! / (k! * (n-k)!)
        paths = math.comb(n, k)
        total_paths_sum += paths
        
    return total_paths_sum

# Il tuo input specifico
puzzle_input = """4 5
4 6
6 3
6 4
8 3"""

result = solve_hyper_grids(puzzle_input)
print(f"La somma totale dei percorsi è: {result}")
