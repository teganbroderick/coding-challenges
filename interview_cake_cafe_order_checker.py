def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    if take_out_orders == [] and dine_in_orders == []:
        merged_orders == []
    elif take_out_orders == []:
        merged_orders = dine_in_orders
    elif dine_in_orders == []:
        merged_orders = take_out_orders
    
    #merge takeout orders and dine in orders, sort
    take_out_orders.extend(dine_in_orders) #O(n)
    merged_orders = take_out_orders
    merged_orders.sort() #O(n log n)
    
    #compare sorted merged list with served orders, see if theyre the same
    return merged_orders == served_orders #O(n)
