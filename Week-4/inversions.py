def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    avg = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, avg)
    number_of_inversions += get_number_of_inversions(a, avg, right)
    
    L, R = a[left: avg], a[avg: right+1]
    i, j, k = 0, 0, left
    n1, n2 = avg - left, right - avg
    while i < n1 and j < n2:
        if L[i] <= R[i]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j, number_of_inversions = j+1, number_of_inversions+1
        k += 1
    while i < n1:
        a[k] = L[i]
        i, k = i+1, k+1
    while j < n2:
        a[k] = R[j]
        j, k = j+1, k+1
    return number_of_inversions

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()][:n]
    print(get_number_of_inversions(a, 0, len(a)))