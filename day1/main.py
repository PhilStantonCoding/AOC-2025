def parse(filePath):
    weights = []
    
    with open(filePath) as f:
        lines = f.readlines() 
       
        for line in lines: 
            weight = int(line[1:])
            
            if line[0] == "R": 
                weights.append(weight)
            else: 
                weights.append(-1 * weight)
                
    return weights
        
def solve(weights): 
    part1     = 0 
    part2     = 0
    position  = 50

    for weight in weights: 
        degree   = position + weight; 
        position = (position + weight) % 100

        if degree <= 0: 
            part2 += (degree // 100) * -1
        elif degree > 99:
            part2 += (degree // 100)

        if position == 0: 
            part1 += 1

    print(part1)
    print(part2)
    return
    
def main(): 
    filePath = "in/input.txt"
    weights  = parse(filePath)
    
    solve(weights)
   
main()

