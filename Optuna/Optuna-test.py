import optuna
import matplotlib.pyplot as plt
def objective(trial):
    x1 = trial.suggest_float("x1", -5, 5)
    x2 = trial.suggest_float("x2", -5, 5)
    return (x1 + 2) ** 2 + (x2 - 4) ** 2

# Creating Optuna object and defining its parameters
study = optuna.create_study(direction='minimize')
study.optimize(objective, n_trials = 50)

print('Number of finished trials:', len(study.trials))
print('Best trial parameters:', study.best_trial.params)
print('Best score:', study.best_value)

optuna.visualization.matplotlib.plot_optimization_history(study)
plt.show()