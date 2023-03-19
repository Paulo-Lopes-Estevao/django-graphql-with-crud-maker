from graphene_django import DjangoObjectType
from graphene_crud_maker.utils import CustomNode, CustomConnection

from myapp.models import Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
        connection_class = CustomConnection

