import csv
f = open('202006_202006_연령별인구현황_월간_남여.csv')
data = csv.reader(f)

m = []
f = []

for row in data:
    if '전국' in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3].replace(",", "")))    # i가 0부터 시작하기 때문에 3번째 열부터 계산하고 싶어
            f.append(int(row[-(i+1)].replace(",", ""))) # 뒤에서부터 보자 100세 이상부터~0세 reverse로 한 번 뒤집어 줘야 함

# if '전국' in row[0]:
#     for i in row[3:104] :
#         m.append(int(i))
#     for i in row[106:] :
#         f.append(int(i))

print(m)
print(f)
f.reverse()
print(f)
