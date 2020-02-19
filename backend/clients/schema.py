import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from .models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
    
class Query(graphene.ObjectType):
    clients = graphene.List(ClientType)

    def resolve_clients(self, info):
        return Client.objects.all()

class CreateClient(graphene.Mutation):
    client = graphene.Field(ClientType)

    class Arguments:
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        admin = graphene.Boolean()
        broker_id = graphene.ID()

    def mutate(self, info, name, email, phone):
       user = info.context.user

       if user.is_anonymous:
           raise Exception("Log in to add a client.")

       client = Client(name=name, email=email, phone=phone, brokerID=user)
       client.save()
       return CreateClient(client=client)

class UpdateClient(graphene.Mutation):
    client = graphene.Field(ClientType)

    class Arguments:
        client_id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        phone = graphene.String()
        admin = graphene.Boolean()
        active = graphene.Boolean()
        new_broker = graphene.Int()

    def mutate(self, info, client_id, **kwargs):
        user = info.context.user
        client = Client.objects.get(id=client_id)
        new_broker = kwargs.get("new_broker", None)
        print(kwargs.get("active"))
        if new_broker:
            broker = get_user_model().objects.get(id=new_broker)
        
        if client.brokerID != user and client.admin == False:
            raise Exception("You can only modify your own clients")

        if new_broker and user.is_staff == True:
            broker = get_user_model().objects.get(id=new_broker)
            client.brokerID = broker

        for key, value in kwargs.items():
            setattr(client, key, value)

        client.save()
        return UpdateClient(client=client)

class Mutation(graphene.ObjectType):
    create_client = CreateClient.Field()
    update_client = UpdateClient.Field()