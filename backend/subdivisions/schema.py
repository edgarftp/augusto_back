import graphene
from graphene_django import DjangoObjectType
from graphene_django.forms.mutation import DjangoFormMutation

from backend.inputs import SubdivisionInput
from .models import Subdivision

class SubdivisionType(DjangoObjectType):
    class Meta:
        model = Subdivision

class Query(graphene.ObjectType):
    subdivisions = graphene.List(SubdivisionType)

    def resolve_subdivisions(self, info):
        print(info.context)
        return Subdivision.objects.order_by("id")

class CreateSubdivision(graphene.Mutation):
    subdivision = graphene.Field(SubdivisionType)

    class Arguments:
        name = graphene.String(required=True)
        input = SubdivisionInput(required=True)

    def mutate(self, info, input=None):
        user = info.context.user
        
        if user.is_anonymous or user.is_staff == False:
           raise Exception("Permissions are required for this action.")

        subdivision = Subdivision()
        for key, value in input.items():
                setattr(subdivision, key, value)
        subdivision.save()
        return CreateSubdivision(subdivision=subdivision)

class UpdateSubdivision(graphene.Mutation):
    subdivision = graphene.Field(SubdivisionType)

    class Arguments:
        subdivision_id = graphene.ID(required=True)
        name = graphene.String(default_value="")
        input = SubdivisionInput(required=True)

    def mutate(self, info, name, subdivision_id, input=None):
        user = info.context.user
        subdivision = Subdivision.objects.get(id=subdivision_id)

        if user.is_anonymous or user.is_staff == False:
           raise Exception("Permissions are required for this action.")
        
        if name != "":
            subdivision.name = name

        for key, value in input.items():
            setattr(subdivision, key, value)

        subdivision.save()
        return UpdateSubdivision(subdivision=subdivision)

class DeleteSubdivision(graphene.Mutation):
    subdivision_id = graphene.ID()
    
    class Arguments:
        subdivision_id = graphene.ID(required=True)
    
    def mutate(self, info, subdivision_id):
        user = info.context.user
        subdivision = Subdivision.objects.get(id=subdivision_id)
        
        if user.is_anonymous or user.is_staff == False:
           raise Exception("Permissions are required for this action.")
        
        subdivision.delete()
        return DeleteSubdivision(subdivision_id=subdivision_id)

class Mutation(graphene.ObjectType):
    create_subdivision = CreateSubdivision.Field()
    update_subdivision = UpdateSubdivision.Field()
    delete_subdivision = DeleteSubdivision.Field()