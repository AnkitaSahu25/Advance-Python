'''file=open("C:\\Users\\as741\\OneDrive\\Desktop\\python.txt",'r')
print(file.read(6))
file.close()
file=open("C:\\Users\\as741\\OneDrive\\Desktop\\python.txt",'a')'''
fp1=open("num1.txt","w+")
fp1.write(input("enter numbers"))
fp1.seek(0)
x=0
st=fp1.read()
list1=st.split()
for i in list1:
    x=x+int(i)
print(x)


