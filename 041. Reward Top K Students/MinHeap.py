from heapq import heappop, heappush
def topStudents(positive_feedback, negative_feedback, report, student_id, k: int):
        
        # Convert positive and negative feedback lists into sets for quick lookup
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        
        # Number of students
        n = len(student_id)
        
        # Since we want the top k students
        # We want to discard all the students with less points
        # So, let's use a minHeap
        minHeap = []
        
        # Go over each student
        for i in range(n):
        
            # Id of current student
            studentId = student_id[i]
            
            # Get the report
            studentReport = report[i]
            
            # Points of current student
            studentPoints = 0
            
            # Convert the report into a list of words
            # And then loop over each word
            for word in studentReport.split(" "):
                
                # If this word is present in positive_feedback, increase points by 3
                if word in positive_feedback: studentPoints += 3
                
                # If this word is present in negative_feedback, decrease points by 1
                elif word in negative_feedback: studentPoints -= 1
                    
            # Finally, push the student points and id in the minHeap
            # If the points are same, give priority to the one with smaller studentId
            # So, that's why we are pushing a triplet in a heap where the "second" value is used as tie breaker
            # If "studentsPoints" are same for two triplets, the heap will then check the studentId
            # We are doing "-studentId" because it is a minHeap. 
            # So, we want the student with greater ID to sit above student with a smaller ID
            heappush(minHeap, [studentPoints, -studentId, studentId])
            
            # If heap size exceeds k, pop from top
            if len(minHeap) > k: heappop(minHeap)
                
                
        # Fill the output list
        # Since it is a minHeap, it will have the "k" students ordered based on points from minimum to maximum
        # So, we will start filling the output list in reverse order
        # So that at the end, output list has "k" students ordered based on points from maximum to minimum
        # In this way, we will also avoid the extra step to reverse "output" once we fill it
        output = [0] * k
        i = k - 1
        while i >= 0: 
            output[i] = heappop(minHeap)[2]
            i -= 1
        
        # Return the output list
        return output


positive_feedback = ["smart","brilliant","studious"]
negative_feedback = ["not"]
report = ["this student is studious","the student is smart"]
student_id = [1,2]
k = 2

print("Output -> ", topStudents(positive_feedback, negative_feedback, report, student_id, k))