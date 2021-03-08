def is_isogram(string):
    wordLen = len(string)

    if (wordLen == 1):
        return True

    for i in range(wordLen):
        for j in range((wordLen - 1), -1, -1):
            if ((i != j) and (string[i].lower() == string[j].lower())):
                return False
    
    return True

str1 = "Dermatoglyphics"
str2 = "aba"
str3 = "moOse"

print(is_isogram(str1))
print(is_isogram(str2))
print(is_isogram(str3))