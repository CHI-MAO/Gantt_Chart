import matplotlib.pyplot as plt

# 創建一個包含任務和持續時間的數據
tasks = ['A', 'B', 'C', 'D', 'E']
durations = [10, 5, 19, 2, 8]  # 每個任務的持續時間

# list.sort(durations) #SJF
# PS
# tasks = ['Task C', 'Task A', 'Task E', 'Task B','Task D']
# durations = [19, 10, 8, 5, 2]



# 計算每個任務的開始時間和結束時間
start_times = [sum(durations[:i]) for i in range(len(durations))]
end_times = [start + duration for start, duration in zip(start_times, durations)]


# 設定圖表
fig, ax = plt.subplots(figsize=(12, 2))
colors = ["#1f77b4", "#f2ab15", "#2ca02c", "#d62728", "#9467bd"]


# 添加每個任務的橫條並標註任務名稱
for i, (task, start, duration,color) in enumerate(zip(tasks, start_times, durations, colors)):
    ax.barh(0, duration, left=start, height=0.5, align='center', color=color)
    ax.text(start + duration / 2, 0, task, ha='center', va='center', color='white', fontweight='bold', fontsize ='large', fontfamily='serif')


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

