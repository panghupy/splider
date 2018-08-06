import pymongo


class MongoHelper(object):
    '''封装python3与mongodb交互'''

    def __init__(self):
        self.ip = 'localhost'
        self.port = 27017
        self.client = pymongo.MongoClient(self.ip, self.port)

    def get_database(self, db):
        '''获取数据库，没有就创建'''
        self.db = self.client.db

    def get_collection(self, collection):
        '''获取集合，没有则创建'''
        self.collection = self.db.collection


if __name__ == '__main__':
    mongoHelper = MongoHelper()
    mongoHelper.get_database('duanjinsong')
    print(mongoHelper.db)
