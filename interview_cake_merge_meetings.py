def merge_ranges(meetings):

    # Merge meeting ranges
    #In [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    #out [(0, 1), (3, 8), (9, 12)]
    
    #sort in order of start time (tuple[0])
    meetings.sort()
    
    current_meeting = meetings.pop(0)
    
    merged_meetings = []
    
    for index, meeting in enumerate(meetings):
        #if we make a new meeting
        if meeting[0] <= current_meeting[1]:
            new_meeting = (current_meeting[0], meeting[1])
            merged_meetings.append(new_meeting)
            current_meeting = merged_meetings[-1]
            
        #if we don't make a new meeting
        else:
            merged_meetings.append(current_meeting)
            

    return merged_meetings