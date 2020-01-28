def max_cake_haul(cake_tuples, capacity):
    """Return the maximum monetary value of cakes that you can hold with capacity of your bag.
    cake_tuples is a list of tuples, index 0 is the weight, index 1 is the monetary value"""


    #list to hold max values at each capacity up to and including the bag's max capacity
    max_values_at_capacities = [0] * (weight_capacity + 1)

    #go through each capacity value
    for current_capacity in range(0, (capacity + 1)):

        #max monetary value for current capacity so far
        current_max_value = 0

        #iterate through cake tuples list
        for cake_weight, cake_value in cake_tuples:
            #if weight is 0 and cake value is not 0, result is infinite value
            if cake_weight == 0 and cake_value != 0:
                return float("inf")

            #if cake_weight is less than or equal to the current capacity, 
            #its possible that taking the cake would get a better value
            if cake_weight <= current_capacity:

                #should we take the cake or not?

                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                max_value_using_cake = (cake_value + max_values_at_capacities[current_capacity - cake_weight])

                # Is it worth taking the cake? how does the value using the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake, current_max_value)

            max_values_at_capacities[current_capacity] = current_max_value
    
    #return value from max vals at capacities list for input capacity
    return max_values_at_capacities[capacity]



