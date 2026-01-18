def max_somme_contigue(lst):
    """
    Trouve la sous-liste contiguë avec la somme maximale (Kadane's algorithm).

    🌱 Optimisation :
    - Parcourt la liste UNE SEULE FOIS
    - Complexité O(n)
    - Évite toutes les boucles imbriquées inutiles
    """
    if len(lst) == 0:
        return 0
    max_sum = float('-inf')
    current_sum = 0

    for x in lst:
        current_sum = max(x, current_sum + x)  # soit on démarre à x, soit on continue la sous-liste
        max_sum = max(max_sum, current_sum)

    return max_sum
