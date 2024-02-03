# PROBLEM STATEMENT

A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

# EXAMPLE

    Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]

    Output: 2

Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.

# APPROACH

Since we can travel 1 mile using 1 litre of fuel, it basically means to reach "target", we need to have at least "target" litres of fuel.

Also, we want to avoid stopping at a gas station as much as we can.

The idea is that we will drive the car to the rightmost fuel station with the available fuel. And once we reach that fuel station, we understand from here, there is no way to reach the next fuel station or even the target.

And so, we should've refueled at some previous (or even the current) fuel station so that we could've covered even more distance than what we covered so far.

So now, from all the fuel stations we have covered so far, we will choose the one that has the most amount of fuel and there, we will refuel our vehicle. And now that we got more fuel, it means we might be able to reach at least the next fuel station or even the target. If we cannot, we will again do the same process till we finally reach the target. But, if there are no more fuel stations left to stop at, and we still haven't reached the target, that means it is impossible to reach the target.

And so, based on this approach, we will use a MAX HEAP to keep track of all the gas stations that we have covered so far and then when the time comes, we will pick the gas station from the top since that one has the maximum fuel.

