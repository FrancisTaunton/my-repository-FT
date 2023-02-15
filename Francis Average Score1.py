total = 0
for counter in range(1,11):
  score = input('Enter score ' + str(counter) + ': ')
  score = int(score)
  total = total + score

average_score = total / 10
print('Your average score is:', average_score)
