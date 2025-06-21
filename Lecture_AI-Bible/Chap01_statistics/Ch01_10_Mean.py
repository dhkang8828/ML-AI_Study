import math

if __name__ == "__main__":

    ## Example Data
    data = [56, 93, 88, 72, 65] 
    
    ## 평균 계산
    mean = 0
    for x in data:
        mean += x  / len(data)
    print(f"Mean: {mean:.2f}")
    
    ## 분산 계산
    variance = 0
    for x in data:
        variance += ((x - mean) ** 2) / len(data)
    print(f"Variance: {variance:.2f}")
    
    ## 표준편차 계산
    std = math.sqrt(variance)
    print(f"Standard Deviation: {std:.2f}")
    