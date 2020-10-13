# 2020v1
Model:
run "main_create_model.py" in "model" with changing the folder; "mainpath0 =./data"
Evaluation:
run "main_test.py" in "evl" with changing the folder, "mainpath=./data/", to the path created by "model".


Requirement: Tensorflow > 2.1.0, Scit-learn >0.23.1


