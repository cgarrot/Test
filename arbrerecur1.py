import turtle as t
 
def y(length=100):
    
    if length < 10:
           return       # échappe la fonction
    t.fd(length)        # peint la grosse branche de l'arbre
    t.left(30)          # s'oriente vers la gauche pour la première branche dérivée de la parente
    y(length * 0.6)      # crée une plus petites branche, de deux tiers la longueur de la branche parente
    t.right(60)         # s'oriente vers la droite pour la seconde branche dérivée de la parente
    y(length * 0.6)      # crée la seconde petite branche
    t.left(30)          # s'oriente vers le point de départ des petites branches
    t.fd(-length)       # revient au point de départ des petites branches
    return