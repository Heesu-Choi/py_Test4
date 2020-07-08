import csv      # 우리동네랑 가장 비슷한 인구구조가 비슷한 곳은 어느 동네인가?
f = open('202006_202006_연령별인구현황_월간_전국.csv')
data = csv.reader(f)

mn = 10000
result = []
result_name = ''

home = []
<<<<<<< HEAD
home_name = input("동 이름을 입력해주세요")
home_linenum = 0                
=======
home_name = input("동 이름을 입력해 주세요!! :: ")

home_linenum = 0
>>>>>>> 5f02c918cdbe6c83ddc1311264a3966d0d2a396c
for row in data:
    if home_name in row[0]:
        home_linenum = data.line_num
        for i in row[3:]:
            i = i.replace(",", "")
            home.append(int(i))

f = open('202006_202006_연령별인구현황_월간_전국.csv')
data = csv.reader(f)

for row in data:
    if data.line_num == 1 or data.line_num == home_linenum:     # 첫번째 행이거나 우리동네 행은 지나가
        continue
    away = []
    res = [0] * 101         # 0으로 차있는 101개의 리스트를 만들어서
    for i in row[3:]:       # 연령별 인구 하나씩 토스해줌
        i = i.replace(",", "")  # ',' 없애주고
        away.append(int(i)) # away에 하나씩 넣어주세요

    for i in range(0, 101):
        res[i] = home[i]-away[i]    # 101개의 차이값
        res[i] = abs(res[i])

    sumRes = sum(res)    # 차이값의 총합

    if(mn > sumRes):               # 실질적으로 값을 계산해서 기존의 최소값보다 작은 값이 나오면 다음을 실행할 것!
        result_name = row[0]        # 맨 첫번째 열
        mn = sumRes                 # 값의 차이
        result = away               # away 리스트를 result에 넘겨줌

print(result_name)
print(result)
print(mn)
