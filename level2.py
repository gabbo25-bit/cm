def find_highest_point(blueprint):
    current_height = 0
    max_height = 0
    
    for move in blueprint:
        if move == '^':
            current_height += 1
        elif move == 'v':
            current_height -= 1
        
        # Aggiorna il massimo se l'altezza attuale è superiore
        if current_height > max_height:
            max_height = current_height
            
    return max_height

# Incolla qui il tuo input tra le triple virgolette
puzzle_input = """^^^^^^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^v^^^^^^^^^^vvvvvvvvvvvvvv^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^vvvvvvvv^^^^^vvvvvvvvvvvvvvvvvv^^^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvv^^vvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^vvv^^^^^^^vvvvvvvvvvvv^^^^^^^^^^^^v^^^^^^^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^vvvvvv^^^vvvvvvvvvvvvvvv^vvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvvvvv^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^vvvvvvvvv^^^^^^^^^^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^vvvvvvvvv^^vvvvvvvvvvvv^^^^^^^^^^^^vvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvv^^^^^^^^^^^^^^^^^vvvvvvvvvvv^^^^^vv^^^^^^^^^^^^^^^^vvvvvv^^^^^^vvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^vvvvvvv^^^^^^^^^^^^^^^^vvvvvvv^^^^^^^^^^^^^^^^^^^vvvv^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^vvvv^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^vv^^^^^^^^vvvvvvvvvvvvv^vvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvv^^^^^^vvvvvvvvvvvvvvvvv^^^^^vvvvvv^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvv^^^^^^^^^^^^^^^^^^^^vvv^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvv^^^^^^^^^^^^^^^^^^^^v^^^^^^^^^^^v^^^^^^^^^^^^^^^^^^v^^^^^^^^^^^^^^^^^vvvvvvv^^^vvvvvvvv^^^^^vvv^^^^^^^^^^^vvvvvv^^^^^^^^^^^^^^^vvv^^^^^^vvvvvvvv^^^^^^^^^^^^^vvvvv^^^^^^^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvv^^^^^^^^^^^vvvvvvvvvvvvvvvvv^^^^^^^vvvvvv^vvvvvvvvvvvvvvvvvvv^^^^^^vvvvvvv^vvvvvvvvvv^^^^^^^^^^v^^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvv^^^^^^^^^^^^vvv^^^^^vvvvvvvvvvvv^^^^^^^^^vvvvvv^^^^^^^^^v^^^^^^^^^^^^vvvv^^^^^^^^^^^^^^^^vvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^vv^^^^^^^^^^^^^^^v^^^^vvvvvvvvvv^^^^^^^^vvvvvvvvvvvvvv^^^^^^^^^^^^vvvvvvvvvv^^^^^^^^^^^^^^vvvvvvvv^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^v^^^^^^^^^^^^^^^^^vvvvvvvvvv^^^^vvvvvvvvvv^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^vvvvvvvvvvv^^^^^^^^^^^^^^^vvv^^^^^^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^vvvvvv^^^^^^^vvvvvvv^^^^^^^^^^^^^vv^^^^vvvvvvvvvvvvvvvvvv^^^^^^v^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvv^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^vvvv^^vvvvvvvvvv^^^^^^^^vv^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^vvvvv^^^^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^^^^v^^^^^^vvvvvvvvvvvvvvv^vvvvvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvv^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^vvvvvvvv^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^vvv^^^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvv^^^^^vvvvvvvvvvvvvvvvvvv^^^^^vvvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvv^^^^^^vvvvvvvvvvvvvvvvvvvv^vvvvvvvv^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvvvv^^^^^^^^^^^vvvvvvvvv^^^^^^^^vvvvvvvvvvvvvv^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvv^^^^^^^^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^^^^^vvvvvvvvv^^^^^^^vvvvvvvvvvvvvvvvv^^^^^^^^^^vvvvvvvvvv^^^^vvvvvvvvvvvvvvv^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvvv^^^^^^^^^^^^^^^vvvvvvvvvvvv^^^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^^^^^^^^^^^^^^^vvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvvvvvvvvv^^^^^^vvvvvvvvv^^^^^^^^^^vvvvvvvvvvvvvvvvvvv^^^^^^^^vvvvvvvvvvvv^^^^^^^^^^^^^^^^^^vvvvvvvvvvvvvvvvv^^^^^^^^^^^^^vvvvvvvvv^^^^^^vvvvvvvvvvvvvvvv"""

print(f"Il punto più alto raggiunto è: {find_highest_point(puzzle_input)}")
