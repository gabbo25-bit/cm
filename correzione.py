import math
import os

def read_file(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as f:
        return f.read().strip()

def solve_p4_beach():
    data = read_file('input_p4.txt')
    if not data: return
    cx, cy, total = 0, 0, 0
    lines = data.split('\n')
    for line in lines:
        tx, ty = map(int, line.split(','))
        total += abs(tx - cx) + abs(ty - cy)
        cx, cy = tx, ty
    print(f"P4 - Beach Cleanup:")
    print(f"   1. Punti totali analizzati: {len(lines)}")
    print(f"   2. Ultima posizione raggiunta: ({cx}, {cy})")
    print(f"   3. RISPOSTA FINALE (Totale passi): {total}\n")

def solve_p5_tunnels():
    s = read_file('input_p5.txt')
    if not s: return
    total, pos, n = 0, 0, len(s)
    positions = {}
    for idx, char in enumerate(s):
        positions.setdefault(char, []).append(idx)
    while pos < n:
        char = s[pos]
        pair = positions[char]
        other_pos = pair[1] if pair[0] == pos else pair[0]
        total += abs(other_pos - pos)
        pos = other_pos + 1
    print(f"P5 - Strange Tunnels:")
    print(f"   1. Lunghezza stringa: {n}")
    print(f"   2. Numero tunnel unici: {len(positions)}")
    print(f"   3. RISPOSTA FINALE (Totale passi): {total}\n")

def solve_p6_birds():
    data = read_file('input_p6.txt')
    if not data: return
    count = 0
    lines = data.split('\n')
    for line in lines:
        vx, vy = map(int, line.split(','))
        xf, yf = (vx * 100) % 1000, (vy * 100) % 1000
        if 250 <= xf < 750 and 250 <= yf < 750:
            count += 1
    print(f"P6 - Bird Spotters:")
    print(f"   1. Uccelli totali: {len(lines)}")
    print(f"   2. Tempo simulazione: 100s")
    print(f"   3. RISPOSTA FINALE (Uccelli in frame): {count}\n")

def solve_p7_grids():
    data = read_file('input_p7.txt')
    if not data: return
    total_paths = 0
    lines = data.split('\n')
    for line in lines:
        r, c = map(int, line.split())
        total_paths += math.comb((r-1) + (c-1), r-1)
    print(f"P7 - Hyper Grids:")
    print(f"   1. Numero griglie nel file: {len(lines)}")
    print(f"   2. Esempio ultima griglia: {lines[-1]}")
    print(f"   3. RISPOSTA FINALE (Somma percorsi): {total_paths}\n")

if __name__ == "__main__":
    # Assicurati di avere i file input_p4.txt, input_p5.txt, ecc. nella stessa cartella
    solve_p4_beach()
    solve_p5_tunnels()
    solve_p6_birds()
    solve_p7_grids()
