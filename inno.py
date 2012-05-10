import settings
from django.core.management import setup_environ

setup_environ(settings)

def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    
def set_InnoDB():
    from django.db import connection
    c = connection.cursor()
    c.execute("show tables")
    for row in dictfetchall(c):
        str = 'show create table ' + row["Tables_in_cbframe"]
        cc = connection.cursor()
        cc.execute(str)
        for table in dictfetchall(cc):
            if "MyISAM" in table["Create Table"]:
                print "converting table " + row["Tables_in_cbframe"]
                alter = "alter table " + row["Tables_in_cbframe"] + " ENGINE=INNODB"
                ccc = connection.cursor()
                ccc.execute(alter)
                ccc.close()
        cc.close()
    c.close()
            
if __name__ == '__main__':
    set_InnoDB()
