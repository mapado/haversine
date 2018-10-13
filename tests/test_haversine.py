from haversine import haversine

lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)

def test_kilometers():
    assert haversine(lyon, paris) == 392.2172595594006  # in kilometers

def test_miles():
    assert haversine(lyon, paris, miles=True) == 243.7125041070121  # in miles

def test_nautical_miles():
    assert haversine(lyon, paris, nautical_miles=True) == 211.7803748731092  # in nautical miles
