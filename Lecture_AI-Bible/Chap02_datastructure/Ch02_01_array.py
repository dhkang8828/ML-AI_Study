if __name__ == "__main__":
    
    # 1차원 배열 생성
    array_1d = [1, 2, 3, 4, 5]
    print("1D Array:", array_1d)
    
    # 2차원 배열 생성
    array_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("2D Array:")
    for row in array_2d:
        print(row)
       
    '''
    # List Comprehension
    ## 기본 문법: [expression for item in iterable if condition]
    ## item: 반복 가능한 객체(iterable)에서 하나씩 가져온 요소
    ## iterable: 리스트, 튜플, 문자열 등 반복 가능한 객체
    ## if condition: 조건을 만족하는 경우에만 요소 포함 
    ''' 
    n = 5
    arry_comp = [i for i in range(n)]
    print("List Comprehension Array:", arry_comp)
    
    # 2차원 배열 초기화#1
    n = 3
    m = 5
    arr = [[0] * m for i in range(n)]
    print("Initialized 2D Array:", arr)
    
    ## 2차원 배열 초기화#2
    arr2 = [[i * m + j for j in range(m)] for i in range(n)]
    print("Initialized 2D Array with Values:", arr2)
        
    # 배열의 길이
    print("Length of 1D Array:", len(array_1d))
    print("Length of 2D Array:", len(array_2d))
    
    # 배열의 특정 요소 접근
    print("Element at index 0 in 1D Array:", array_1d[0])
    print("Element at row 0, column 1 in 2D Array:", array_2d[0][1])