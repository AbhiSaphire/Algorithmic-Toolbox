"""
# Time Complexity : O(nlogn)
# Auxilary Space : O(1)/Constant
"""
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    a.sort()
    count = j = 0
    for i in range(1, len(a)):
        if a[i] != a[i-1]:
            if count < i-j:
                count = i-j
            j = i
    if count > len(a)/2:
        return count
    return -1

"""
# Description : SPACE TIME TRADEOFF using dictionary
# Time Complexity : O(n)
# Auxilary Space : O(n)
"""
def get_majority(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    lookup = {}
    for i in a:
        if i not in lookup:
            lookup[i] = 1
        else:
            lookup[i] += 1
    maximum = max(lookup.values())
    if maximum > len(a)/2:
        return maximum
    return -1

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()][:n]
    if get_majority(a, 0, n, 0) != -1:
        print(1)
    else:
        print(0)
