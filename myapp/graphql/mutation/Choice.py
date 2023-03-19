from graphene import Field
from graphene import ID, Mutation, List
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_crud_maker.utils import CustomModelForm

from myapp.models import Choice
from myapp.graphql.query import ChoiceType


class ChoiceForm(CustomModelForm):
    class Meta:
        model = Choice
        exclude = []


class ChoiceMutation(DjangoModelFormMutation):
    class Meta:
        form_class = ChoiceForm

    data = Field(ChoiceType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return ChoiceMutation(data=data)
        except Exception as ex:
            raise ex



class RemoveChoice(Mutation):
    class Arguments:
        ids = List(ID)

    class Meta:
        output = List(ChoiceType)

    def mutate(self, info, **kwargs):
        deleted_items = []
        for item in Choice.objects.filter(pk__in=kwargs['ids']):
            item.delete()
            deleted_items.append(item)
        return deleted_items

