import graphene


class SubdivisionInput(graphene.InputObjectType):

    num_lots = graphene.Int(default_value=0)
    private = graphene.Boolean(default_value=False)
    club_house = graphene.Boolean(default_value=False)
    amenities = graphene.Boolean(default_value=False)
    park = graphene.Boolean(default_value=False)
    active = graphene.Boolean(default_value=True)



