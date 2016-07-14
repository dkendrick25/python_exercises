## Is it a straight?

# Implement a function to determine if a list of 7 cards is a straight. The cards will be represented as numbers representing the point values of the cards. is_straight(cards). Example:
#
# is_straight([1, 2, 3, 4, 5, 6, 7]) => True
# is_straight([4, 2, 1, 8, 3, 5]) => True
# is_straight([1, 2, 3, 3, 3, 4, 5]) => True
# is_straight([4, 4, 2, 1, 9, 10, 11]) => False

def is_straight(cards):
    streak = 1
    cards.sort()
    for i in range(1,len(cards)):
        current_card = cards[i]
        prev_card = cards[i - 1]
        if (current_card - prev_card) == 1:
            streak = streak + 1
        elif current_card == prev_card:
            pass
        else:
            streak = 1

        if streak == 5:
            return True

    return False


print is_straight([1, 2, 3, 4, 5, 6, 7])
print is_straight([4, 2, 1, 8, 3, 5])
print is_straight([1, 2, 3, 3, 3, 4, 5])
print is_straight([4, 4, 2, 1, 9, 10, 11])
