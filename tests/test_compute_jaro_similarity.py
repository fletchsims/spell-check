import pytest
from distances.edit_distance import EditDistance

edit = EditDistance()


def test_compute_jaro_similarity():
    assert edit.compute_jaro_similarity('FARMS', 'FARMR') == 4
    # FAREMVIEL # FARMVILLE
