def main():
    n = int(input())
    a=[]
    b=[]
    total = 0
    for _ in range(n):
        aa, bb = map(int, input().split())
        total += aa*bb
        a.append(aa)
        b.append(bb)
    half = total / 2
    ans = 0.0
    time = 0.0
    for i in range(n):
        print(ans)
        if time + a[i] * b[i] > half:
            ans += (half - time) / b[i]
            break
        else:
            ans += a[i]
            time += a[i] * b[i]
    print(ans)

if __name__ == "__main__":
    main()