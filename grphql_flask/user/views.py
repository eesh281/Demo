from database import init_db
from flask import Flask
from flask_graphql import GraphQLView
from schema import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    init_db()
    app.run()


# from flask import Flask
# from flask_graphql import GraphQLView
# from schema import schema
# from models import UserInfo
# from mongoengine import connect
# from flask import jsonify

# connect('gursheesh', host='localhost:27017', alias='default')
# app = Flask(__name__)

# # app.add_url_rule(                               
# #     '/graphql',
# #     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
# # )
# @app.route('/post',methods=['POST'])
# def user_post():
#     import ipdb; ipdb.set_trace()
#     # view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
#     user_obj = UserInfo(name='eesh',email='kour.gursheesh281@gmail.com',number='9149746060')
#     user_obj.save()
#     user_dict = {}
#     user_dict['name'] = user_obj.name
#     user_dict['email'] = user_obj.email
#     user_dict['number'] = user_obj.number

#     return jsonify(user_dict)


# if __name__ == '__main__':
#     # init_db()
#     app.run()