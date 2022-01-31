from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe):
    masks_to_buy = sum([
        1
        for friend in friends
        if not friend["wearing_a_mask"] or "wearing_a_mask" not in friend
    ])

    try:
        for friend in friends:
            cafe.visit_cafe(friend)
    except VaccineError:
        return "All friends should be vaccinated"
    except NotWearingMaskError:
        return f"Friends should buy {masks_to_buy} masks"

    return f"Friends can go to {cafe.name}"
