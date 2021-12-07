from peewee import *

db = MySQLDatabase("fengshuidlt", host="127.0.0.1", port=3306, user="root", password="root")

class BaseModel(Model):
    class Meta:
        database = db

#设计数据表的时候有几个重要点一定要注意
"""
char类型， 要设置最大长度
对于无法确定最大长度的字段，可以设置为Text
设计表的时候 采集到的数据要尽量先做格式化处理
default和null=True
"""

class Periods(BaseModel):
    id = IntegerField(primary_key=True, default=0)
    no = IntegerField(default=0)
    one = IntegerField(default=0)
    two = IntegerField(default=0)
    three = IntegerField(default=0)
    four = IntegerField(default=0)
    five = IntegerField(default=0)
    six = IntegerField(default=0)
    seven = IntegerField(default=0)


if __name__ == "__main__":
    db.create_tables([Periods])
