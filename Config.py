CHUNK_SIZE = 8K
MySQLConfig = {
 'host':'localhost',
 'db':'t_dms',
 'user':'apuser',
 'passwd':'user@123',
    }

MyTables = """
CREATE TABLE file_content(
fid INT UNSIGNED NOT NULL,
sno INT UNSIGNED  NOT NULL,
content mediumblob NOT NULL
);
"""
