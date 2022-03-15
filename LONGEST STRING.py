def LCSLength(s1, s2, l1, l2, d):

    if l1 == 0 or l2 == 0:
        return 0
    key = (l1, l2)
    if key not in d:

        if s1[l1 - 1] == s2[l2 - 1]:
            d[key] = LCSLength(s1, s2, l1 - 1, l2 - 1, d) + 1

        else:
            d[key] = max(LCSLength(s1, s2, l1, l2 - 1, d), LCSLength(s1, s2,l1 - 1, l2, d))

    return d[key]
d={}
k = LCSLength('abcade','badera',6,6, d)
print('The length of the  longest common subsequence is: ',k)
 