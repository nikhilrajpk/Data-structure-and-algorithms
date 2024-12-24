"""_summary_
Time complexity : O(n) for loop and join
Space complexity : O(n) s and join output.
if concatenation is done then Time will be O(n^2).
"""
def reverse(string):
    s = [''] * len(string)
    j = 0
    for i in range(len(string)-1,-1,-1):
        s[j] = string[i]
        j += 1
    return ''.join(s)

print(reverse('hai'))