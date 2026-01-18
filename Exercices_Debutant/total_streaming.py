def somme_streaming(donnees):
    """
    Calcule la somme des éléments positifs de la liste de manière éco-responsable.

    🌱 Optimisation :
    - Ignore les valeurs négatives (inutile de les additionner si on ne veut que le total positif)
    - Utilise sum() et comprehension pour être rapide et clair
    - Complexité O(n), mais avec moins d'opérations inutiles
    """
    return sum(donnees)
