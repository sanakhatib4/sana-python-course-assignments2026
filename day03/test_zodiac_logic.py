import pytest
from zodiac_logic import get_zodiac_sign_from_angle, get_moon_sign, get_rising_sign, get_sun_sign, get_sign_description
from datetime import datetime

# Test get_zodiac_sign_from_angle
def test_get_zodiac_sign_from_angle():
    assert get_zodiac_sign_from_angle(15) == "♈ Aries"
    assert get_zodiac_sign_from_angle(45) == "♉ Taurus"
    assert get_zodiac_sign_from_angle(75) == "♊ Gemini"
    assert get_zodiac_sign_from_angle(105) == "♋ Cancer"
    assert get_zodiac_sign_from_angle(135) == "♌ Leo"
    assert get_zodiac_sign_from_angle(165) == "♍ Virgo"
    assert get_zodiac_sign_from_angle(195) == "♎ Libra"
    assert get_zodiac_sign_from_angle(225) == "♏ Scorpio"
    assert get_zodiac_sign_from_angle(255) == "♐ Sagittarius"
    assert get_zodiac_sign_from_angle(285) == "♑ Capricorn"
    assert get_zodiac_sign_from_angle(315) == "♒ Aquarius"
    assert get_zodiac_sign_from_angle(345) == "♓ Pisces"

# Test get_sun_sign
def test_get_sun_sign():
    assert get_sun_sign(21, 3) == "♈ Aries"
    assert get_sun_sign(20, 4) == "♉ Taurus"
    assert get_sun_sign(15, 6) == "♊ Gemini"
    assert get_sun_sign(10, 7) == "♋ Cancer"
    assert get_sun_sign(5, 8) == "♌ Leo"
    assert get_sun_sign(1, 9) == "♍ Virgo"
    assert get_sun_sign(10, 10) == "♎ Libra"
    assert get_sun_sign(5, 11) == "♏ Scorpio"
    assert get_sun_sign(25, 11) == "♐ Sagittarius"
    assert get_sun_sign(1, 1) == "♑ Capricorn"
    assert get_sun_sign(5, 2) == "♒ Aquarius"
    assert get_sun_sign(10, 3) == "♓ Pisces"

# Test get_sign_description
def test_get_sign_description():
    assert get_sign_description("♈ Aries") == "Dynamic, confident, and adventurous. Natural leader with boundless energy."
    assert get_sign_description("♉ Taurus") == "Reliable, patient, and determined. Appreciates beauty and comfort."
    assert get_sign_description("♊ Gemini") == "Versatile, expressive, and curious. Quick-witted communicator."
    assert get_sign_description("♋ Cancer") == "Nurturing, intuitive, and emotional. Deep connection to home and family."
    assert get_sign_description("♌ Leo") == "Charismatic, generous, and proud. Born leader with a flair for drama."
    assert get_sign_description("♍ Virgo") == "Analytical, practical, and perfectionist. Detail-oriented problem solver."
    assert get_sign_description("♎ Libra") == "Harmonious, diplomatic, and charming. Seeks balance and beauty."
    assert get_sign_description("♏ Scorpio") == "Intense, passionate, and transformative. Deeply emotional and mysterious."
    assert get_sign_description("♐ Sagittarius") == "Optimistic, adventurous, and philosophical. Seeker of truth and wisdom."
    assert get_sign_description("♑ Capricorn") == "Ambitious, disciplined, and patient. Natural manager and achiever."
    assert get_sign_description("♒ Aquarius") == "Innovative, independent, and humanitarian. Forward-thinking visionary."
    assert get_sign_description("♓ Pisces") == "Compassionate, artistic, and intuitive. Deeply spiritual and empathetic."

# Test get_moon_sign and get_rising_sign with mock data
def test_get_moon_sign():
    date = datetime(2025, 11, 22, 12, 0)
    lat, lon = 0, 0  # Mock coordinates
    assert isinstance(get_moon_sign(date, lat, lon), str)  # Check if it returns a string

def test_get_rising_sign():
    date = datetime(2025, 11, 22, 12, 0)
    lat, lon = 0, 0  # Mock coordinates
    assert isinstance(get_rising_sign(date, lat, lon), str)  # Check if it returns a string