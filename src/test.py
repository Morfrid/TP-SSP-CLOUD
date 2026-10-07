from voiture import Voiture

def test_accelere_incremente_vitesse():
    # GIVEN
    v = Voiture("4L", "verte")

    # WHEN
    v.accelere(5)

    # THEN
    assert v.vitesse == 5

def test_accelere_limite_increment():
    # GIVEN
    v = Voiture("4L", "verte")

    # WHEN
    v.accelere(20)

    # THEN
    assert v.vitesse == 10


    