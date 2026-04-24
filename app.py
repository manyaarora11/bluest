from flask import Flask, render_template, request
import re

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    input_array = None
    error = None
    
    if request.method == 'POST':
        array_input = request.form.get('array', '').strip()
        
        if array_input:
            try:
                # Parse the input, allowing various separators
                # Split on commas, spaces, or newlines
                numbers = re.split(r'[,\s\n]+', array_input)
                arr = [int(num.strip()) for num in numbers if num.strip()]
                
                if not arr:
                    error = "Please enter at least one integer."
                else:
                    result = max_subarray_sum(arr)
                    input_array = arr
                    
            except ValueError:
                error = "Please enter valid integers separated by spaces, commas, or newlines."
        else:
            error = "Please enter an array of integers."
    
    return render_template('index.html', result=result, input_array=input_array, error=error)

if __name__ == '__main__':
    app.run(debug=True)