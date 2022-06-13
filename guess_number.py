import random
answer = random.randint(1, 100)

while True:
	guess = input('猜猜看是1～100的哪一個數字： ')
	guess = int(guess)
	if guess == answer:
		print('你猜對了！')
		break
	elif guess > answer:
		print('答案比', guess, '小')
	elif guess < answer:
		print('答案比', guess, '大')
	elif guess > 100 or guess < 1:
		print('只能輸入1～100的整數')

