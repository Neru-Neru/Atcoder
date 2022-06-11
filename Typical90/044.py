n, q = map(int, input().split())
a = list(map(int, input().split()))
shift_cnt = 0
for _ in range(q):
    ct, cx, cy = map(int, input().split())
    x = cx - 1
    y = cy - 1
    if ct == 1:
        x = (x - shift_cnt) % n
        y = (y - shift_cnt) % n
        tmp = a[x]
        a[x] = a[y]
        a[y] = tmp
    elif ct == 2:
        shift_cnt += 1
    else:
        print(a[(x - shift_cnt) % n])
