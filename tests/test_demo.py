import pytest
from data_warehouse import check_dependency

@pytest.mark.my_test_suite
def test_data_warehouse_uses_tiny_pkg():
    assert check_dependency() == 204
