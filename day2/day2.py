#!/usr/bin/env python3

"""
I Acknowledge this code is shit. However, it works and I'm tired
"""
import numpy

def parse(filePath): 
    with open(filePath, "r") as f: 
        ranges = f.readline().split(",")
        return list(map(lambda r:(int(r.split("-")[0]), int(r.split("-")[1])), ranges))
  
def part1(ranges): 
    count = 0

    for rng in ranges: 
        for i in range(rng[0], rng[1]+1): 
            num = str(i)
            
            if len(num) % 2 == 0 and num[0:len(num)//2] == num[len(num)//2:len(num)]: 
                count += i
    
    print(f"part 1: {count}") 
    return

def part2(ranges): 
    count = 0
    
    for rng in ranges: 
        for i in range(rng[0], rng[1]+1): 
            num = str(i)

            for k in range(0, len(num)//2):  
                if len(num) % (k+1) == 0: 
                    chunks = list(map(''.join, numpy.array_split(list(num), k+1)))

                    if (k == 0 and len(set(list(num))) == 1) or (k > 0 and len(set(chunks)) == 1):
                        count += i  
                        break
                    
    print(f"part 2: {count}")    
    return

def main():
    filePath = "in/input.txt"
    ranges   = parse(filePath)
    
    part1(ranges) 
    part2(ranges)
    return

if __name__ == "__main__":
    main()
