n=int(input("請輸入一個數字n(2<=n<=15):"))
if 2<=n <= 15:
    #2. 依序印出每一行
 for i in range(1, n+1):
    spaces=" "*(n-i)
    row_str=""
    
    start_num=n- i+ 1
    end_num =n+i-1
    
    for num in range(start_num, end_num+ 1):
        if num<10:
            row_str +=str(num)
        else:
            
            row_str+=chr(ord('a')+num-10)
            
    print(spaces +row_str) #必須是spaces在前面
else:
        print("輸入錯誤，數字必須在2到15之間。")
        
        
