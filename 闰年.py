input_year= int(input("请输入年份："))
if input_year%400==0:
    print("闰年")
else:
    if input_year%4==0 and input_year%100!=0:
        print("闰年")
    else:
        print("平年")