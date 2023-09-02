# PROBLEM STATEMENT

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

# EXAMPLE

    Input: trips = [[2,1,5],[3,3,7]], capacity = 4
    Output: false

# APPROACH

If you draw all the points on a number line, you will see that this is a general intervals-based problem.

It is given that the car will move from left to right and pick passengers. It is quite obvious that it will pick those passengers first which have a smaller "from" value. In other words, we have to first sort the list by the "start" value of each trip so that the trips are laid out from left to right in order.

The only thing that we have to do extra here is to know when the passengers will be dropped off and so when our capacity will again increase by the number of passengers we dropped off.

For that, we have to check when current trip has begun so that we can drop off all the passengers for which their trips have already ended. This can be done by ordering all the trips our car has covered by their end values from least to maximum. So that, at any time, we can check whether there are trips that have already ended by the time we reach a certain trip.

We can use a MinHeap for that which will take care of maintaing the order.