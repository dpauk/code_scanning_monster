from unittest.mock import patch
import pytest
import random

from rock_paper_scissors.rock_paper_scissors import get_computer_guess, is_human_guess_valid, get_human_guess, get_winner


@patch.object(random, 'randint')
def test_get_computer_guess(m):
    m.return_value = 2
    assert get_computer_guess() == 'scissors'


def test_is_human_guess_valid_with_valid_guess():
    assert is_human_guess_valid(2) == True


def test_is_human_guess_valid_with_letter():
    with pytest.raises(ValueError):
        is_human_guess_valid('k')


def test_is_human_guess_valid_with_too_low_number():
    assert is_human_guess_valid(0) == False


def test_is_human_guess_valid_with_too_high_number():
    assert is_human_guess_valid(4) == False


@patch ("builtins.input", side_effect=[0, 1, 2, 3, 'k'])
def test_get_human_guess(input, capfd):
    # get_human_guess()

    # 0 is invalid
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_human_guess()
        out, _ = capfd.readouterr()
        assert out.rstrip() == 'Invalid guess.'
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

    # 1 returns rock
    assert get_human_guess() == 'rock'

    # 2 returns paper
    assert get_human_guess() == 'paper'

    # 3 returns scissors
    assert get_human_guess() == 'scissors'

    # 'k' returns ValueError
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        get_human_guess()
        out, _ = capfd.readouterr()
        assert out.rstrip() == 'Invalid guess.'
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

@pytest.mark.parametrize("human, computer", [
    ('rock', 'rock'),
    ('paper', 'paper'),
    ('scissors', 'scissors'),
])
def test_get_winner_its_a_draw(human, computer, capfd):
    get_winner(human, computer)
    out, _ = capfd.readouterr()
    assert out.rstrip() == 'Both have chosen the same.'


@pytest.mark.parametrize("human, computer", [
    ('rock', 'scissors'),
    ('paper', 'rock'),
    ('scissors', 'paper'),
])
def test_get_winner_human_wins(human, computer, capfd):
    get_winner(human, computer)
    out, _ = capfd.readouterr()
    assert out.rstrip() == f'You have chosen {human.capitalize()}, Computer has chosen {computer.capitalize()}'


@pytest.mark.parametrize("human, computer", [
    ('rock', 'paper'),
    ('paper', 'scissors'),
    ('scissors', 'rock')
])
def test_get_winner_computer_wins(human, computer, capfd):
    get_winner(human, computer)
    out, _ = capfd.readouterr()
    assert out.rstrip() == f'You have chosen {human.capitalize()}, Computer has chosen {computer.capitalize()}'
