def optimal_points(segments, n):
    segments.sort(key = lambda x: x[1])
    index = 0
    coordinates = []
    while index < n:
        curr = segments[index]
        while index < n-1 and curr[1]>=segments[index+1][0]:
            index += 1
        coordinates.append(curr[1])
        index += 1
    print(len(coordinates))
    print(' '.join([str(i) for i in coordinates]))

if __name__ == '__main__':
    n = int(input())
    segments = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        segments.append((x, y))
    optimal_points(segments, n)