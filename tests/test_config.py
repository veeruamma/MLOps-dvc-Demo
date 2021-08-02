import pytest

class NotInrange(Exception):
    def __init__(self, message="Value is not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a=5
    with pytest.raises(NotInrange):
        if a not in range(10, 20):
            raise NotInrange