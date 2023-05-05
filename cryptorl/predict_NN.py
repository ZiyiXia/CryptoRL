from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import tensorflow as tf

from .utils import get_feature_combinations
from .data import prep_training_data


def all_nn(processed_df, additional_factors):
    """Use neural network with given processed dataframe object and additional factors to predict

    Args:
        processed_df (DataFrame): a DataFrame object with well processed data
        additional_factors (list): a list of feature combination that we want to use

    Returns:
        list: a list of prediction results

    """
    all_rmse = []
    all_combinations = get_feature_combinations(additional_factors)

    for comb in all_combinations:
        cur_df = processed_df[comb]
        X, y = prep_training_data(cur_df, 10)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(16, activation='relu'))
        model.add(tf.keras.layers.Dense(8, activation='relu'))
        model.add(tf.keras.layers.Dense(1, activation='relu'))
        model.compile(optimizer="Adam", loss="mse")

        model.fit(X_train, y_train, epochs=100, verbose=0)

        y_pred = model.predict(X_test, verbose=0)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        all_rmse.append([comb, rmse])
    all_rmse = sorted(all_rmse, key=lambda x: x[1])
    print(*all_rmse, sep="\n")
    return all_rmse
