
score_list = []
for i in range(10):
    n = int(input())
    score_list.append(n)

cnt = 0
end = 0
score = 0
while cnt < 10:
    end += 1
    cnt += 1
    score = sum(score_list[0:end])
    compare_score = sum(score_list[0:end - 1])
    if score >= 100:
        break

if score > 100 and abs(100 - compare_score) < abs(100 - score):
    print(compare_score)
else:
    print(score)