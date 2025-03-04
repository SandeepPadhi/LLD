def dynamic_programming_recurrence_relations(problem_type):
    """
    Returns the recurrence relation for various DP problems as a string.

    Args:
        problem_type (str): The type of DP problem.

    Returns:
        The recurrence relation as a string.
    """

    if problem_type == 'lcs':
        return """
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        """

    elif problem_type == 'lcs_substring':
        return """
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = 0
        """

    elif problem_type == 'knapsack':
        return """
        if weights[i-1] <= w:
            dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
        """

    elif problem_type == 'edit_distance':
        return """
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        """

    elif problem_type == 'fibonacci':
        return """
        dp[i] = dp[i-1] + dp[i-2]
        """

    elif problem_type == 'coin_change_min':
        return """
        dp[i] = min(dp[i], dp[i - coin] + 1) for each coin if coin <= i
        """

    elif problem_type == 'coin_change_combinations':
        return """
        dp[i] = sum(dp[i - coin]) for each coin if coin <= i
        """

    elif problem_type == 'longest_increasing_subsequence':
        return """
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        """

    elif problem_type == 'rod_cutting':
        return """
        dp[i] = max(dp[i], prices[j - 1] + dp[i - j]) for each j <= i
        """

    elif problem_type == 'matrix_chain_multiplication':
        return """
        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]) for each k in range(i, j)
        """

    else:
        return "Invalid problem type"

# Example Usage:
print(dynamic_programming_recurrence_relations('lcs'))
print(dynamic_programming_recurrence_relations('knapsack'))
print(dynamic_programming_recurrence_relations('edit_distance'))
print(dynamic_programming_recurrence_relations('fibonacci'))
print(dynamic_programming_recurrence_relations('coin_change_min'))
print(dynamic_programming_recurrence_relations('longest_increasing_subsequence'))