password = 'a123456'
i = 3
while i > 0:
	i = i -1
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('剩餘',i,'機會')
		
		


		


