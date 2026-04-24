def max_subarray_sum(arr):
    """
    Returns the maximum sum of any contiguous subarray using Kadane's algorithm.
    
    Args:
        arr (list): List of integers
    
    Returns:
        int: Maximum subarray sum
    """
    if not arr:
        return 0
    
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

def main():
    """
    Main function to run the app.
    Takes input from user and computes maximum subarray sum.
    """
    print("Maximum Subarray Sum Calculator")
    print("Enter integers separated by spaces (e.g., -2 1 -3 4 -1 2 1 -5 4):")
    
    try:
        # Read input and convert to list of integers
        input_str = input().strip()
        arr = [int(x) for x in input_str.split()]
        
        if not arr:
            print("Error: No integers provided.")
            return
        
        result = max_subarray_sum(arr)
        print(f"Array: {arr}")
        print(f"Maximum subarray sum: {result}")
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()