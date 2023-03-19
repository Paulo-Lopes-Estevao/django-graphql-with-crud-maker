import graphql_jwt
from graphene import ObjectType, Schema, Field
from graphql_jwt.refresh_token.signals import refresh_token_rotated
from django.dispatch import receiver
from graphql_jwt.relay import JSONWebTokenMutation




from myapp.graphql.schema import Mutation as myappMutation
from myapp.graphql.schema import Query as myappQuery



""" 
from myapp.graphql.query import UserType

class ObtainJSONWebToken(JSONWebTokenMutation):
    user = Field(UserType) 

    @classmethod
    def resolve(cls, root, info, **kwargs):
        return cls(user=info.context.user)

# add fields to the mutation
class Mutation(myappMutation, ObjectType):
    token_auth = ObtainJSONWebToken.Field()
 """     

class Query(myappQuery):
    pass


class Mutation(myappMutation, ObjectType):
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    revoke_token = graphql_jwt.Revoke.Field()

    @receiver(refresh_token_rotated)
    def revoke_refresh_token(sender, request, refresh_token, **kwargs):
        refresh_token.revoke(request)

schema = Schema(query=Query, mutation=Mutation)