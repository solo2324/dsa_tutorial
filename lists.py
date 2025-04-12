if __name__ == '__main__':
    N = int(input())
    List = []
    for _ in range(N):
        op = (input().split())
        command = op[0]
        if command == "print":
            print(List)
        elif command == "sort":
            List.sort()
        elif command== "insert":
            i=int(op[1])
            j=int(op[2])
            List.insert(i,j)
        elif command=="remove":
            i=int(op[1])
            List.remove(i)
        elif command=="append":
            i=int(op[1])
            List.append(i)
        elif command=="pop":
            List.pop()
        elif command=="reverse":
            List.reverse()
    
         
        
