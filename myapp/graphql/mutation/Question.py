from graphene import Field
from graphene import ID, Mutation, List
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_crud_maker.utils import CustomModelForm

from myapp.models import Question
from myapp.graphql.query import QuestionType


class QuestionForm(CustomModelForm):
    class Meta:
        model = Question
        exclude = []


class QuestionMutation(DjangoModelFormMutation):
    class Meta:
        form_class = QuestionForm

    data = Field(QuestionType)

    def perform_mutate(form, info):
        try:
            data = form.save()
            return QuestionMutation(data=data)
        except Exception as ex:
            raise ex



class RemoveQuestion(Mutation):
    class Arguments:
        ids = List(ID)

    class Meta:
        output = List(QuestionType)

    def mutate(self, info, **kwargs):
        deleted_items = []
        for item in Question.objects.filter(pk__in=kwargs['ids']):
            item.delete()
            deleted_items.append(item)
        return deleted_items

