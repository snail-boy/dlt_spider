(int|str) 表示参数既可以是int类型，也可以是str类型
(datetime | str) 表示参数既可以是datetime类型，也可以是str类型
 
year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
month (int|str) – month (1-12) -（表示取值范围为1-12月）
day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
second (int|str) – second (0-59) - （表示取值范围为0-59秒）
start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）



# 一个定时爬去大乐透彩票网站的爬虫项目，定时爬去，存储在mysql数据库中，并供风水大乐透http://www.webrabbit.top/使用

