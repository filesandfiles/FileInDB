CHUNK_SIZE = 8K
MySQLConfig = {
 'host':'localhost',
 'db':'t_dms',
 'user':'amrut',
 'passwd':'p0reiczm',
    }

MyTables = """
CREATE TABLE file_content(
fid INT UNSIGNED NOT NULL,
sno INT UNSIGNED  NOT NULL,
content mediumblob NOT NULL
);
"""