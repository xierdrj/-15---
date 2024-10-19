n=2000#最大数据量
res=[]
for _   in range(2000):#python的循环结构 循环中不需要用到迭代次数用_来表示
    c,in_,t=input().split()#c,in_,t是三个字段 保存正确值 输入值 时间
    res.append([c,in_,int(t)])#将读取的数据储存在列表res中
print(res)  
ans=0
n=len(res)#返回子列表的个数
 
for i in range(n):
    if res[i][0]!=res[i][1]:#如果用户输入是正确的
        continue#跳过当前循环的剩余部分，直接进入下一次循环的迭代
    st=i#定位第一次正确结果和输入结果相同的位置
    while i+1<n and res[i+1][0]==res[i+1][1] and res[i+1][2]-res[i][2]<=1000:
        i+=1#找到基于第一次位置的后续连击
    ans=max(ans,i-st+1)
print(ans)