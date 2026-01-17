def solve_beach_cleanup(input_data):
    current_x, current_y = 0, 0
    total_steps = 0
    
    # Dividiamo l'input in righe
    lines = input_data.strip().split('\n')
    
    for line in lines:
        if not line.strip(): continue
        # Estraiamo x e y dalla riga (es: "3,3")
        target_x, target_y = map(int, line.split(','))
        
        # Calcoliamo la distanza di Manhattan
        steps = abs(target_x - current_x) + abs(target_y - current_y)
        total_steps += steps
        
        # Aggiorniamo la posizione attuale
        current_x, current_y = target_x, target_y
        
    return total_steps

# Incolla qui l'input tra le virgolette
my_input = """9,94
31,18
29,83
6,85
24,56
75,70
83,65
26,94
68,14
20,67
80,83
45,76
2,5
55,52
68,43
65,52
56,90
20,89
45,2
78,87
30,56
97,78
43,36
39,56
77,77
30,23
66,7
11,29
44,10
97,84
39,33
20,8
36,79
89,55
57,10
83,21
39,7
77,62
71,47
34,88
34,71
79,77
72,88
83,84
87,7
67,26
37,19
31,92
76,96
81,52
0,59
91,23
47,10
91,95
7,43
4,67
5,53
19,8
93,6
3,45
47,28
98,71
99,62
0,22
85,44
10,59
2,98
64,71
62,95
73,23
73,78
43,70
76,7
100,82
73,67
14,94
60,64
99,43
100,34
61,64
91,89
5,10
51,38
78,0
45,20
26,62
3,15
87,43
91,59
67,49
28,99
98,85
40,22
4,38
86,73
14,30
12,54
53,17
4,6
80,56"""
print(f"Il numero totale di passi è: {solve_beach_cleanup(my_input)}")
