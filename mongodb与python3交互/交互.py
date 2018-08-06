import pymongo

# 创建客户端名称
client = pymongo.MongoClient('localhost', 27017)
# 进入数据库
db = client.student
# 获取数据库中的集合,没有就创建
info = db.info
info = db['info']

document = {
    'name': 'zhangsan',
    'age': 20,
    'gender': 1
}
result = info.insert(document)

result = info.update({'name':'zhangsan'},{'$set':{'age':200}})

result = info.find({'name':'zhangsan'})
for i in result:
    print(i)
