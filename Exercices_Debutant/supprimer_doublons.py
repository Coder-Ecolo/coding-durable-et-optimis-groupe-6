def supprimer_doublons(fichiers):
    """
    Supprime les doublons tout en conservant l'ordre, de manière efficace.

    🌱 Optimisation :
    - Utilise un set pour vérifier les doublons (O(1) par élément)
    - Conserve l'ordre original
    - Complexité O(n)
    """
    seen = set()
    result = []

    for f in fichiers:
        if f not in seen:
            seen.add(f)
            result.append(f)

    return result
