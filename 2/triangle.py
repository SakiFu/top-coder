# Make triangle with 3 sticks. The length of stick[i] is a[i]. The perimeter has to be as long as possible.


def triangle(n, a):
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                length = a[i] + a[j] + a[k]
                ma = max(a[i], a[j], a[k])
                rest = length - ma

                if ma < rest:
                    ans = max(ans, length)
    return ans