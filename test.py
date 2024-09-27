def longest_peak_interval(heights):
    n = len(heights)
    longest_length = 0

    # Iterate through the heights to find peaks
    for i in range(1, n - 1):
        # Check if the current element is a peak
        if heights[i - 1] < heights[i] > heights[i + 1]:
            # At this point, we have found a peak at heights[i]
            left = i - 1
            right = i + 1
            
            # Count the length of the increasing sequence to the left
            while left > 0 and heights[left - 1] < heights[left]:
                left -= 1
            
            # Count the length of the decreasing sequence to the right
            while right < n - 1 and heights[right] > heights[right + 1]:
                right += 1
            
            # Calculate the length of the interval
            length = right - left + 1
            longest_length = max(longest_length, length)
    
    return longest_length

# Read input
heights = 2, 1, 4, 7, 3, 2, 5, 1

# Calculate and print the longest peak interval
print(longest_peak_interval(heights))