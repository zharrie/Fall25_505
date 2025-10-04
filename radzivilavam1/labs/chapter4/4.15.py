highway_number = int(input())

if (1 <= highway_number < 1000) and (highway_number % 100 != 0):
        
    is_even = (highway_number % 2 == 0)

    direction = ""
    if is_even == True:
        direction = "going east/west."
    else:
        direction = "going north/south."


    primary_highway = highway_number % 100

    aux_prim_ind = ""
    if 100 <= highway_number < 1000:
        aux_prim_ind = f"I-{highway_number} is auxiliary, serving I-{primary_highway}, {direction}"
    else:
        aux_prim_ind = f"I-{highway_number} is primary, {direction}"

    print(aux_prim_ind)
    
    
else:
    print(f"{highway_number} is not a valid interstate highway number.")