if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    nums=sorted(list(set(arr)), reverse=True)
    print(nums[1])
