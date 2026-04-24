# Maximum Subarray Sum Calculator

A web application that solves the classic maximum subarray sum problem using Kadane's algorithm.

## Problem Description

The maximum subarray sum problem asks for the maximum sum of any contiguous subarray within a one-dimensional array of numbers. For example:
- Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
- Output: `6` (from the subarray `[4, -1, 2, 1]`)

## Features

- Web-based interface for easy use
- Supports input via spaces, commas, or newlines
- Real-time calculation using Kadane's algorithm (O(n) time complexity)
- Error handling for invalid input
- Responsive design

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/max-subarray-sum.git
   cd max-subarray-sum
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`

3. Enter integers in the text area and click "Calculate"

## Algorithm

This implementation uses Kadane's algorithm:
- Time Complexity: O(n)
- Space Complexity: O(1)
- Handles negative numbers and empty arrays correctly

## Testing

The application includes comprehensive error handling and input validation.

## Requirements

- Python 3.7+
- Flask 3.0.0

## License

MIT License