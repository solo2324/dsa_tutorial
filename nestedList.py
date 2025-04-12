if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    lowest=records[0][1]
    
    for name, score in records:
        if score<lowest:
            lowest=score
       
    ans = float("inf")
    for name, score in records:
        if score > lowest and score < ans:
            ans = score
    res = []   
    for name, score in records:
        if score == ans:
            res.append(name)
            
            
    res = sorted(res)
    for i in res:
        print(i)
    
        
    
