def solve_tunnels(s):
    total_steps = 0
    pos = 0
    n = len(s)
    
    positions = {}
    for idx, char in enumerate(s):
        if char not in positions:
            positions[char] = []
        positions[char].append(idx)
    
    while pos < n:
        char = s[pos]
        pair = positions[char]
        other_pos = pair[1] if pair[0] == pos else pair[0]
        
        total_steps += abs(other_pos - pos)
        pos = other_pos + 1
            
    return total_steps

puzzle_input = "VyAsXFDvMHzaEJehigWRfECSIBszlukcutrSWUtRxpKyLPqYJZVOlTjMIbCQeYThcofqBLNndgDXHondpjwQAFKxPGZUkOairGNvwbmm"
print(solve_tunnels(puzzle_input))
