import matplotlib as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn import tree

from data import prep_training_data


def dt_pruning(processed_df):
    if len(processed_df) == 0:
        return processed_df
    all_rmse = []
    X, y = prep_training_data(processed_df, 10)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Fit the Decision Tree with all features and obtain the max depth
    dt_max = DecisionTreeRegressor(random_state=0).fit(X_train, y_train)
    all_depth = [int(i) for i in range(1, dt_max.tree_.max_depth + 1)]

    # Prune the tree and record MSE
    for cur_depth in all_depth:
        reg = DecisionTreeRegressor(random_state=0, max_depth=cur_depth).fit(X_train, y_train)
        y_pred = reg.predict(X_test)
        rmse = mean_squared_error(y_test, y_pred, squared=False)
        all_rmse.append(rmse)

    # Get tree depth with the smallest MSE and plot the tree
    fn = [x[0] for x in list(X.columns)]
    best_depth = np.argmin(all_rmse)
    print("best_depth:", best_depth)
    best_tree = DecisionTreeRegressor(random_state=0, max_depth=best_depth).fit(X_train, y_train)
    plt.figure(figsize=(12, 12))
    tree.plot_tree(best_tree, fontsize=10, feature_names=fn)

    return best_tree


def dt_feature_importance(best_model, feature_names):
    feat_imps = zip(feature_names, best_model.feature_importances_)
    feat, imps = zip(*(sorted(list(filter(lambda x: x[1] != 0, feat_imps)), key=lambda x: x[1])))

    # Get feature importance graph
    plt.figure(figsize=(3, 5))
    plt.barh(feat, imps)
    plt.xlabel("Feature Importance")
    plt.ylabel("Features")
    plt.title("Feature Importance of Decision Tree")
    plt.yticks(fontsize=7)
    plt.show()

    processed_comb = set()
    for feature in feat:
        feat = re.sub(r'[0-9]', '', feature)
        processed_comb.add(feat)
    comb = list(processed_comb)
    comb.sort()
    print("feature combination:", comb)
    return comb
