#!/usr/bin/python3

def main():

    word = input("Write a word here: ")
    for num_chars in range(len(word)):
        for i in range(len(word) - num_chars):
            substring = ""
            for chars in range(i, i + num_chars + 1):
                substring += word[chars]
            print(substring)


if __name__ == "__main__":
    main()
    
#another_algorithm
a = input()
cnt = 1
for i in range(len(a)):
    for j in range(len(a)):
        if j + cnt <= len(a):
            b = a[j:j+cnt]
            print(b)
    cnt = cnt + 1
