def solution(blocks):
    n = len(blocks)

    #array to store max distance
    max_distance = [0] * n

    #max distance when frogs jump to the right
    for i in range(1, n):
        if blocks[i] >= blocks[i - 1]:
            max_distance[i] = max_distance[i-1]+1

    #max distance when frogs jump to the left
    for i in range(n - 2, -1, -1):
        if blocks[i] >= blocks[i + 1]:
            max_distance[i] = max(max_distance[i], max_distance[i + 1]+1)

    #max distance in the max distance array
    return max(max_distance)


#test case
blocks1 = [2,6,8,5]
print(solution(blocks1)) #2

blocks2 = [1,5,5,2,6]
print(solution(blocks2)) #3

blocks3 = [1,1]
print(solution(blocks3)) #2
