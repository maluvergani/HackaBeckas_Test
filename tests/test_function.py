import pytest
from src.function import functionFoda


class TestfunctionFoda:
    def test_functionFoda(self):
        assert functionFoda() == "rellou"
