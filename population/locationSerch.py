import csv
f = open('202006_202006_연령별인구현황_월간.csv')
data = csv.reader(f)

# for row in data:
#     if '서울특별시 성북구 안암동(1129060000)' == row[0]:
#         print(row)

# for row in data:
#     if '장위' in row[0]:
#         print(row)

# for row in data:
#     if '성북구' in row[0]:
#         for i in row[3:]:
#             print(i)

result = [0] * 11
for row in data:
    if '등촌제2' in row[0]:        # row[0]이 '장위'를 포함하고 있으면
        n = 0                   # n=0
        for i in row[3:]:       # 0-9세 구간부터 값을 가져오는데
            i = i.replace(",", "")  # ',' 지워주시고
            result[n] = result[n]+int(i) # 
            n = n+1

print(result)
