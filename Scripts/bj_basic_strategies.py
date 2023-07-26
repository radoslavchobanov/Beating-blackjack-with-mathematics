def should_hit_hard_hand(hand_value, dealer_upcard):
    """
        Determine whether the player should hit a hard hand based on the player's hand value and the dealer's upcard.

        Arguments:
        - hand_value: The numerical value of the player's hand.
        - dealer_upcard: The rank of the dealer's upcard.

        Returns:
        - True if the player should hit, False otherwise.
    """
    
    # Always hit when the hand value is 11 or lower
    if hand_value <= 11:
        return True
    # Hit when the hand value is 12 and the dealer's upcard is not 4, 5, or 6
    elif hand_value == 12 and dealer_upcard not in {'4', '5', '6'}:
        return True
    # Hit when the hand value is 13, 14, 15, or 16 and the dealer's upcard is 7, 8, 9, 10, J, Q, K, or A
    elif hand_value in {13, 14, 15, 16} and dealer_upcard in {'7', '8', '9', '10', 'J', 'Q', 'K', 'A'}:
        return True
    # Stand (do not hit) for any other hand value and dealer's upcard
    else:
        return False


def should_hit_soft_hand(hand_value, dealer_upcard):
    """
        Determine whether the player should hit a soft hand based on the player's hand value and the dealer's upcard.

        Arguments:
        - hand_value: The numerical value of the player's hand.
        - dealer_upcard: The rank of the dealer's upcard.

        Returns:
        - True if the player should hit, False otherwise.
    """
    
    # Always hit when the hand value is 17 or lower
    if hand_value <= 17:
        return True
    # Hit when the hand value is 18 and the dealer's upcard is 9, 10, J, Q, K, or A
    elif hand_value == 18 and dealer_upcard in {'9', '10', 'J', 'Q', 'K', 'A'}:
        return True
    # Stand (do not hit) for any other hand value and dealer's upcard
    else:
        return False
