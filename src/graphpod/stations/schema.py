import graphene
from graphene_django import DjangoObjectType
from .models import Station

class StationType(DjangoObjectType):
    class Meta:
        model = Station

class Query(graphene.ObjectType):
    stations = graphene.List(StationType)

    def resolve_stations(self, info, **kwargs):
        return Station.objects.all()

class UpdateStation(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()
    description = graphene.String()
    followers = graphene.Int()
    active = graphene.Boolean()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()
        url = graphene.String()
        name = graphene.String()
        description = graphene.String()
        followers = graphene.Int()
        active = graphene.Boolean()

    def mutate(self, info, id, url, name, description, followers, active):

        station = Station.objects.filter(id=id).first()

        if not station:
            raise Exception("Station not Found!")

        station.url = url
        station.name = name
        station.description = description
        station.followers = followers
        station.active = active
        station.save()

        return UpdateStation(
            ok=True,
            id=station.id,
            url=station.url,
            name=station.name,
            description=station.description,
            followers=station.followers,
            active=station.active
        )

class DeleteStation(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):

        station = Station.objects.filter(id=id).first()

        if not station:
            raise Exception("No Station Found")

        station.delete()

        return DeleteStation(
            id=id,
            ok=True
        )


class CreateStation(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    name = graphene.String()
    description = graphene.String()
    followers = graphene.Int()
    active = graphene.Boolean()

    class Arguments:
        url = graphene.String()
        name = graphene.String()
        description = graphene.String()
        followers = graphene.Int()
        active = graphene.Boolean()


    def mutate(self, info, url, name, description, followers, active):
        station = Station(
            url=url,
            name=name,
            description=description,
            followers=followers,
            active=active
        )

        station.save()

        return CreateStation(
            id=station.id,
            url=station.url,
            name=station.name,
            description=station.description,
            followers=station.followers,
            active=station.active
        )

class Mutation(graphene.ObjectType):
    create_station = CreateStation.Field()
    update_station = UpdateStation.Field()
    delete_station = DeleteStation.Field()
