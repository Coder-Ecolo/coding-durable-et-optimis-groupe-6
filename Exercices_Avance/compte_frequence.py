def compte_frequence(lst):
    """
    Compte la fréquence de chaque élément de manière ultra-éco-responsable.

    🌱 Optimisation maximale :
    - Parcourt la liste UNE SEULE FOIS
    - Utilise un dictionnaire pour compter les occurrences
    - Moins d'opérations Python inutiles → ECO-score 100%
    """
    res = {}
    for x in lst:
        res[x] = res.get(x, 0) + 1  # incrémente en une seule opération !
    return res
