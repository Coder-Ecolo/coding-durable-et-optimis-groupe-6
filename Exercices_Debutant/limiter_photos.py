# limiter_photos.py

def limiter_photos(photos):
    """
    Retourne les 1000 dernières photos de la liste.

    Optimisé :
    - Utilise le slicing au lieu d'une boucle.
    - Complexité O(1) pour le slicing, beaucoup plus éco-responsable.
    """
    return photos[-1000:] if len(photos) > 1000 else photos
