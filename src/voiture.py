class Voiture:
    """Classe représentant une voiture.

    Attributes
    ----------
    nom : str
        le nom de la voiture.
    couleur : str
        la couleur de la voiture.
    vitesse : int
        la vitesse de la voiture (initialisée à 0).
    """
    def __init__(self, nom: str, couleur: str):
        """Constructeur"""
        self.nom = nom
        self.couleur = couleur
        self.vitesse = 42

    def __str__(self):
        return f"La voiture {self.nom} de couleur {self.couleur} roule à {self.vitesse} km/h."

            # ...

    def accelere(self, increment:int) -> None:
        """Augmente la vitesse de la voiture.

        L'incrément maximal est de 10 km/h.
        La vitesse maximale est de 130 km/h.

        Parameters
        ----------
        increment : int
            la valeur de l'accélération demandée (limité à 10)
        """
        if increment > 10:
            increment = 10
        self.vitesse = min(160, self.vitesse + increment)