import random
answer = random.randint(1, 100)
count = 0
while True:
	guess = input('猜猜看是1～100的哪一個數字： ')
	guess = int(guess)
	count = count + 1
	if guess == answer:
		print('你猜對了！')
		print('你猜了', count, '次')
		break
	elif guess > answer:
		print('答案比', guess, '小')
	elif guess < answer:
		print('答案比', guess, '大')
	elif guess > 100 or guess < 1:
		print('只能輸入1～100的整數')

