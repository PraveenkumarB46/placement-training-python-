def group_anagrams(words):
    from collections import defaultdict
    result = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        result[key].append(word)
    return list(result.values())
