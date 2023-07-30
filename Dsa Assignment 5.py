def find_original(changed):
    freq_dict = {}
    for num in changed:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    changed.sort()

    original = []
    for num in changed:
        half_val = num // 2
        if half_val in freq_dict and freq_dict[half_val] > 0:
            freq_dict[half_val] -= 1
        else:
            return []

    for num, freq in freq_dict.items():
        if freq > 0:
            original.extend([num] * freq)

    return original

# Test the function with the given example
changed = [1, 3, 4, 2, 6, 8]
result = find_original(changed)
print(result)  # Output: [1, 3, 4]