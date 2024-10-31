import random

number_of_iterations = int(input("Enter number of iterations: "))

distribution_dictionary = {}
total_distribution = []
total_points = []

for _ in range(number_of_iterations):

    spade_cards = 0
    heart_cards = 0
    diamond_cards = 0
    clubs_cards = 0
    cards_in_hand = []
    points = []

    for _ in range(100):
        randon_number = random.randint(1, 52)
        if randon_number not in cards_in_hand:
            cards_in_hand.append(randon_number)
        else:
            continue
        if len(cards_in_hand) == 13:
            break

    for card in cards_in_hand:
        if card in range(1, 14):
            spade_cards += 1

        elif card in range(14, 27):
            heart_cards += 1

        elif card in range(27, 40):
            diamond_cards += 1

        elif card in range(40, 53):
            clubs_cards += 1

    for num in cards_in_hand:
        if num in (1, 14, 27, 40):
            points.append(4)

        elif num in (11, 24, 37, 50):
            points.append(1)

        elif num in (12, 25, 38, 51):
            points.append(2)

        elif num in (13, 26, 39, 52):
            points.append(3)
    distribution = (spade_cards, heart_cards, diamond_cards, clubs_cards, sum(points))
    total_distribution.append(distribution)
    total_points.append(sum(points))

for num in total_distribution:
    if num not in distribution_dictionary:
        distribution_dictionary[num] = 1
    else:
        distribution_dictionary[num] += 1

print(f"{'-' * 100}")

sorted_distribution_dictionary = dict(sorted(distribution_dictionary.items(), key=lambda kv: (-kv[0][-1], -kv[1])))
counter = 0
two_to_five_cards = 0
cards_0 = 0
cards_1 = 0
cards_2 = 0
cards_3 = 0
cards_4 = 0
cards_5 = 0
cards_6 = 0
cards_7 = 0
cards_8 = 0
cards_9 = 0
cards_10 = 0
cards_11 = 0
cards_12 = 0
cards_13 = 0

for (key, value) in sorted_distribution_dictionary.items():
    counter += 1
    if 2 <= key[0] <= 5 and 2 <= key[1] <= 5 and 2 <= key[2] <= 5 and 2 <= key[3] <= 5:
        two_to_five_cards += value

    if key[0] == 0 or key[1] == 0 or key[2] == 0 or key[3] == 0:
        cards_0 += value
    if key[0] == 1 or key[1] == 1 or key[2] == 1 or key[3] == 1:
        cards_1 += value
    if key[0] == 2 or key[1] == 2 or key[2] == 2 or key[3] == 2:
        cards_2 += value
    if key[0] == 3 or key[1] == 3 or key[2] == 3 or key[3] == 3:
        cards_3 += value
    if key[0] == 4 or key[1] == 4 or key[2] == 4 or key[3] == 4:
        cards_4 += value
    if key[0] == 5 or key[1] == 5 or key[2] == 5 or key[3] == 5:
        cards_5 += value
    if key[0] == 6 or key[1] == 6 or key[2] == 6 or key[3] == 6:
        cards_6 += value
    if key[0] == 7 or key[1] == 7 or key[2] == 7 or key[3] == 7:
        cards_7 += value
    if key[0] == 8 or key[1] == 8 or key[2] == 8 or key[3] == 8:
        cards_8 += value
    if key[0] == 9 or key[1] == 9 or key[2] == 9 or key[3] == 9:
        cards_9 += value
    if key[0] == 10 or key[1] == 10 or key[2] == 10 or key[3] == 10:
        cards_10 += value
    if key[0] == 11 or key[1] == 11 or key[2] == 11 or key[3] == 11:
        cards_11 += value
    if key[0] == 12 or key[1] == 12 or key[2] == 12 or key[3] == 12:
        cards_12 += value
    if key[0] == 13 or key[1] == 13 or key[2] == 13 or key[3] == 13:
        cards_13 += value

    print(f"# {counter} - Points: {key[-1]:02d} --> Distribution: {key[0], key[1], key[2], key[3]} "
          f"--> Times: {value} --> {((value / number_of_iterations) * 100):.2f} %")
print()
print(f"Average points at this set: {(sum(total_points) / number_of_iterations):.2f}")
print()
print(f"{'-' * 100}")
print()
print(f"[2-5] cards in hands: {two_to_five_cards:_}  --> {((two_to_five_cards / number_of_iterations) * 100):.2f} %")
print(f"[0] cards in hands: {cards_0:_}  --> {((cards_0 / number_of_iterations) * 100):.2f} %")
print(f"[1] cards in hands: {cards_1:_}  --> {((cards_1 / number_of_iterations) * 100):.2f} %")
print(f"[2] cards in hands: {cards_2:_}  --> {((cards_2 / number_of_iterations) * 100):.2f} %")
print(f"[3] cards in hands: {cards_3:_}  --> {((cards_3 / number_of_iterations) * 100):.2f} %")
print(f"[4] cards in hands: {cards_4:_}  --> {((cards_4 / number_of_iterations) * 100):.2f} %")
print(f"[5] cards in hands: {cards_5:_}  --> {((cards_5 / number_of_iterations) * 100):.2f} %")
print(f"[6] cards in hands: {cards_6:_}  --> {((cards_6 / number_of_iterations) * 100):.2f} %")
print(f"[7] cards in hands: {cards_7:_}  --> {((cards_7 / number_of_iterations) * 100):.2f} %")
print(f"[8] cards in hands: {cards_8:_}  --> {((cards_8 / number_of_iterations) * 100):.2f} %")
print(f"[9] cards in hands: {cards_9:_}  --> {((cards_9 / number_of_iterations) * 100):.2f} %")
print(f"[10] cards in hands: {cards_10:_}  --> {((cards_10 / number_of_iterations) * 100):.2f} %")
print(f"[11] cards in hands: {cards_11:_}  --> {((cards_11 / number_of_iterations) * 100):.2f} %")
print(f"[12] cards in hands: {cards_12:_}  --> {((cards_12 / number_of_iterations) * 100):.2f} %")
print(f"[13] cards in hands: {cards_13:_}  --> {((cards_13 / number_of_iterations) * 100):.2f} %")
print(f"{'-' * 100}")