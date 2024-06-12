import psycopg2


# conn = psycopg2.connect(database='netologydb_1', user='postgres', password='ichbinaleksey')
# with conn.cursor() as cur:
#     cur.execute("CREATE TABLE test(id SERIAL PRIMARY KEY);")
#     conn.commit()
#     # conn.rollback()
# cur = conn.cursor()
# cur.execute('')
# cur.close()
# conn.close()
c1 = None
c2 = '47568734'
c3 = [432, 543, 4633]
c4 = 'ergjer'
a = [None, '98457678945', [72, 87236, 8932947]]
b = ['98456','87396']
c = [c1, c2, c3, c4]

for i in c:
        if i and type(i) is not list:
                if i == c1:
                        print('this c1')
                elif i == c2:
                        print('this c2')
                elif i == c4:
                        print('this c4')
        elif type(i) is list:
                for l in i:
                        print(l)