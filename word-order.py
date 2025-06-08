if __name__ == '__main__':
    n = int(input())
    word_dict = {}
    
    for _ in range(n):
        word = input()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    
    print(len(word_dict))
    print(*word_dict.values())
