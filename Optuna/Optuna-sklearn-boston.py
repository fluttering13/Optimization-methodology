import pandas as pd
import numpy as np
import optuna
import xgboost as xgb
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
x = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
y = raw_df.values[1::2, 2]

print('input_data',x.shape)
print('label',y.shape)

def objective(trial, X=x, y=y):
    """
    A function to train a model using different hyperparamerters combinations provided by Optuna.
    """
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.4)

    params = {
        'max_depth': trial.suggest_int('max_depth', 6, 15),
        "subsample": trial.suggest_float("subsample", 0.2, 1.0),
        'n_estimators': trial.suggest_int('n_estimators', 500, 2000, 100),
        'eta': trial.suggest_float("eta", 1e-8, 1.0, log=True),
        'alpha': trial.suggest_float('alpha', 1e-8, 1.0, log=True),
        'lambda': trial.suggest_float('lambda', 1e-8, 1.0, log=True),
        'gamma': trial.suggest_float("gamma", 1e-8, 1.0, log=True),
        'min_child_weight': trial.suggest_int('min_child_weight', 2, 10),
        'grow_policy': trial.suggest_categorical("grow_policy", ["depthwise", "lossguide"]),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.2, 1.0)
    }

    reg = xgb.XGBRegressor(**params)
    reg.fit(X_train, y_train,
            eval_set=[(X_valid, y_valid)], eval_metric='rmse',
            verbose=False)

    return mean_squared_error(y_valid, reg.predict(X_valid), squared=False)

# Creating Optuna object and defining its parameters
study = optuna.create_study(direction='minimize')
### Study with a random sampler
###study = optuna.create_study(sampler=RandomSampler(seed=42))
### Study with a CMA ES sampler
###study = optuna.create_study(sampler=CmaEsSampler(seed=42))
study.optimize(objective, n_trials = 10)

# Showing optimization results
print('Number of finished trials:', len(study.trials))

print('Best trial parameters:', study.best_trial.params)
print('Best score:', study.best_value)

###plot the score of the trials
# plotly_config = {"staticPlot": True}
fig=optuna.visualization.matplotlib.plot_optimization_history(study)
plt.show()

### plot the imporatance of hyper parameters
fig2 = optuna.visualization.matplotlib.plot_param_importances(study)
plt.show()

### plot the score-eta and score-grow_policy plot
fig3 = optuna.visualization.matplotlib.plot_slice(study, params=["eta", "grow_policy"])
plt.show()