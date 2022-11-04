def sql_database_remover():
    import pymysql
    from os import system
    result = []
    p = input('What is the SQL Server Password? ')          # Password
    system('clear|cls')
    conn = pymysql.connect(user='root',
                           host='localhost',
                           password=p)
    cur = conn.cursor()
    while True:
        a = input('Are you sure you want to delete all databases(this is irreversible)? ').lower()
        if a not in ['yes', 'no']:
            continue
        elif a == 'yes':
            break
        else:
            quit()
    cur.execute('show databases')
    res = cur.fetchall()
    for val in res:
        result.append(val[0])
    while True:
        a = input('Are you sure you want to delete all databases(second check)? ').lower()
        if a not in ['yes', 'no']:
            continue
        elif a == 'yes':
            break
        else:
            quit()
    for db in result:
        if db not in ('information_schema', 'performance_schema', 'mysql'):
            cur.execute(f'drop database {db}')
    print('The SQL Server has succesfully been wiped!!')
