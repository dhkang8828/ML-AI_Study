import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    X = [97, 85, 26, 54, 76, 15, 33, 83, 88, 91]
    Y = [100, 92, 31, 61, 83, 28, 57, 45, 92, 93]
    
    plt.plot(X, Y, 'o')
    plt.xlabel('Math')
    plt.ylabel('English')
    plt.title('Math vs English Scores')
    plt.grid(True)
    plt.savefig('/home/dhkang/data3/work/AI_Study/ML-AI_Study/Lecture_AI-Bible/Chap01_statistics/Ch01_12_Covariance.jpg')
    
    ## X 평균(Mean) 계산
    x_mean = 0
    for x in X:
        x_mean += x / len(X)
    ## X 분산(Variance) 계산
    x_var = 0
    for x in X:
        x_var += ((x - x_mean) ** 2) / (len(X) - 1)
    ## X 표준편차(Standard Deviation) 계산
    x_std = math.sqrt(x_var)
    print(f"X Mean: {x_mean:.2f}, X Variance: {x_var:.2f}, X Standard Deviation: {x_std:.2f}")    
        
    ## Y 평균(Mean) 계산
    y_mean = 0
    for y in Y:
        y_mean += y / len(Y)
    ## Y 분산(Variance) 계산
    y_var = 0
    for y in Y:
        y_var += ((y - y_mean) ** 2) / (len(Y) - 1)
    y_std = math.sqrt(y_var)
    print(f"Y Mean: {y_mean:.2f}, Y Variance: {y_var:.2f}, Y Standard Deviation: {y_std:.2f}")
    
    ## 공분산(Covariance) 계산
    covariance = 0
    for x, y in zip(X, Y):
        covariance += ((x - x_mean) * (y - y_mean)) / (len(X) - 1)
    print(f"Covariance: {covariance:.2f}")
    print(f"Covariance (using numpy): {np.cov(X, Y)[0][1]:.2f}")
    
    ## 상관계수(Correlation Coefficient) 계산
    correlation_coefficient = covariance / (x_std * y_std)    
    ## correlation_coefficient = covariance / math.sqrt(x_var * y_var)
    print(f"Correlation Coefficient: {correlation_coefficient:.2f}")
    print(f"Correlation Coefficient (using numpy): {np.corrcoef(X, Y)[0][1]:.2f}")
