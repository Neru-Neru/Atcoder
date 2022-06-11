def main():
    li = []
    s = input()
    for i in range(len(s)):
        li.append(s[i:]+s[:i])
    li.sort()
    print(li[0])
    print(li[-1])
if __name__ == '__main__':
    main()