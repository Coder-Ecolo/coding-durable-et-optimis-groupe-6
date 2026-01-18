def nettoyer_mails(mails):
    """
    Supprime les doublons et les mails indésirables ("spam" ou "pub") de manière efficace.

    🌱 Optimisation :
    - Utilise un set pour détecter les doublons (O(1) par mail)
    - Filtre "spam" et "pub" directement
    - Complexité globale O(n)
    """
    seen = set()
    result = []

    for mail in mails:
        if mail in ("spam", "pub"):
            continue  # ignore unwanted mails
        if mail not in seen:
            seen.add(mail)
            result.append(mail)

    return result
