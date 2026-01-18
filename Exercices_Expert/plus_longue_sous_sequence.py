from bisect import bisect_left

def plus_long_sous_sequence(lst):
    """
    Trouver la longueur de la plus longue sous-séquence croissante.

    🌱 Optimisation :
    - Patience sorting + bisect → O(n log n)
    - Pas de récursion inutile
    - Utilise mémoire minimale et opérations réduites
    """
    sub = []  # sub[i] = smallest last element of an increasing subsequence of length i+1
    for x in lst:
        # Trouver l'emplacement où x peut aller
        i = bisect_left(sub, x)
        if i == len(sub):
            sub.append(x)  # x prolonge la plus longue sous-séquence
        else:
            sub[i] = x     # x remplace un élément plus grand pour garder sub optimal
    return len(sub)
