from itertools import combinations
from collections import defaultdict
from statistics import mean


def get_feature_combinations(additional_factors):
    """Get all possible combinations of features

    Args:
        additional_factors (list): a list of features that would include in the combination

    Returns:
        list: a list of possible combinations

    """
    all_combination = []
    for i in range(1, len(additional_factors)):
        combs = combinations(additional_factors, i)
        for comb in combs:
            all_combination.append(list(comb) + ['Price'])

    all_combination = [['Price']] + all_combination + [['Volume', 'RSI', 'ROC', 'OBV', 'Price']]
    return all_combination


def cal_avg_rank(all_rmse):
    """Calculate the average ranking for each feature combination

    Args:
        all_rmse (list): a list of prediction error for each ticker

    Returns:
        list: a list of tuples of (combination, average ranking), sort by average ranking in ascendant order

    """
    rank = defaultdict(list)
    for company_rmse_rank in all_rmse:
        for i in range(len(company_rmse_rank)):
            combination_name = ','.join(company_rmse_rank[i][0])
            rank[combination_name].append(i + 1)
    avg_rank = defaultdict(int)
    for combination in rank:
        avg_rank[combination] = mean(rank[combination])

    avg_rank = sorted(avg_rank.items(), key=lambda x: x[1])
    for rank in avg_rank:
        print(rank)
    return avg_rank
