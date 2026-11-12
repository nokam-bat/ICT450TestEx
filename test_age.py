# importe pytest pour les tests
import pytest
# importe la fonction is_adult de la page age
from age import is_adult


def test_adult_at_18():
    # Arrange
    age = 18

    # Act
    result = is_adult(age)

    # Assert
    assert result is True


def test_not_adult_at_17():
    # Arrange
    age = 17

    # Act
    result = is_adult(age)

    # Assert
    assert result is False


def test_adult_above_18():
    # Arrange
    age = 45

    # Act
    result = is_adult(age)

    # Assert
    assert result is True


def test_not_adult_zero():
    # Arrange
    age = 0

    # Act
    result = is_adult(age)

    # Assert
    assert result is False


def test_negative_age():
    # Arrange
    age = -5

    # Act
    result = is_adult(age)

    # Assert
    assert result is False


def test_invalid_type_raises_exception():
    # Arrange
    invalid_input = "dix-huit"

    # Act + Assert
    with pytest.raises(ValueError):
        is_adult(invalid_input)
