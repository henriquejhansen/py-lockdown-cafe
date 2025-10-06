from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list, cafe: Cafe) -> str:
    masks_to_buy = 0
    vaccine_error_found = False

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            # If any vaccine error occurs, we break immediately
            vaccine_error_found = True
            break
        except NotWearingMaskError:
            # Count friends without masks, but continue checking others
            masks_to_buy += 1

    if vaccine_error_found:
        return "All friends should be vaccinated"
    elif masks_to_buy > 0:
        return f"Friends should buy {masks_to_buy} masks"
    else:
        return f"Friends can go to {cafe.name}"
