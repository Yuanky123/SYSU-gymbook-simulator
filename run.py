import os
import json
from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask import request
import random
import copy
from flask import jsonify

app = Flask(__name__)
CORS(app)
attributes = ['User_name', 'Password', 'Start_date', 'End_date', 'Id']
user_file = './user_information.json'
time_period = ['16:00-18:00', '18:00-20:00', '20:00-22:00']

def current_time():
    current_date = datetime.now()
    current_date_list = [current_date.year, current_date.month, current_date.day]
    return current_date_list

def check_time(input_time):
    if input_time < 10:
        return '0'+ str(input_time)
    else:
        return str(input_time)
    
month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
time_list = current_time()

now_time_list = copy.deepcopy(time_list)
for i in range(len(now_time_list)):
    now_time_list[i] = check_time(now_time_list[i])
now_date = '-'.join(now_time_list)

if time_list[2] == 1:
    time_list[1] -= 1
    if time_list[1] == 0:
        time_list[1] = 12
        time_list[0] -= 1
    time_list[2] = month_days[time_list[1]]
else:
    time_list[2] -= 1
for i in range(len(time_list)):
    time_list[i] = check_time(time_list[i])
hh = check_time(random.choice([0,1,6,7,8,9,10,11,12,13,14,15,16]))
mm = check_time(random.randint(0, 59))
ss = check_time(random.randint(0, 59))
previous_date = '-'.join(time_list) + f' {hh}:{mm}:{ss}'

    
class User_operation:
    def __init__(self, data):
        self.information = data
        self.index = 0

    def set_time(self):
        print(f'previous: {self.index}')
        self.index = (self.index + 1) % 3
        print(f'now: {self.index}')

if os.path.exists(user_file):
    with open(user_file, 'r') as in_file:
        users = json.load(in_file)
        users_name = [name['User_name'] for name in users]
        user_dict = {}
        for name in users:
            user_dict[name['User_name']] = User_operation(name)
        print('-'*30 + ' Now User ' + '-'*30)
        for user in users:
            print(user)
        print('-'*30 + '----------' + '-'*30)
else:
    users = []
    users_name = []
    user_dict = {}


@app.route("/new_user", methods=['POST'])
def new_user():
    data = request.get_json()
    print(data)
    user_name, password, student_id = data['username'], data['password'], data['schoolnumber']
    if user_name in users_name:
        print('User exist!')
        return str(0)
    else:
        current_date = current_time()
        user = {
            'User_name': user_name,
            'Password': password,
            'Start_date': current_date,
            'End_date': current_date,
            'Id': student_id
        }
        users.append(user)
        users_name.append(user_name)
        user_dict[user_name] = User_operation(user)
        with open(user_file, 'w') as out_file:
            json.dump(users, out_file)
        print('User sign up done!')
        return str(1)

@app.route("/sign_in", methods=['POST'])
def sign_in():
    data = request.get_json()
    print(data)
    user_name, password, student_id = data['username'], data['password'], data['schoolnumber']
    if user_name not in users_name:
        print('User not exist!')
        return str(0)
    for user in users:
        if user['User_name'] == user_name and user['Password'] == password and user['Id'] == student_id:
            print('User sign in done!')
            break
    return str(1)

@app.route("/remove_user", methods=['POST'])
def remove_user():
    data = request.get_json()
    print(data)
    user_name, password, student_id = data['username'], data['password'], data['schoolnumber']

    if user_name not in users_name:
        print('User not exist!')
        return str(0)
    for user in users:
        if user['User_name'] == user_name and user['Password'] == password and user['Id'] == student_id:
            users.remove(user)
            users_name.remove(user_name)
            user_dict.pop(user_name)
            break
    with open(user_file, 'w') as out_file:
        json.dump(users, out_file)
    print('Remove user done!')
    return str(1)

@app.route("/gethomedata", methods=['POST'])
def gethomedata():
    # print(user_dict)
    data = request.get_json()
    print(data)
    user_name = data['username']
    print(user_name)
    user_operation = user_dict[user_name]
    return jsonify({'data':[now_date, previous_date, time_period[user_operation.index], user_name, user_operation.information['Id']]})

@app.route("/changetimeperiod", methods=['POST'])
def change_time_period():
    data = request.get_json()
    print(data)
    user_name = data['username']
    print(user_name)
    user_operation = user_dict[user_name]
    user_operation.set_time()
    return time_period[user_operation.index]

def print_data():
    print('-'*30 + ' Now User ' + '-'*30)
    for user in users:
        print(user)
    print('-'*30 + '----------' + '-'*30)

if __name__ == '__main__':
    # print_data()
    app.run(debug=True, port=5000,host='0.0.0.0')


