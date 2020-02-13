def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    #walk through list
    #find a random index faster that one to swap current index value with
    for i in range(0, len(the_list)-1):
        random_index = get_random(0, len(the_list) -1 )
        if random_index != i:
            first_val = the_list[i] 
            second_val = the_list[random_index]
            the_list[random_index] = first_val
            the_list[i] = second_val
            
    return the_list