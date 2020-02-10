def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list

    #my_list     = [3, 4, 6, 10, 11, 15]
    #alices_list = [1, 5, 8, 12, 14, 19]
    
    #start at 0 index in each list, add pointers to vals
    #compare pointer vals
    #smaller val gets appended to merged list, pointer to index gets incremented by 1
    #compare pointer vals again
    #if pointer of one list reaches end, append rest of other list
    
    if my_list == [] and alices_list == []:
        return []
    elif my_list == []:
        return alices_list
    elif alices_list == []:
        return my_list
        
    merged_list = []
    ml_index_pointer = 0
    al_index_pointer = 0
    
    while len(merged_list) < (len(my_list) + len(alices_list)):
        #if we've reached the end of my list
        if ml_index_pointer == len(my_list) :
            merged_list.extend(alices_list[al_index_pointer:])
        #if we've reached the end of alices list    
        elif al_index_pointer == len(alices_list):
            merged_list.extend(my_list[ml_index_pointer:])
        
        elif my_list[ml_index_pointer] <= alices_list[al_index_pointer]:
            merged_list.append(my_list[ml_index_pointer])
            ml_index_pointer += 1
            
        elif my_list[ml_index_pointer] > alices_list[al_index_pointer]:
            merged_list.append(alices_list[al_index_pointer])
            al_index_pointer += 1
        # print(merged_list)
    
    return merged_list