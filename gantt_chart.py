import matplotlib.pyplot as plt

# 創建一個包含任務和持續時間的數據
tasks = ['A', 'B', 'C', 'D', 'E']
durations = [10, 5, 19, 2, 8]  # 每個任務的持續時間

# list.sort(durations) #SJF
# PS
# tasks = ['Task C', 'Task A', 'Task E', 'Task B','Task D']
# durations = [19, 10, 8, 5, 2]

# 新增一個暫存list
tamp = [10, 5, 19, 2, 8]
rr_durations=[]

# 將每個任務的持續時間存入rr_durations
for i in range(1,time :=int((max(durations))/5)+1):
    x=0
    for y in tamp:

        if tamp.count(0) == len(tamp) - 1 and y >= 5:
            rr_durations.append(max(tamp))

        elif y >= 5:
            rr_durations.append(5)
            tamp.pop(x)
            tamp.insert(x, (y - 5))

        elif y < 5 and y > 0:
            rr_durations.append(y)
            tamp.pop(x)
            tamp.insert(x, (y - y))
        else:
            rr_durations.append(0)
        x+=1


# 計算每個任務的開始時間和結束時間
start_times = [sum(rr_durations[:i]) for i in range(len(rr_durations))]
end_times = [start + rr_durations for start, rr_durations in zip(start_times, rr_durations)]


# 設定圖表
fig, ax = plt.subplots(figsize=(12, 2))
colors = ["#1f77b4", "#f2ab15", "#2ca02c", "#d62728", "#9467bd"]

# 添加每個任務的橫條並標註任務名稱(RR)
for i, (task, start, rr_duration, color) in enumerate(zip(tasks*3, start_times, rr_durations, colors*3)):
     if rr_duration != 0:
        ax.barh(0, rr_duration, left=start, height=0.5, align='center', color = color)
        ax.text(start + rr_duration / 2, 0, task, ha='center', va='center', color='white', fontweight='bold', fontsize ='large', fontfamily='serif')

# 添加每個任務的橫條並標註任務名稱(非RR)
# for i, (task, start, rr_duration,color) in enumerate(zip(tasks, start_times, rr_durations, colors)):
    # ax.barh(0, rr_duration, left=start, height=0.5, align='center', color=color)
    # ax.text(start + rr_duration / 2, 0, task, ha='center', va='center', color='white', fontweight='bold', fontsize ='large', fontfamily='serif')


# 設定標籤和標題
ax.set_yticks([])

start_times.append(sum(durations))
x_ticks = start_times
ax.set_xticks(x_ticks)

ax.set_xlabel('Time')
ax.set_title('(FCFS) Gantt Chart',fontweight='demi', fontsize ='x-large', fontfamily='serif')
ax.set_xlim(0, sum(durations))


# 隱藏 y 軸
ax.yaxis.set_visible(False)


# 顯示圖表
plt.show()

