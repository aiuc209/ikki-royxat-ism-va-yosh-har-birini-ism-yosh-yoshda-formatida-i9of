import pytest

def combine_names_and_ages(names, ages):
    return [f"{name} ({age} yoshda)" for name, age in zip(names, ages)]

def test_combine_names_and_ages():
    names = ["Ali", "Vali", "Jasur"]
    ages = [20, 25, 30]
    expected_result = ["Ali (20 yoshda)", "Vali (25 yoshda)", "Jasur (30 yoshda)"]
    assert combine_names_and_ages(names, ages) == expected_result

def test_combine_names_and_ages_empty_lists():
    names = []
    ages = []
    expected_result = []
    assert combine_names_and_ages(names, ages) == expected_result

def test_combine_names_and_ages_unequal_length_lists():
    names = ["Ali", "Vali", "Jasur"]
    ages = [20, 25]
    with pytest.raises(ValueError):
        combine_names_and_ages(names, ages)
