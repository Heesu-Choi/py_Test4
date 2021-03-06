import csv
import matplotlib.pyplot as plt

f = open('202006_202006_연령별인구현황_월간.csv')
data = csv.reader(f)

result = [0] * 11
for row in data:
    if '장위' in row[0]:
        n = 0
        for i in row[3:]:
            i = i.replace(",", "")
            result[n] = result[n]+int(i)
            n = n+1

plt.style.use('ggplot')
plt.rc('font', family='Malgun Gothic')
plt.title('장위동 인구구조')
plt.plot(result)
plt.show()
