"""_summary_
Time complexity : O(n). while loop is continuesly traversing through the string. and also in join.
                if we are concatenating the string then for one concatenation O(m+n).
                when it is inside the loop it will become (n^2).
Space complexity : O(n) in worst case. it is basically O(2n) so it is rounded to n.
                for best case it will be O(2).
"""
def count_of_alphabet(string):
    count = 1
    s = []
    prev = string[0]
    i = 1
    while i <= len(string):
        while i < len(string) and string[i] == prev:
            count += 1
            i += 1
        s.append(str(count))
        s.append(prev)
        if i < len(string) : prev = string[i]
        count = 1
        i += 1
        print()
    return ''.join(s)

string = input('enter the sorted string:')
print('string : ', count_of_alphabet(string))