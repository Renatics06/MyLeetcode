def stringMatching(words):
    words.sort(key=len)
    result = []
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if words[i] in words[j]:
                result.append(words[i])
                break
    return result

print(stringMatching(["mass", "as", "hero", "superhero"]))