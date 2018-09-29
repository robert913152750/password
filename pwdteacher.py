password = 'a123456'
i = 3
while True:
	pwd = input('請輸入密碼:')
	if pwd == password:
		print('登入成功!')
		break
	else:
		i = i -1
		print('錯誤，剩餘',i,'機會')
		if i == 0:
			print('系統關閉')
			break


