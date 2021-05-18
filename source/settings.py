# 기본
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# 데이터 가져오기
import pandas as pd
from sklearn.datasets import load_breast_cancer

# 훈련/검증용 데이터 분리
from sklearn.model_selection import train_test_split

# 분류모델
from sklearn.tree import DecisionTreeClassifier  # 결정트리
from sklearn.neighbors import KNeighborsClassifier  # K-최근접 이웃
from sklearn.linear_model import LogisticRegression  # 로지스틱
# 앙상블 모델 구축
from sklearn.ensemble import VotingClassifier  # 과반수 투표

# 모델 검정
from sklearn.metrics import confusion_matrix, classification_report  # 혼돈, 혼잡
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import roc_curve, auc  # ROC 곡선 그리기

# 최적화
from sklearn.model_selection import learning_curve, validation_curve, GridSearchCV, cross_val_score