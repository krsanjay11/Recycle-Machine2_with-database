import sqlite3
con = sqlite3.connect('databasefile.db')
print("open successfully")

# command = "create table todo( id int, task text, date text, status text)"
# command = "insert into todo(id, task, date, status) values(2,'do python','27-7-2019', 'progress')"
command = "select * from todo"
# command = "update todo set status='done' where id = 2"
# command = "delete from todo where id = 1"
# command = "drop table todo"
result= con.execute(command)
# print(result)
# for row in result:
#     id, task, date, status = row
#     # print(i)
#     print(id, task, date, status)
# con.commit()
# print('total changes',con.total_changes)
r = result.fetchall()
print(r)