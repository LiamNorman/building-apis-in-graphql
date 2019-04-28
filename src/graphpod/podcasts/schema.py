import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from django.db.models import Q
from .models import Podcast, Favourite


class PodcastType(DjangoObjectType):
    class Meta:
        model = Podcast


class FavouritePodcastType(DjangoObjectType):
    class Meta:
        model = Favourite

class FavouritePodcast(graphene.Mutation):
    user = graphene.Field(UserType)
    podcast = graphene.Field(PodcastType)

    class Arguments:
        podcast_id = graphene.Int()

    def mutate(self, info, podcast_id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('You must be logged in to Favourite!')

        podcast = Podcast.objects.filter(id=podcast_id).first()
        if not podcast:
            raise Exception('Invalid Podcast!')

        Favourite.objects.create(
            user=user,
            podcast=podcast
        )

        return FavouritePodcast(user=user, podcast=podcast)


class Query(graphene.ObjectType):
    podcasts = graphene.List(PodcastType,
                             search=graphene.String(),
                             first=graphene.Int(),
                             skip=graphene.Int(),
                             )
    favourites = graphene.List(FavouritePodcastType)

    def resolve_favourites(self, info, **kwargs):
        return Favourite.objects.all()

    def resolve_podcasts(self,
                         info,
                         search=None,
                         first=None,
                         skip=None,
                         **kwargs):

        podcasts = Podcast.objects.all()
        if search:
            filter = (
                    Q(url__icontains=search) |
                    Q(description__icontains=search)
            )
            podcasts = podcasts.filter(filter)

        if skip:
            podcasts = podcasts[skip:]

        if first:
            podcasts = podcasts[:first]

        return podcasts

class DeletePodcast(graphene.Mutation):
    id = graphene.Int()
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):

        podcast = Podcast.objects.filter(id=id).first()

        if not podcast:
            raise Exception("No Podcast Found")

        podcast.delete()

        return DeletePodcast(
            ok=True
        )

class CreatePodcast(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user or None
        podcast = Podcast(
            url=url,
            description=description,
            posted_by=user,
        )
        podcast.save()

        return CreatePodcast(
            id=podcast.id,
            url=podcast.url,
            description=podcast.description,
            posted_by=podcast.posted_by,
        )

class Mutation(graphene.ObjectType):
    create_podcast = CreatePodcast.Field()
    favourite_podcast = FavouritePodcast.Field()
    delete_podcast = DeletePodcast.Field()