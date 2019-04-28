import graphene
import graphql_jwt

import podcasts.schema
import users.schema
import stations.schema

class Query(users.schema.Query, stations.schema.Query, podcasts.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, podcasts.schema.Mutation, stations.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

