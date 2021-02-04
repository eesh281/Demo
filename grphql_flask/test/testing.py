from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/api/ping/<tag>/', methods=["GET"])
def api_ping_data(tag):

    data_object = requests.get(' https://api.hatchways.io/assessment/blog/posts?tag='+str(tag)).json()
    return jsonify({"success":True,'data':data_object})


def quickSort(arr,sortBy):
    less = []
    final_list = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        value_ = arr[0][sortBy]
        for i in arr:
            if i[sortBy] < value_:
                less.append(i)
            elif i[sortBy] > value_:
                more.append(i)
            else:
                final_list.append(i)
        less = quickSort(less,sortBy)
        more = quickSort(more,sortBy)
        return less + final_list + more
 

@app.route('/api/posts/<tag>/<sortBy>/<direction>/', methods=["GET"])
def api_posts_data(tag,sortBy,direction):

    data_object = requests.get(' https://api.hatchways.io/assessment/blog/posts?tag='+str(tag)).json()

    posts_list = data_object['posts']

    data_list = quickSort(posts_list,sortBy)

    if direction == 'asc':
        return jsonify({"success":True,'data':data_list})
    else:
        data_list.reverse()
        print(data_list)
        
        return jsonify({"success":True,'data':data_list})



