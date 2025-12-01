def parse(filePath):
    weights = []
    
    with open(filePath) as f:
        lines = f.readlines() 
        print(part_two(lines))
        
        for line in lines: 
            weight = int(line[1:])
            
            if line[0] == "R": 
                weights.append(weight)
            else: 
                weights.append(-1 * weight)
                
    return weights
    
def part_two(lines: list[str], start: int = 50, period: int = 100):
    cursor = start
    direction = "R"
    hits = 0
    for line in lines:
        letter = line[0]
        number = int(line[1:])

        if letter != direction:
            cursor = (period - cursor) % period
            direction = letter

        cursor += number

        hits += cursor // period
        cursor = cursor % period

    return hits
    
def solve(weights): 
    part1    = 0 
    part2    = 0
    position = 50
    
    for weight in weights: 
        degree    = abs(weight) + position
        position  = (position + weight) % 100
      
        if degree > 99: 
            part2 += degree // 100
                           
        if position == 0: 
            part1 += 1 

    print(part1)
    print(part2)
    return
    
def main(): 
    filePath = "C:/Projects/AOC/day1/in/input.txt"
    weights  = parse(filePath)
    
    solve(weights)
   
main()

D3videNC0nquer24A
