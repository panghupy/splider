# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import pymysql

class CrawljobbolePipeline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        #数据库的连接参数
        parmas = {
            'host':settings['MYSQL_HOST'],
            'user':settings['MYSQL_USER'],
            'passwd':settings['MYSQL_PWD'],
            'db':settings['MYSQL_DB'],
            'port':settings['MYSQL_PORT'],
            'charset':'utf-8',
        }
        # 一个*表示元组，**表示字典
        #这里创建了一个连接池
        dbpool = adbapi.ConnectionPool('pymysql',parmas)
        return cls(dbpool)

    def process_item(self, item, spider):
        #让连接池执行数据插入任务，并传递参数
        query = self.dbpool.runInteraction(self.insert_data_to_db,item,spider)
        #添加一个数据插入失败的回调
        query.addErrback(self.handle_err,item)
        return item

    def insert_data_to_db(self,cursor,item,spider):
        #使用游标执行数据插入
        insert_sql,parmas = item.insert_data()
        cursor.execute(insert_sql,parmas)

    def handle_err(self,failure,item):
        #数据插入失败的回调函数
        print(failure)
        print('数据库插入失败')






