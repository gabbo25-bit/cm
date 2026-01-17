import math

def solve_all_puzzles():
    # --- PUZZLE 4: BEACH CLEANUP ---
    def beach_cleanup(coords):
        cx, cy = 0, 0
        total_steps = 0
        for line in coords:
            tx, ty = map(int, line.split(','))
            total_steps += abs(tx - cx) + abs(ty - cy)
            cx, cy = tx, ty
        return total_steps

    # --- PUZZLE 5: STRANGE TUNNELS ---
    def strange_tunnels(s):
        total_steps, pos, n = 0, 0, len(s)
        positions = {}
        for idx, char in enumerate(s):
            positions.setdefault(char, []).append(idx)
        while pos < n:
            char = s[pos]
            pair = positions[char]
            other_pos = pair[1] if pair[0] == pos else pair[0]
            total_steps += abs(other_pos - pos)
            pos = other_pos + 1
        return total_steps

    # --- PUZZLE 7: HYPER GRIDS ---
    def hyper_grids(grids):
        total_paths = 0
        for line in grids:
            r, c = map(int, line.split())
            total_paths += math.comb((r-1) + (c-1), r-1)
        return total_paths

    # ESEMPIO DI ESECUZIONE (Sostituisci con i tuoi dati reali)
    # Dati Puzzle 4
    p4_data = ["9,94", "31,18", "29,83", "6,85", "24,56"] # ... continua
    
    # Dati Puzzle 5
    p5_data = "VyAsXFDvMHzaEJehigWRfECSIBszlukcutrSWUtRxpKyLPqYJZVOlTjMIbCQeYThcofqBLNndgDXHondpjwQAFKxPGZUkOairGNvwbmm"
    
    # Dati Puzzle 7
    p7_data = ["4 5", "4 6", "6 3", "6 4", "8 3"]

    print("--- SOLUZIONI C-LAND ---")
    print(f"Puzzle 4 (Beach): {beach_cleanup(p4_data)} passi")
    print(f"Puzzle 5 (Tunnels): {strange_tunnels(p5_data)} passi")
    print(f"Puzzle 7 (Grids): {hyper_grids(p7_data)} percorsi")

if __name__ == "__main__":
    solve_all_puzzles()
