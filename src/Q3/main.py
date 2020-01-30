import sys
from cache import Cache
from math import sin, cos, sqrt, atan2, radians
import geopy.distance

def main():

    cache_list = []
    print("Input your coordinates:")
    print("Longitude:")
    client_long = sys.stdin.readline().strip()
    print("Latitude:")
    client_lat =  sys.stdin.readline().strip()
    print("Please type 'create' to create cache: ")
    command = sys.stdin.readline().strip()
    while command == "create":
        print("Please input the name and coordinates of the Cache you would like to create")
        print("Name:")
        name = sys.stdin.readline().strip()
        print("Longitude:")
        longitude = sys.stdin.readline().strip()
        print("Latitude:")
        lat =  sys.stdin.readline().strip()
        cache = Cache(name,(lat,longitude))
        cache_list.append(cache)
        print("Please type 'select' to select cache or type 'create: ")
        command = sys.stdin.readline().strip()
    
    while command== 'select':
        
        print("Please input the name of the cache you want to select\n(if left blank the closest cache will be selected based on coordinates)")
        name = sys.stdin.readline().strip()
        c = None
        shortest_dist = 9999999999999.0
        for cache in cache_list:
            dist=geopy.distance.distance((int(client_lat),int(client_long)), (int(cache.coord[0]),int(cache.coord[1]))).km
            print(dist)
            if cache.name==name or dist<shortest_dist:
                c=cache
                shortest_dist = dist
            elif dist>shortest_dist:
                pass
                
            else:
                print("Error")
                return
        print("Selected "+c.name)
        print("Type command 'print', 'add', 'empty', 'remove' ")
        com = sys.stdin.readline().strip()
        
        
        if com=="print":
            print(c.print())
        elif com=="add":
            print("Please input value to add:")
            value = sys.stdin.readline().strip()
            c.add(value)
        elif com=="empty":
            print(c.empty())
        elif com =="remove":
            c.remove()

      
        
        
        print("type 'select' or 'quit':")
        commmand = sys.stdin.readline().strip()
    if command =="quit":
        return
        

    
def distance(lat1,lon1,lat2,lon2):
    R = 6373.0


    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance



if __name__ == '__main__':
    main()