import re

input = [re.sub('\n','', x).split() for x in open('input.txt').readlines()]
cards = {hand:int(bid) for hand,bid in input}

card_vals = {c:i+1 for i,c in enumerate(reversed(['A','K','Q','J','T','9','8','7','6','5','4','3','2']))}

def hand_type(hand):
    unq_cards = set(hand)
    unq_len = len(unq_cards)
    if unq_len == 1:
        return 7
    elif unq_len == 5:
        return 1
    else:
        most = max([len(re.findall(x, hand)) for x in unq_cards])
        if most == 4:
            return 6
        elif most == 3:
            return 5 if unq_len == 2 else 4
        elif most == 2:
            return 3 if unq_len == 3 else 2
        


def sort_hands(hand1, hand2):
    rank1 = hand_type(hand1)
    rank2 = hand_type(hand2)
    if rank1 > rank2:
        return 0
    elif rank2 > rank1:
        return 1
    i = 0
    while hand1[i] == hand2[i]:
        i += 1
    
    if card_vals[hand1[i]] > card_vals[hand2[i]]:
        return 0
    else:
        return 1

# Adapted from https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python
def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if sort_hands(left[index_left], right[index_right]) == 0:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

rank = merge_sort(list(cards.keys()))
rank.reverse()

# solution
winnings = sum([cards[hand]*(i+1) for i, hand in enumerate(rank)])