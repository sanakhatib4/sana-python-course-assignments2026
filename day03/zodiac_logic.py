import math
import ephem

def get_zodiac_sign_from_angle(angle):
    zodiac_ranges = [
        (0, "♈ Aries"), (30, "♉ Taurus"), (60, "♊ Gemini"),
        (90, "♋ Cancer"), (120, "♌ Leo"), (150, "♍ Virgo"),
        (180, "♎ Libra"), (210, "♏ Scorpio"), (240, "♐ Sagittarius"),
        (270, "♑ Capricorn"), (300, "♒ Aquarius"), (330, "♓ Pisces"), (360, "♈ Aries")
    ]
    for i in range(len(zodiac_ranges)-1):
        if zodiac_ranges[i][0] <= angle < zodiac_ranges[i+1][0]:
            return zodiac_ranges[i][1]
    return zodiac_ranges[0][1]

def get_moon_sign(date, lat, lon):
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    observer.date = date.strftime('%Y/%m/%d %H:%M:%S')
    moon = ephem.Moon()
    moon.compute(observer)
    # Convert moon longitude to degrees
    degrees = math.degrees(moon.elong) % 360
    return get_zodiac_sign_from_angle(degrees)

def get_rising_sign(date, lat, lon):
    observer = ephem.Observer()
    observer.lat = str(lat)
    observer.lon = str(lon)
    observer.date = date.strftime('%Y/%m/%d %H:%M:%S')
    sun = ephem.Sun()
    sun.compute(observer)
    # Calculate ascendant
    rasc = observer.sidereal_time() - sun.ra + math.pi
    degrees = math.degrees(rasc) % 360
    return get_zodiac_sign_from_angle(degrees)

def get_sun_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "♈ Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "♉ Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "♊ Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "♋ Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "♌ Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "♍ Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "♎ Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "♏ Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "♐ Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "♑ Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "♒ Aquarius"
    else:
        return "♓ Pisces"

def get_sign_description(sign):
    descriptions = {
        "♈ Aries": "Dynamic, confident, and adventurous. Natural leader with boundless energy.",
        "♉ Taurus": "Reliable, patient, and determined. Appreciates beauty and comfort.",
        "♊ Gemini": "Versatile, expressive, and curious. Quick-witted communicator.",
        "♋ Cancer": "Nurturing, intuitive, and emotional. Deep connection to home and family.",
        "♌ Leo": "Charismatic, generous, and proud. Born leader with a flair for drama.",
        "♍ Virgo": "Analytical, practical, and perfectionist. Detail-oriented problem solver.",
        "♎ Libra": "Harmonious, diplomatic, and charming. Seeks balance and beauty.",
        "♏ Scorpio": "Intense, passionate, and transformative. Deeply emotional and mysterious.",
        "♐ Sagittarius": "Optimistic, adventurous, and philosophical. Seeker of truth and wisdom.",
        "♑ Capricorn": "Ambitious, disciplined, and patient. Natural manager and achiever.",
        "♒ Aquarius": "Innovative, independent, and humanitarian. Forward-thinking visionary.",
        "♓ Pisces": "Compassionate, artistic, and intuitive. Deeply spiritual and empathetic."
    }
    return descriptions.get(sign, "Unknown sign")