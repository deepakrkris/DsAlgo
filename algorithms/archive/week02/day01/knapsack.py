def find_knapsack_memoiz(capacity, weights, values):
    table = [[-1] * (capacity + 1) for i in range(len(weights))]

    def value_by_weight(index, current_capacity, current_value) :
        if index == len(weights) :
            return current_value

        if current_capacity >= capacity :
            return current_value

        if table[index][current_capacity] == -1 :
            added_current_value = -1
            if (weights[index] + current_capacity) <= capacity :
                added_current_value = value_by_weight(index + 1,
                    weights[index] + current_capacity,
                    current_value + values[index])

            table[index][current_capacity] = max(added_current_value , value_by_weight(index + 1, current_capacity, current_value))

        return table[index][current_capacity]

    return value_by_weight(0, 0, 0)


def find_max_knapsack_profit(capacity, weights, values):
 
    def value_by_weight(index, current_capacity, current_value) :
        if index == len(weights) :
            return current_value

        if current_capacity >= capacity :
            return current_value

        added_current_value = -1
        if (weights[index] + current_capacity) <= capacity :
            added_current_value = value_by_weight(index + 1,
                    weights[index] + current_capacity,
                    current_value + values[index])

        return max(added_current_value ,
            value_by_weight(index + 1, current_capacity, current_value))

    return value_by_weight(0, 0, 0)


"""
   5 , 3 , 10
   6 , 3 , 8
"""
def find_knapsack_profit_dynamic(capacity, weights, values):

    profits = [0 for i in range(capacity + 1)]
    #
    #  0 . 1 . 2 . 3 . 4 . 5 . 6 . 7 . 8 . 9 . 10
    #  0 .                 6   6 . 6 . 6 . 6 . 6
    #
    for knapsack_index in range(len(weights)) :
        for c in range(capacity, -1, -1) :
            if weights[knapsack_index] <= c :
                profits[c] = max(profits[c - weights[knapsack_index]] + values[knapsack_index] , profits[c])

    return profits[capacity]

print(find_knapsack_profit_dynamic(6 , [1,2,3,5] , [1,5,4,8]))
print(find_knapsack_memoiz(6 , [1,2,3,5] , [1,5,4,8]))
