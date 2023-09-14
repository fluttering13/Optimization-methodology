# Optimization-methodology
## META optimzation (hyperparameter optimzation)
這邊使用到optuna的包來進行優化，並實作XGboost在sklearn-boson資料集上的表現

Optuna code explanation

https://optuna.readthedocs.io/en/stable/index.html

Optuna example:

https://github.com/optuna/optuna-examples


## Modohiyaiku (Faster and Faster)
就是一些寫code或是用code的技巧都放這
### CV2 
1. 從BGR轉RGB就直接矩陣倒轉就好
### pytorch
1. pytorch的dataloader可以使用pin_memory的指令合併