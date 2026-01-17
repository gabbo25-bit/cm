import math

def solve_guild_challenge(filename):
    total_distinct_paths = 0
    
    print(f"{'Griglia':<10} | {'Lunghezza':<10} | {'Percorsi Distinti'}")
    print("-" * 45)

    try:
        with open(filename, 'r') as file:
            for line in file:
                if not line.strip():
                    continue
                
                # Legge R e C
                r, c = map(int, line.split())
                
                # 1. Lunghezza del percorso più breve (steps)
                # Si sottraggono 1 perché contiamo i passi tra le celle
                steps_down = r - 1
                steps_right = c - 1
                path_length = steps_down + steps_right
                
                # 2. Numero di percorsi distinti (Combinatoria)
                distinct_paths = math.comb(path_length, steps_down)
                
                # 3. Aggiorna la somma totale
                total_distinct_paths += distinct_paths
                
                print(f"{r}x{c:<8} | {path_length:<10} | {distinct_paths}")

        print("-" * 45)
        print(f"SOMMA TOTALE DEI PERCORSI: {total_distinct_paths}")

    except FileNotFoundError:
        print("Errore: Il file 'input.txt' non è stato trovato.")

# Esecuzione
if __name__ == "__main__":
    solve_guild_challenge('input.txt')
