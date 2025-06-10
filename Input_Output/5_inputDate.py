import datetime
date = input("Enter date in HH/MM/SS format")

print("Date Enetered is : ", datetime.datetime.strptime(date,"%H:%M:%S"))