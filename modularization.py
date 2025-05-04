# Step 1: Define the function to evaluate how close the guess is
def evaluate_guess(guess):
    target = 9
    return guess * guess - target  # This returns f(x) = x² - 9

# Step 2: Define the function to update the guess using Newton-Raphson
def update_guess(guess):
    derivative = 2 * guess        # f'(x) = 2x
    function_value = evaluate_guess(guess)  # f(x) = x² - 9
    return guess - (function_value / derivative)

# Step 3: Main function that uses the above two to find the root
def find_root():
    guess = 1.0  # Initial guess
    tolerance = 0.0001  # How close we want to get
    while abs(evaluate_guess(guess)) > tolerance:
        guess = update_guess(guess)
    return guess

# Step 4: Output the result
root = find_root()
print("Root of x^2 - 9 is approximately:", round(root, 5))