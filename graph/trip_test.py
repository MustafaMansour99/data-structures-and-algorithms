import pytest
from graph.graph import *

def test1():
    syria_airlines_route_map = {
    "Seattle": {"San Francisco": 250, "Los Angeles": 200, "Denver": 300},
    "San Francisco": {"Seattle": 250, "Los Angeles": 150},
    "Los Angeles": {"Seattle": 200, "San Francisco": 150, "Denver": 350},
    "Denver": {"Seattle": 300, "Los Angeles": 350}
}

    cities = ["Seattle", "San Francisco"]
    expected = 250
    actual = Graph.business_trip(syria_airlines_route_map,cities)
    assert actual==expected
def test2():
    Jordanian_airlines_route_map = {
    "Seattle": {"San Francisco": 250, "Los Angeles": 200, "Denver": 300},
    "San Francisco": {"Seattle": 250, "Los Angeles": 150},
    "Los Angeles": {"Seattle": 200, "San Francisco": 150, "Denver": 350},
    "Denver": {"Seattle": 300, "Los Angeles": 350}
}

    cities = ["Seattle", "San Francisco","Los Angeles"]
    expected = 400
    actual = Graph.business_trip(Jordanian_airlines_route_map,cities)
    assert actual==expected
