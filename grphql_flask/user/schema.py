import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import UserInfo


class User(MongoengineObjectType):

    class Meta:
        model = UserInfo
        interfaces = (Node,)


class Query(graphene.ObjectType):
    node = Node.Field()
    all_users = MongoengineConnectionField(User)


schema = graphene.Schema(query=Query, types=[User])
