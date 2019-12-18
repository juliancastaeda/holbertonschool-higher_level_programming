#!/usr/bin/python3
def max_integer(my_list=[]):
    num_larger = my_list[0]
    if (my_list == ""):
        return (None)
    for i in range(0, len(my_list)):
        if num_larger < my_list[i]:
            num_larger = my_list[i]
            return (num_larger)
            
    


    
