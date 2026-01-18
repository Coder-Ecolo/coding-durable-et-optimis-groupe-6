def tri_eco(lst):
    """
    Tri d'une liste de manière éco-responsable.

    🌱 Optimisation :
    - Utilise Python built-in sorted() (Timsort)
    - Complexité O(n log n)
    - Beaucoup moins de comparaisons → meilleur ECO-SCORE
    """
    return sorted(lst)
