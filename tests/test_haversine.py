from haversine import haversine, inverse_haversine

lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)


def test_kilometers():
    assert haversine(lyon, paris) == 392.2172595594006  # in kilometers


def test_miles():
    assert haversine(lyon, paris, miles=True) == 243.7125041070121  # in miles


def test_nautical_miles():
    assert haversine(lyon, paris, nautical_miles=True) == 211.7803748731092  # in nautical miles


def test_inverse_kilometers():
    assert inverse_haversine(paris, 32, 'west') == (48.8567, 1.9134030884190545)


def test_inverse_miles():
    assert inverse_haversine(paris, 50, 'north', miles=True) == (49.5803579218996, 2.3508)


def test_nautical_inverse_miles():
    assert inverse_haversine(paris, 10 ,'south', nautical_miles=True) == (48.69014586638915, 2.3508)