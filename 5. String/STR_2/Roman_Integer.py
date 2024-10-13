s = "III"
# tput: 1994


def romanToInt(s):
    mpp = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    ans = 0
    i = 0
    n = len(s)

    while (i < n):
        if (s[i] in mpp):
            if (i < n - 1 and mpp[s[i]] < mpp[s[i + 1]]):
                ans += (mpp[s[i + 1]] - mpp[s[i]])
                i += 2
            else:
                ans += mpp[s[i]]

                i += 1

    return ans


print(romanToInt(s))
