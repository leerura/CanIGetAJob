import sys

input = sys.stdin.readline

def solve():

    accidents = [] #시간 타입 양
    
    for line in sys.stdin:
        data = line.strip()
        if not data:
            continue
        kind = data.split()

        accidents.append((int(kind[1]), kind[0], 0.0 if kind[0] == "Query" else float(kind[2])))
    accidents.sort()
                
    eaten_foods = [] #food_time, food_type, food_ammount

    for time, type, ammount in accidents:
        if(type == "Query"):
            dist = 0
            for food_time, food_type, food_ammount in eaten_foods:
                dt = time-food_time
                if(food_type=="Chocolate"):
                    dist += 8*food_ammount-dt/12 if(8*food_ammount-dt/12>1e-9) else 0
                    
                else:
                    dist += 2*food_ammount-(dt**2)/79 if(2*food_ammount-(dt**2)/79>1e-9) else 0
            
            print(f"{time} {max(1.0, dist):.1f}")
            
        else:
            eaten_foods.append((time,type,ammount))
                                
if __name__ == "__main__":
    solve()
