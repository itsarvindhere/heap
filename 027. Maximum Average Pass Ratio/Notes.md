# PROBLEM STATEMENT

There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

# EXAMPLE

    Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
    Output: 0.78333
    
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

# APPROACH

The main thing to understand is how we are going to assign a student to any class.

See, we want to "MAXIMIZE" the average pass ratio. So, it makes sense that when we assign a student to any class, we are doing it such that the change in the pass ratio is maximum for that particular class after we assign a student to it. 

To understand it better, take an example.

	classes = [[1,2],[3,5],[2,2]], extraStudents = 2
	
	Let's say we want to assign a student to any class.
	
	We have three options to choose from.
	
	For class 0, its old pass ratio is 1/2 => 0.5
    If we assign one student to it, is new pass ratio will be 2/3 => 0.66666
        
    For class 1, its old pass ratio is 3/5 => 0.6
    If we assign one student to it, is new pass ratio will be 4/6 => 0.66666
        
    For class 2, its old pass ratio is 2/2 => 1
    If we assign one student to it, is new pass ratio will be 3/3 => 1
	
	So, what can we observe?
	
	We can see that assigning students to class 2 is of no use because its pass ratio will always remain "1"
	So, for class 2, the increase in pass ratio will be 0.
	
	As for class 0 and class 1, 
	
	we see that assigning a student to class 0 will increase the pass ratio
	from 0.5 to 0.66666 => An increase of 0.16666
	
	And, assigning a student to class 1 will increase the pass ratio
	from 0.6 to 0.66666 => An increase of 0.06666
	
	So, we can conclude that we if have to assign a student to any class such that 
	the average pass ratio is maximized, we have to assign that student to class 0
	since for that class, the increase in pass ratio is the maximum among all the classes.
	
And that's the main idea behind choosing a class for a student.

We want to keep track of what is the increase in the pass ratio if we assign a student to any class.
And whatever class has the highest increase will be the one which we will choose and add the student to it.

And since we want this data to be ordered all the time as we add students to classes, we will use a maxHeap here which will order the classes by their increase in the pass ratio upon addition of a student.