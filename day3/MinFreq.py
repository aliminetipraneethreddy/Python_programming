def Occurence(s1):
    visited = []
    result = []   # to store counts as integers
    result1 = []  # to store characters

    for char in s1:
        if char not in visited:
            count = 0
            for char1 in s1:
                if char == char1:
                    count += 1
            result.append(count)
            result1.append(char)
            visited.append(char)
    
    # Find the minimum count
    min_count = min(result)
    index = result.index(min_count)
    print(f"{result1[index]}{min_count}")

s1 = "SmtSriSanthoshiPraneethReddy"
Occurence(s1)
