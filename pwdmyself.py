user = 0
while True:
	password = input('請輸入密碼:')
	if password == 'a123456':
		print('登入成功!')
		break
	else :
		user = user + 1
		if user == 1:
			print('錯誤，你還有三次機會')
		if user == 2:
			print('錯誤，你還有二次機會')
		if user == 3:
			print('錯誤，你還有一次機會')
		if user == 4:
			print('系統關閉')
			break

	



