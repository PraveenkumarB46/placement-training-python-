def first_non_repeating(s):
    from collections import Counter
    freq = Counter(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None
