"""
Introduction to Algorithms
An algorithm is a clear sequence of steps for accomplishing a task. Think of it as a recipe. A key aspect of an algorithm is its runtime, which is the time it takes to execute. We often measure this not in seconds, but in how the number of steps grows as the input size (N) grows.

Big O Notation: A Quick Guide
Big O notation is a way to describe how the runtime of an algorithm scales with the size of the input (N). It helps us compare algorithm efficiency by focusing on the "worst-case scenario" and the parts of the algorithm that have the most significant impact on runtime as the input gets very large.

Here are some common Big O notations, from most to least efficient:
O(1) - Constant: The runtime is always the same, regardless of the input size.
O(log N) - Logarithmic: The runtime grows very slowly. The algorithm often halves the problem with each step.
O(N) - Linear: The runtime grows directly in proportion to the input size.
O(N log N) - Log-linear: A very efficient runtime for sorting algorithms.
O(N²) - Quadratic: The runtime grows exponentially. This is common in algorithms with nested loops.
"""

"""
The Core Question: What Are Your Constraints?

The "best" algorithm depends entirely on the problem you are trying to solve. 
You choose an algorithm by asking a series of questions about your data and your goals.

1. Choosing a Searching Algorithm
This is the most straightforward choice. It comes down to one simple question:

- Is the list already sorted?
If NO, the list is unsorted:
You must use Linear Search.
Reasoning: There is no order to the data, so there's no clever way to find an element. You have no choice but to look at each item one by one until you find what you're looking for. It's like looking for a specific car in a massive, unorganized parking lot—you have to walk down every aisle.

If YES, the list is sorted:
You should use Binary Search.
Reasoning: Because the data is sorted, you can be much more intelligent in your search. By starting in the middle, you can eliminate half of the remaining data with every single comparison. This is dramatically faster than checking every element. It's like looking up a word in a dictionary—you open it to the middle, not the first page.
The Special Case: Searching Many Times What if you have an unsorted list, but you need to search for items in it repeatedly?

The Smart Strategy: Sort the list once at the beginning using an efficient sorting algorithm (like Merge Sort or Quicksort). 
Then, perform all subsequent searches using the much faster Binary Search.
Reasoning: You pay the one-time "cost" of sorting to gain the massive benefit of fast O(log N) searches every time after that. 
This is a very common and practical approach in software development.

2. Choosing a Sorting Algorithm
Choosing a sorting algorithm is more complex because there are more trade-offs to consider. Here are the key questions to ask:

Question 1: How large is the list (N)?
This is the most important factor.

If the list is SMALL (e.g., fewer than a few hundred items):
Use Insertion Sort or Selection Sort.
Reasoning: For small lists, the difference in speed between a simple O(N²) algorithm and a complex O(N log N) algorithm is negligible. Simpler algorithms are easier to write, debug, and have less overhead. Insertion Sort is often preferred because it's very fast for small lists.

If the list is LARGE (e.g., thousands or millions of items):
You MUST use an O(N log N) algorithm like Merge Sort or Quicksort.
Reasoning: For large lists, an O(N²) algorithm will be unacceptably slow. The difference between sorting a million items with Quicksort (fast) versus Selection Sort (could take hours) is enormous.

Question 2: How much memory can you use?
This helps you choose between the fast O(N log N) algorithms.
If memory is NOT a concern:
- Merge Sort is an excellent and reliable choice.
Reasoning: Merge Sort guarantees O(N log N) performance, but it requires extra memory (O(N)) to create a temporary array for merging. If you have plenty of RAM, this isn't a problem.

If memory is very LIMITED:
Quicksort is a better choice.
Reasoning: Quicksort is an "in-place" sort, meaning it uses very little extra memory (O(log N) for recursion). This makes it ideal for memory-constrained environments like embedded systems.

Question 3: Is the list already "nearly sorted"?
If YES, the list is almost in order with only a few misplaced items:
Use Insertion Sort.
Reasoning: Insertion Sort is surprisingly the champion in this specific scenario. Its performance becomes close to O(N) on nearly sorted data because it only has to do a small amount of work to shift the few out-of-place elements. An O(N log N) algorithm would still go through its entire complex process, making it slower in this case.

Question 4: Do you need a "stable" sort?
A stable sort preserves the original relative order of equal elements.
Imagine sorting a list of students by grade. 
If two students have the same grade, a stable sort ensures they remain in their original alphabetical order.

If YES, you need stability:
Use Merge Sort or Insertion Sort. Both are stable.

If NO, stability doesn't matter:
Quicksort is a great option. Quicksort is not stable, as its swapping mechanism can change the relative order of equal elements.

Summary and Decision Flowchart
Here is a quick reference table and a flowchart to guide a student's decision.

Algorithm	        Time Complexity (Avg)	Memory Usage	Stable?	        When to Use It
Linear Search	    O(N)	                O(1)	        N/A	            For unsorted lists.
Binary Search	    O(log N)	            O(1)	        N/A	            For sorted lists.
Selection Sort	    O(N²)	                O(1)	        No	            For small lists where simplicity is more important than speed.
Insertion Sort	    O(N²)	                O(1)	        Yes	            For small lists or nearly sorted lists (it's very fast in this case).
Quicksort	        O(N log N)	            O(log N)	    No	            The default choice for large lists when memory is a concern and stability is not needed.
Merge Sort	        O(N log N)	            O(N)	        Yes	            Great for large lists when you need a stable sort and memory is not an issue.

"""

# Check all algorithms visualizatio here: https://visualgo.net/en/sorting

"""
Searching Algorithms
Searching algorithms are used to find a specific item (the "key") in a list.

Linear Search: The Simple Approach
Linear search starts at the beginning of a list and checks each element one by one until the key is found or the end of the list is reached.

The Code Explained: The algorithm iterates through a list called numbers using a for loop. In each iteration, it checks if the current element (numbers[i]) is equal to the key.
"""

# O(N) - Linear Runtime
def linear_search(numbers, key):
    # Iterate through the list from the first element (index 0) to the last.
    for i in range(len(numbers)):
        # Check if the current element matches the key.
        if numbers[i] == key:
            # If a match is found, return the index.
            return i
    # If the loop finishes without finding the key, return -1.
    return -1 # not found

# Efficiency: In the worst-case scenario (the item is at the end or not in the list), this search requires N comparisons for a list of N elements. This gives it a runtime of O(N).

"""
Binary Search: The Fast Approach
If a list is sorted, binary search is a much faster method. It works by repeatedly dividing the search interval in half. It starts by checking the middle element. If that's not the key, it eliminates half of the remaining elements and repeats the process on the smaller sublist.

The Code Explained: The algorithm maintains low and high pointers to define the current search range. It calculates the mid point and compares the element at that position with the key.
"""

# O(log N) - Logarithmic Runtime
def binary_search(numbers, key):
    # Set the initial search range to the entire list.
    low = 0
    high = len(numbers) - 1

    # Continue searching as long as the range is valid.
    while high >= low:
        # Calculate the middle index.
        mid = (high + low) // 2

        # If the middle element is less than the key, search the right half.
        if numbers[mid] < key:
            low = mid + 1
        # If the middle element is greater than the key, search the left half.
        elif numbers[mid] > key:
            high = mid - 1
        # If the middle element is the key, return its index.
        else:
            return mid
            
    # If the loop finishes, the key was not found.
    return -1 # not found

# Efficiency: Because it halves the search space with each comparison, binary search is incredibly efficient. Its runtime is O(log N).
"""
Sorting Algorithms
Sorting is the process of arranging a list of elements in a specific order.

Selection Sort
Selection sort divides the list into a sorted part and an unsorted part. It repeatedly finds the smallest element in the unsorted part and swaps it with the first unsorted element.

The outer loop (i) iterates through the list, expanding the "sorted" portion. 
The inner loop (j) searches the remaining "unsorted" portion to find the index of the smallest element (index_smallest). 
After the inner loop finishes, the smallest element is swapped into its correct position.
"""

# O(N²) - Quadratic Runtime
def selection_sort(numbers):
    # The outer loop tracks the boundary between the sorted and unsorted parts.
    for i in range(len(numbers)):
        # Assume the first element of the unsorted part is the smallest.
        index_smallest = i
        # The inner loop finds the actual smallest element in the unsorted part.
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index_smallest]:
                index_smallest = j

        # Swap the found smallest element with the first element of the unsorted part.
        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp
# Efficiency: Due to the nested loops where each element is compared with every other element, selection sort has a runtime of O(N²).

"""
Insertion Sort
Insertion sort also maintains a sorted and an unsorted part. 
It takes the first element from the unsorted part and "inserts" it into the correct position within the sorted part.

The outer loop (i) picks the next element to be inserted. 
The inner while loop (j) moves through the sorted part, shifting larger elements one position to the right to make space for the element being inserted.
"""

# O(N²) - Quadratic Runtime
def insertion_sort(numbers):
    # Start from the second element, as the first is considered sorted.
    for i in range(1, len(numbers)):
        j = i
        # The while loop shifts elements in the sorted part to the right
        # until the correct spot for numbers[i] is found.
        while j > 0 and numbers[j] < numbers[j - 1]:
            # Swap the current element with the one before it.
            temp = numbers[j]
            numbers[j] = numbers[j - 1]
            numbers[j - 1] = temp
            # Move to the next position on the left.
            j = j - 1
# Efficiency: In the average and worst cases, insertion sort has a runtime of O(N²). However, for lists that are already or nearly sorted, it is much faster, with a runtime of O(N).

"""
Quicksort (Divide and Conquer)
Quicksort is a highly efficient "divide and conquer" algorithm. 
It picks an element as a pivot and partitions the array into two sub-arrays: elements smaller than the pivot and elements larger than the pivot. 
It then recursively sorts the sub-arrays.
The quicksort function is recursive. 
Its base case is when a partition has one or zero elements. 
Otherwise, it calls partition to rearrange the elements around a pivot and find the split point (j). 
Then, it calls quicksort on the low and high partitions.
The partition function uses two pointers, l and h, to scan from both ends of the list. 
It moves elements that are on the wrong side of the pivot until the pointers meet, at which point the partition is complete.
"""
# O(N log N) - Typical Runtime
# O(N²) - Worst-Case Runtime

def partition(numbers, i, k):
    # Pick the middle element as the pivot.
    midpoint = i + (k - i) // 2
    pivot = numbers[midpoint]
    
    l = i
    h = k
    
    done = False
    while not done:
        # Increment l while numbers[l] is less than the pivot.
        while numbers[l] < pivot:
            l = l + 1
        # Decrement h while the pivot is less than numbers[h].
        while pivot < numbers[h]:
            h = h - 1
        
        # If pointers cross, partitioning is done.
        if l >= h:
            done = True
        else:
            # Swap elements and move pointers.
            temp = numbers[l]
            numbers[l] = numbers[h]
            numbers[h] = temp
            l = l + 1
            h = h - 1
            
    return h # Return the split point.

def quicksort(numbers, i, k):
    # Base case: If the partition has 0 or 1 elements, it's already sorted.
    if i >= k:
        return
    
    # Partition the array and get the split point.
    j = partition(numbers, i, k)
    
    # Recursively sort the low and high partitions.
    quicksort(numbers, i, j)
    quicksort(numbers, j + 1, k)
# Efficiency: Quicksort's typical runtime is very fast at O(N log N). Its worst-case runtime is O(N²), but this rarely happens with a good pivot selection strategy.
"""
Merge Sort (Divide and Conquer)
Merge sort is another "divide and conquer" algorithm. It divides the list into two halves, recursively sorts each half, and then merges the two sorted halves back into one sorted list.
The Code Explained: The merge_sort function recursively divides the list in half until it reaches lists with a single element (the base case). Then, it calls the merge function to combine them.
The merge function takes two sorted partitions and builds a new sorted list (merged_numbers) by repeatedly comparing the first elements of each partition and adding the smaller one to the merged list.
"""

# O(N log N) - Runtime
def merge(numbers, i, j, k):
    merged_size = k - i + 1
    merged_numbers = [0] * merged_size
    merge_pos = 0
    left_pos = i
    right_pos = j + 1

    # Add the smallest element from the left or right partition to the merged list.
    while left_pos <= j and right_pos <= k:
        if numbers[left_pos] <= numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    # If any elements remain in the left partition, add them.
    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1

    # If any elements remain in the right partition, add them.
    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    # Copy the sorted merged list back to the original list.
    for merge_pos in range(merged_size):
        numbers[i + merge_pos] = merged_numbers[merge_pos]

def merge_sort(numbers, i, k):
    if i < k:
        j = (i + k) // 2  # Find the midpoint.
        
        # Recursively sort the left and right partitions.
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        
        # Merge the sorted partitions.
        merge(numbers, i, j, k)
# Efficiency: Merge sort has a consistent and efficient runtime of O(N log N) in all cases (best, average, and worst). Its main drawback is that it requires extra memory to store the merged list.


"""
In Practice: Always Use the Built-in Methods

For any scenario—a short list, a long list, inserting, or sorting—rely on Python's built-in functionalities.

For Sorting: Use my_list.sort() or sorted(my_list).
For Searching: Use the in keyword (if item in my_list:) or my_list.index(item).
For Inserting: Use my_list.insert(index, item) or my_list.append(item).

Why are the built-in methods better?
Highly Optimized: 
Python's built-in sorting method is called Timsort. 
It is an incredibly efficient, hybrid algorithm developed specifically for Python. 
It's written in C and is far faster than any sorting algorithm you could write in pure Python.
Timsort combines the best of Merge Sort and Insertion Sort. It looks for pre-sorted "runs" in the data and merges them, making it extremely fast on real-world data that is often partially sorted.
It has a worst-case performance of O(N log N) and a best-case performance of O(N), making it more efficient than a standard Quicksort or Merge Sort in many scenarios.

Reliability and Correctness: 
These methods have been tested for years by millions of users. 
They are guaranteed to be bug-free and to handle all edge cases correctly. 
When you write your own algorithm, you risk introducing subtle bugs.

Readability and Maintainability: 
Code like numbers.sort() is instantly understandable to any Python developer. 
A custom 50-line sorting function requires other developers to read, understand, and trust your implementation, which slows down collaboration.
Even for a short list, using .sort() is the correct choice. The performance difference is zero, and the code is cleaner and more standard.

So, Why Did We Learn These Algorithms?
If you should always use the built-ins, why spend time learning Selection Sort, Merge Sort, etc.? 
This is the crucial distinction between being a coder and being a computer scientist or software engineer.

You learn these algorithms for three main reasons:
To Understand the Fundamentals (The "How"):
Learning these algorithms teaches you how to think about efficiency, trade-offs (time vs. memory), and complexity (Big O notation). This knowledge is essential for making informed decisions when designing more complex systems. You understand why one approach might be slow and can identify performance bottlenecks in your own code.

For Technical Interviews (The "Gate"):
Many software engineering job interviews will explicitly ask you to write a sorting or searching algorithm on a whiteboard from scratch. They are not testing if you can write a better sort than Python's Timsort (you can't). They are testing your fundamental understanding of computer science principles.
For Specialized or Custom Problems (The "Rare Case"):
Very rarely, you may encounter a problem where the standard library functions don't quite fit. 
You might have a unique data structure that isn't a simple list, or you may need to slightly modify an algorithm's behavior in a way the built-ins don't allow. 
In these advanced and uncommon situations, knowing how to implement or adapt an algorithm is invaluable.

A Simple Rule of Thumb

When writing code for a project, a job, or any practical application: 
Always use the built-in, optimized methods provided by the language (.sort(), sorted(), in, etc.).

When studying for an exam or preparing for a technical interview: 
You must understand the underlying algorithms, know their trade-offs, and be able to write them from scratch.
"""