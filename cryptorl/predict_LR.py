import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

from utils import get_feature_combinations
from data import prep_training_data


def test_all_lr(processed_df, additional_factors):
    if len(processed_df) == 0:
        return processed_df
    all_rmse = []
    all_combinations = get_feature_combinations(additional_factors)

    # loop through all feature combinations
    for comb in all_combinations:
        cur_df = processed_df[comb]
        X, y = prep_training_data(cur_df, 10)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # standardize data so the model won't be affected by huge ranges and huge variances of some features
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Add a column of ones to the feature matrices to record bias
        X_train = np.hstack([np.ones((X_train.shape[0], 1)), X_train])
        X_test = np.hstack([np.ones((X_test.shape[0], 1)), X_test])

        # train linear regression model
        reg = LinearRegression().fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        all_rmse.append([comb, rmse])
    all_rmse = sorted(all_rmse, key=lambda x: x[1])
    print(*all_rmse, sep="\n")
    return all_rmse