x = 3
while True:
    password = 'a123456'
    if input("請輸入密碼: ") == password: 
        print("登入成功! ")
        break
        
    else:    
        print('密碼錯誤! 還有', x - 1, '次機會')
        x = x - 1
    if x == 0:     
    	raise SystemExit