# ====================================
# LeetCode #1475: Final Prices With a Special Discount in a Shop
# Difficulty: Easy
# Topic: Array, Iteration
# ====================================

def finalPrices(self, prices):
    """
    Problem Approach:
    - For each price, look at all prices after it
    - Apply discount if we find a lower/equal price
    - Discount = first lower/equal price found
    """
    n = len(prices)
    answer = []  # Store results after discount
    
    # Outer loop: Process each price
    for i in range(n):
        current_price = prices[i]
        discount = 0  # Default: no discount
        
        # Inner loop: Look for discount in remaining prices
        for j in range(i + 1, n):
            if prices[j] <= current_price:
                discount = prices[j]  # Found valid discount
                break  # Stop searching - we want first valid discount
        
        # Calculate and store final price
        final_price = current_price - discount
        answer.append(final_price)
    
    return answer

# ====================================
# TEST CASES
# ====================================
# Example 1: prices = [8,4,6,2,3] → [4,2,4,2,3]
# Example 2: prices = [1,2,3,4,5] → [1,2,3,4,5]
# Example 3: prices = [10,1,1,6] → [9,0,1,6]