def trouver_sous_sequence(seq, subseq):
    """
    Vérifie si `subseq` apparaît dans `seq` de manière éco-responsable.

    🌱 Optimisation ECO :
    - Pas de slices → pas de copies inutiles
    - Compare directement chaque élément
    - Arrêt immédiat dès qu'un élément diffère
    - Complexité O(n*m) mais plus rapide et moins gourmand en mémoire
    """
    n = len(seq)
    m = len(subseq)
    
    for i in range(n - m + 1):
        for j in range(m):
            if seq[i + j] != subseq[j]:
                break  # arrêt précoce dès qu'un élément diffère
        else:
            return True  # toutes les positions correspondent
    return False
