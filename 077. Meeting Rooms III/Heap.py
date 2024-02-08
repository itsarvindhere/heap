from heapq import heappush, heappop, heapify
def mostBooked(n: int, meetings) -> int:
        
        # Sort the meetings by the time they "start"
        # Convert it to a minHeap
        heapify(meetings)
        
        # A Min Heap to keep track of the unused rooms
        # We are using a minHeap because from all the unused rooms, 
        # we will always pick the one with lowest number
        # Initially, all rooms from 0 to n - 1 are unused
        unusedRooms = []
        
        # A list to keep track of the rooms and the number of meetings each room held
        meetingCount = [0] * n
        
        for i in range(n): 
            heappush(unusedRooms, i)
            meetingCount[i] = 0
            
        # A Min Heap to keep track of the rooms currently in use
        # WE will use a minHeap for those so that the used rooms are ordered
        # Based on when they will become unused again
        usedRooms = []
        
        # To keep track of the time
        # Initialize it with the time at which the very first meeting starts (the one with the smallest "start" value)
        time = meetings[0][0]
        
        # Go over each meeting from left to right
        while meetings:
            
            # Update the time accordingly
            time = max(time, meetings[0][0])
            
            # If any used rooms are now free, push them back to the unusedRooms minHeap
            while usedRooms and usedRooms[0][0] <= time: heappush(unusedRooms, heappop(usedRooms)[1])
            
            # If we have unused rooms, choose the one with the smallest number
            if unusedRooms:
                
                # Room Number
                roomNumber = heappop(unusedRooms)
                
                # Update the meeting count for this room
                meetingCount[roomNumber] += 1
                
                # When will the current room be free again?
                # That would be current time + duration of the meeting
                start, end = heappop(meetings)
                duration = end - start
                
                # Push the data to usedRooms
                heappush(usedRooms, [time + duration, roomNumber])
            
            # If we do not have any unused room
            # Update the time at which at least one room will be free
            # That is, the free time for the room at the top of "usedRooms" minHeap
            else: time = usedRooms[0][0]
                
        # What is the max count of meetings in a room
        maxCount = max(meetingCount)
        
        # The room number to return
        roomNumber = float("inf")

        for i in range(n):
            if meetingCount[i] == maxCount and i < roomNumber: roomNumber = i
        
        # Return the room number
        return roomNumber

n = 2
meetings = [[0,10],[1,5],[2,7],[3,4]]

print("Output ->", mostBooked(n,meetings))