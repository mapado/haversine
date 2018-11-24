from haversine import haversine

lyon = (45.7597, 4.8422)
paris = (48.8567, 2.3508)

def test_kilometers():
    assert haversine(lyon, paris) == 392.2172595594006  # in kilometers

def test_miles():
    assert haversine(lyon, paris, unit='mi') == 243.71250410685667  # in miles

def test_nautical_miles():
    assert haversine(lyon, paris, unit='nmi') == 211.78037487427127  # in nautical miles

def test_meters():
    assert haversine(lyon, paris, unit='m') == 392217.2595594006

def test_feets():
    assert haversine(lyon, paris, unit='ft') == 1286802.0326751503

def test_inches():
    assert haversine(lyon, paris, unit='in') ==  15441624.392102592
