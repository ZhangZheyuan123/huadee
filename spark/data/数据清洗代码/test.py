list = []
a = 0
for line in open("C://Users/Shinelon/Desktop/002.txt", "r"):
    list.append(line)
clear_line_index = 0
list[0].split()
while (clear_line_index < len(list)):
    if list[clear_line_index].count('@')==8:
        clear_line_index=clear_line_index+1
        pass
    else:
        list.pop(clear_line_index)
    pass

for i in range(0, len(list)):
    list[i] = list[i].replace("万元", "*10000")
    list[i] = list[i].replace("亿元", "*100000000")
    list[i] = list[i].replace(",", "")
    list[i] = list[i].replace("没分数", "0")
    list[i] = list[i].replace("没票房", "0")
    list[i] = list[i].replace("没想看人", "0")
    list[i] = list[i].replace("反腐", "其他")
    list[i] = list[i].replace("儿童", "其他")
    list[i] = list[i].replace("情色", "其他")
    list[i] = list[i].replace("西部", "其他")
    list[i] = list[i].replace("运动", "其他")
    list[i] = list[i].replace("记录片", "其他")
    list[i] = list[i].replace("女性", "其他")
    list[i] = list[i].replace("成人", "其他")
    list[i] = list[i].replace("律政", "其他")
    list[i] = list[i].replace("青春", "其他")
    list[i] = list[i].replace("微电影", "其他")
    list[i] = list[i].replace("纪录", "其他")
    list[i] = list[i].replace("综艺", "其他")
    list[i] = list[i].replace("犯罪", "其他")
    list[i] = list[i].replace("传记", "其他")
    list[i] = list[i].replace("美食", "其他")
    list[i] = list[i].replace("歌舞", "其他")
    list[i] = list[i].replace("网络", "其他")
    list[i] = list[i].replace("古装", "其他")
    list[i] = list[i].replace("恐怖", "惊悚")
    list[i] = list[i].replace("舞台艺术", "其他")
    list[i] = list[i].replace("同性", "其他")
    list[i] = list[i].replace("武侠", "其他")
    list[i] = list[i].replace("儿童", "其他")
    list[i] = list[i].replace("奇幻", "其他")
    list[i] = list[i].replace("农村", "其他")
    list[i] = list[i].replace("戏曲", "其他")
    list[i] = list[i].replace("脱口秀", "其他")
    list[i] = list[i].replace("战争", "其他")
    list[i] = list[i].replace("历史", "其他")
    list[i] = list[i].replace("偶像", "其他")
    list[i] = list[i].replace("励志", "其他")
    list[i] = list[i].replace("游戏秀", "其他")
    list[i] = list[i].replace("短片", "其他")
    list[i] = list[i].replace("新闻", "其他")
    list[i] = list[i].replace("真人秀", "其他")
    list[i] = list[i].replace("黑色电影", "其他")
    list[i] = list[i].replace("音乐", "其他")
    list[i] = list[i].replace("家庭", "其他")

with open("C://Users/Shinelon/Desktop/allo.txt", "a") as file:
    for li in list:
        file.write(li)
