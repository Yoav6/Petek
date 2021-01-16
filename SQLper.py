import sqlite3
import socket
import threading
import datetime  # from datetime
conn = sqlite3.connect(':memory:')
c = conn.cursor()

#######  socket connection  #######

HEADER = 16
PORT = 5050
SERVER = '0.0.0.0' #socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # diff
server.bind(ADDR)  # diff


def activate_socket():
    def handle_client(s_conn, addr):  # diff
        print(f'[NEW CONNECTION] {addr} connected')
        connected = True
        while connected:
            msg_length = s_conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = s_conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f'[{addr}] {msg}')
                s_conn.send("Message received".encode(FORMAT))

        s_conn.close()

    def start():  # diff
        server.listen()
        print(f'[LISTENING] Server is listening on {SERVER}')
        while True:
            s_conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(s_conn, addr), daemon=True)
            thread.start()
            print(f'[ACTIVE CONNECTION] {threading.active_count() - 2}')

    print('[STARTING] Server is starting...')
    start()

#######  base functions  #######

def get_column_names(table, type_='list'):
    cursor = conn.execute("select * from {0}".format(table))
    list_ = list(map(lambda x: x[0], cursor.description))
    if type_ == 'dict':  # currently unused in the code
        dict_ = {}
        for key in list_:
            dict_[key] = None
        return dict_
    return list_

def insert_row_to_table(table, **kwargs):
    values = get_column_names(table, 'dict')
    for key in kwargs:
        if key in values:
            values[key] = kwargs[key]
        else:
            print(key, 'is not an applicable column')
    columns = ':' + ', :'.join(values)
    with conn:
        c.execute(f"INSERT INTO {table} VALUES ({columns})", values)
    return c.lastrowid

def update_rows_in_table(table, where: str, **kwargs):
    columns = '=?,'.join(kwargs) + '=?'
    #where = where[0] + '=' + str(where[1])
    with conn:
        c.execute(f"UPDATE {table} SET {columns} WHERE {where}", tuple(kwargs.values()))
    return c.lastrowid
    #print("Update failed: input:", kwargs)

#######  Insert Functions  #######

def insert_person_basic(first, last):
    #if first and last and type(birth_year) == int:
    return insert_row_to_table('people', first_name=first, last_name=last)

def insert_discussion():
    return insert_row_to_table('discussions', datetime=datetime.datetime.now())

def add_person_discussion_relation(person_id, discussion_id, role):
    if role == ('mediator' or 'initiator' or 'charged' or 'escort'):
        insert_row_to_table('people_discussions',
                            person_id=person_id, discussion_id=discussion_id, role=role)
    else:
        print(role, 'is not an applicable role')

def add_student_mentor_relation(student_id, mentor_id):
    update_rows_in_table('student_mentor',
                         f'student_id={student_id} AND end_time IS NULL', end_time=datetime.date.today())
    insert_row_to_table('student_mentor',
                        student_id=student_id, mentor_id=mentor_id, start_time=datetime.date.today())

#######  Update Functions  #######

def update_student_mentor_relation(student_id, mentor_id, start_time=None, end_time=None):
    pass

#######  Get Functions  #######

def get_all_people():
    c.execute("SELECT first_name || ' ' || last_name AS full_name, id from people")
    return c.fetchall()

def get_all_staff(current_only=True):
    val = '1' if current_only else '1 OR 2'
    c.execute(f"SELECT first_name || ' ' || last_name AS full_name, id from people WHERE staff={val}]")
    return c.fetchall()

def get_all_mentored_students(mentor_id):
    c.execute(f'SELECT student_id from student_mentor WHERE mentor_id={mentor_id} AND end_time is NULL')
    return c.fetchall()

def get_person_by_id(id_):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * from people WHERE id=?", (str(id_)))
    return dict(c.fetchone())

def get_discussion_by_id(id_):
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * from discussions WHERE id=?", (str(id_)))
    return dict(c.fetchone())

def check_if_name_exists(first_name, last_name):
    c.execute(f"SELECT id from people WHERE first_name='{first_name}' AND last_name='{last_name}'")
    return c.fetchall()

try:
    c.execute("""CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY,
                first_name text,
                last_name text,
                birth_year integer,
                student integer,
                committee_member integer,
                staff integer,
                current_mentor integer,
                phone text
                )""")
    #  past_mentors stores list of 3-tuples, 1st value is mentor id, 2nd is start year, 3rd is end year
except sqlite3.OperationalError:
    print('table people already exists')

try:
    c.execute("""CREATE TABLE IF NOT EXISTS discussions (
                id INTEGER PRIMARY KEY,
                datetime text,
                length integer,
                summery_or_transcript text,
                decision text
                )""")
except sqlite3.OperationalError as e:
    print(e)
    print('table discussions already exists')

try:
    c.execute("""CREATE TABLE IF NOT EXISTS people_discussions (
                id INTEGER PRIMARY KEY,
                person_id INTEGER NOT NULL,
                discussion_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                missing INTEGER,
                FOREIGN KEY(person_id) REFERENCES people(id),
                FOREIGN KEY(discussion_id) REFERENCES discussions(id)
                )""")
except sqlite3.OperationalError as e:
    print(e)
    print('table people_discussions already exists')

try:
    c.execute("""CREATE TABLE IF NOT EXISTS student_mentor (
                student_id INTEGER NOT NULL,
                mentor_id INTEGER NOT NULL,
                start_time text,
                end_time text,
                FOREIGN KEY(student_id) REFERENCES people(id),
                FOREIGN KEY(mentor_id) REFERENCES people(id)
                )""")
except sqlite3.OperationalError as e:
    print(e)
    print('table student_mentor already exists')


insert_discussion()

print(get_discussion_by_id(1))

insert_row_to_table('people', first_name='john', last_name='smith', birth_year=2000, staff=1)
insert_row_to_table('people', first_name='גילה', last_name='גוב', birth_year=1970, staff=1)

insert_person_basic('מיה', 'גל')
insert_person_basic('גשם', 'גל')
insert_person_basic('גיא', 'שגיא')
insert_person_basic('Yoav', 'ravid')
insert_person_basic('רותם', 'רונן')

print(get_person_by_id(1))
update_rows_in_table('people', 'id=1', first_name='Sebastian', last_name='watson')  # , git=True
print(get_person_by_id(1))

add_person_discussion_relation(1, 1, 'mediator')

print(list(c.execute('select * from people_discussions')))
#print(get_person_by_id(2))

people = get_all_people()
print(people)

add_student_mentor_relation(3, 1)
add_student_mentor_relation(3, 6)
print(list(c.execute('select * from student_mentor')))
print(get_all_staff())


if __name__ == '__main__':
    socket_main_thread = threading.Thread(target=activate_socket)
    socket_main_thread.start()

#conn.close()
