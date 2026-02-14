from app.cafe import Cafe
from app.errors import (
    VaccineError,
    NotWearingMaskError,
)


def go_to_cafe(friends: list[dict], cafe: Cafe) -> str:
    # KROK 1: Sprawdzamy tylko szczepienia u wszystkich
    # Jeśli ktokolwiek ma problem z vaccine, zwracamy ogólny komunikat
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotWearingMaskError:
                # Ignorujemy maski w pierwszym przebiegu, 
                # interesują nas tylko błędy VaccineError
                continue
    except VaccineError:
        return "All friends should be vaccinated"

    # KROK 2: Jeśli wszyscy są zaszczepieni, liczymy maski
    masks_to_buy = 0
    for friend in friends:
        if not friend.get("wearing_a_mask", False):
            masks_to_buy += 1

    if masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
