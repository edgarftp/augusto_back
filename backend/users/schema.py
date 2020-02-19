from django.contrib.auth import get_user_model

import graphene
from graphene_django import DjangoObjectType

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.ID (required=True))
    me = graphene.Field(UserType)

    def resolve_user(self, info, id):
        return get_user_model().objects.get(id=id)

    def resolve_me(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Not logged in")
        return user

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        is_staff = graphene.Boolean(default_value=False)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate (self, info, username, password, email, first_name, last_name, is_staff):
        user = get_user_model()(
            username=username,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            email=email,
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
