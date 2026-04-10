import sys

input = sys.stdin.readline

#31 28 31 30 31 30 31 31 30 31 30 31
def solve():
    month_date, year_time = input().split(",")

    month, date = month_date.split()
    date = int(date)
    year, time = year_time.split()
    year = int(year)

    h, m = map(int,time.split(":"))

    total = 60*24*(366 if year%400==0 or(year%4==0 and year%100 !=0 ) else 365)

    day_of_month = [0, 31, 29 if year%400==0 or(year%4==0 and year%100 !=0 ) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month_dict = { 
        "January":1,
        "February":2 ,
        "March":3 ,
        "April":4 ,
        "May":5,
        "June":6 ,
        "July":7 ,
        "August":8 ,
        "September":9,
        "October":10 ,
        "November":11,
        "December":12,
    }

    month_minutes = 0

    end_at = month_dict[month]

    for i in range(1,end_at):
        
        month_minutes += day_of_month[i]*24*60



    date_minutes = (date-1)*24*60
    hour_minute = int(h)*60

    total_minute = month_minutes+date_minutes+hour_minute+m

    print(total_minute/total*100)

    



if __name__=="__main__":
    solve()