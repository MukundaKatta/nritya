"""Tests for Nritya."""
from src.core import Nritya
def test_init(): assert Nritya().get_stats()["ops"] == 0
def test_op(): c = Nritya(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Nritya(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Nritya(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Nritya(); r = c.process(); assert r["service"] == "nritya"
