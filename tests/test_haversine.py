from haversine import haversine

def test_haversine():
    lyon = (45.7597, 4.8422)
    paris = (48.8567, 2.3508)

    assert haversine(lyon, paris) == 392.21671780659625  # in kilometers
    assert haversine(lyon, paris, miles=True) == 243.71209416020253  # in miles
