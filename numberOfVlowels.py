
def vowel_count(str):
    count = 0

    vowel = set("aeiouAEIOU")
    for i in str:

        if i in vowel:
            count = count + 1

    return count



str = "GeeksforGeeks"

print(vowel_count(str))
