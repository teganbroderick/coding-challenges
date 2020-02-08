def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    movie_length_set = set(movie_lengths) #O(n)
    
    for length in movie_lengths:
        if (flight_length - length) in movie_length_set:
            if flight_length - length != flight_length // 2:
                return True
            elif flight_length - length == flight_length // 2 and movie_lengths.count(length) >=2:
                return True

    return False