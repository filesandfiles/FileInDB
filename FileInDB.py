from .Config import MySQLConfig
import MySQLdb

class FileInDB:

    def __init__(self):
        try:
            if not Config.DBConfig['Mysql']:
                print "Error! Database is not defined as Mysql!!"
            self.db = MySQLdb.connect(host=MySQLConfig['host'],user=MySQLConfig['user'],
                passwd=MySQLConfig['passwd'],db=MySQLConfig['db'])
        except:
            print "Error! Database Exception"
            exit(1)
    def save_file(f,unique_id):
        cursor = self.db.cursor()
        sql = "insert into file_content(fid,sno,content) values (%s, %s, %s);"
        count = 1
        try:
            for chunk in f.chunks():
                cursor.execute(sql,(str(unique_id),str(count),chunk))
                count = count + 1
            self.db.commit()
        except:
            self.db.rollback()
            return False
        return True
    def get_file(unique_id,filename):
        output = open(filename)
        cursor = self.db.cursor()
        sql = "select content from file_content where fid=%s order by sno;"
        try:
            cursor.execute(sql,[fid])
            for eachchunk in cursor.fetchall():
                output.write(str(eachchunk[0]))
        except:
            return False
        output.close()
        return True