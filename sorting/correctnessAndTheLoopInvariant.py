# In the previous challenge, you wrote code to perform an Insertion Sort on an unsorted array. But how would you prove that the code is correct? I.e. how do you show that for any input your code will provide the right output?
# Loop Invariant
# In computer science, you could prove it formally with a loop invariant, where you state that a desired property is maintained in your loop. Such a proof is broken down into the following parts:
# - Initialization: It is true ( in a limited sense) before the loop runs.
# - Maintenance: If it's true before an iteration of a loop, it remains true before the next iteration.
# - Termination: It will terminate in a useful way once it is finished.

# Insertion Sort's Invariant
# Say, you have some InsertionSort code, where the outer loop goes through the whole array:
#     for(int i=1; i < A.length; i++){
#     // insertion sort code
# You could then state the following loop invariant:
#     At the start of every iteration of the outer loop(indexed with), the subarray until  consists of the original elements that were there, but in sorted order.
# To prove Insertion Sort is correct, you will then demonstrate it for the three stages:
# - Initialization - The subarray starts with the first element of the array, and it is (obviously) sorted to begin with.
# - Maintenance - Each iteration of the loop expands the subarray, but keeps the sorted property. An element  gets inserted into the array only when it is greater than the element to its    left. Since the elements to its left have already been sorted, it means is greater than all the elements to its left, so the array remains sorted. (In Insertion Sort 2 we saw this by printing the array each time an element was properly inserted.)
# - Termination - The code will terminate after  has reached the last element in the array, which means the sorted subarray has expanded to encompass the entire array. The array is now fully sorted.

# You can often use a similar process to demonstrate the correctness of many algorithms. You can see these notes for more information(http://www.cs.uofs.edu/~mccloske/courses/cmps144/invariants_lec.html).

# Challenge
# In the InsertionSort code below, there is an error. Can you fix it? Print the array only once, when it is fully sorted.

# Input Format
# There will be two lines of input:
# - s = the size of the array
# - arr = the list of numbers that makes up the array

# Constraints
# 1 ≤ s ≤ 1000
# - 1500 ≤ V ≤ 1500, V ∈ arr

# Output Format
# Output the numbers in order, space-separated on one line.

# Sample Input
#     6
#     7 4 3 5 6 2
# Sample Output
#     2 3 4 5 6 7


def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        # to fix the loop change j > 0 to j >= 0
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
    return l


m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str, ar)))
