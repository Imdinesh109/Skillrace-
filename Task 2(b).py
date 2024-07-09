def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    freq1 = {}
    for letter in name1:
        if letter in freq1:
            freq1[letter] += 1
        else:
            freq1[letter] = 1
    freq2 = {}
    for letter in name2:
        if letter in freq2:
            freq2[letter] += 1
        else:
            freq2[letter] = 1
    total_count = 0
    for letter in set(name1 + name2):
        count1 = freq1.get(letter, 0)
        count2 = freq2.get(letter, 0)
        total_count += abs(count1 - count2)
    flames = ["Friends", "Lovers", "Affectionate", "Marriage", "Enemies", "Siblings"]
    while len(flames) > 1:
        split_index = (total_count % len(flames)) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
result = flames_game(name1, name2)
print(f"The relationship between {name1} and {name2} is: {result}")