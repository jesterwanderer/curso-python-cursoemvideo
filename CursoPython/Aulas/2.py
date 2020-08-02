def lastLetters(word):
    array = []
    for i in word[-2:]:
          array.append(i)
    return ' '.join(array[::-1])


print(lastLetters('APPLE')) # E L