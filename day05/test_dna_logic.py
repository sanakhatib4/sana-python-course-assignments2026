from dna_logic import validate_guess, score_guess


def test_validate_guess_ok():
    assert validate_guess("acgt") == "ACGT"
    assert validate_guess(" ACGT ") == "ACGT"


def test_validate_guess_wrong_length():
    import pytest
    with pytest.raises(ValueError):
        validate_guess("ACG")  
    with pytest.raises(ValueError):
        validate_guess("ACGTT")  


def test_validate_guess_invalid_chars():
    import pytest
    with pytest.raises(ValueError):
        validate_guess("AXGT")  


def test_score_guess_all_exact():
    secret = "ACGT"
    guess = "ACGT"
    exact, partial = score_guess(secret, guess)
    assert exact == 4
    assert partial == 0


def test_score_guess_none_match():
    secret = "AAAA"
    guess = "CCCC"
    exact, partial = score_guess(secret, guess)
    assert exact == 0
    assert partial == 0


def test_score_guess_partial_only():
    secret = "ACGT"
    guess = "TGCA"  
    exact, partial = score_guess(secret, guess)
    assert exact == 0
    assert partial == 4


def test_score_guess_mixed():
    secret = "ACGT"
    guess = "AGCT"  
    exact, partial = score_guess(secret, guess)
    assert exact == 2  
    assert partial == 2  
