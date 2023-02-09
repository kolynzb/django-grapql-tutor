import graphene

from graphql_auth.schema import UserQuery, MeQuery

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

# from graphene_django import DjangoObjectType
# import graphene

# from accounts.models import UserAccount as UserModel 

# class User(DjangoObjectType):
#     class Meta:
#         model = UserModel

# class Query(graphene.ObjectType):
#     users = graphene.List(User)

#     def resolve_users(self, info):
#         return UserModel.objects.all()

# schema = graphene.Schema(query=Query)