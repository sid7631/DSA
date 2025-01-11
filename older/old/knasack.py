def knap_sack(profits, profits_length, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each
    :param profits_length: The number of pieces of jewelry
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    weights_length = profits_length

    # basic checks
    if capacity <= 0 or profits_length == 0:
        return 0

    lookup_table = [0 for x in range(capacity + 1)]
    # if we have only one weight, we will take it if it is not more than the
    # capacity
    for i in range(capacity + 1):
        if weights[0] <= i:
            lookup_table[i] = profits[0]

    # process all sub-lists for all the capacities
    for i in range(1, profits_length):
        for j in reversed(range(capacity + 1)):

            profit1 = 0
            profit2 = 0

            # include the item, if it is not more than the capacity
            if weights[i] <= j:
                profit1 = profits[i] + lookup_table[j - weights[i]]
            # exclude the item
            profit2 = lookup_table[j]
            # take maximum
            lookup_table[j] = max(profit1, profit2)

    return lookup_table[capacity]


# Driver code to test the above function
if __name__ == '__main__':
    profits = [1, 6, 10, 16]  # The values of the jewelry
    weights = [1, 2, 3, 5]  # The weight of each
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 7))
    print("Total knapsack profit = ", knap_sack(profits, len(profits), weights, 6))