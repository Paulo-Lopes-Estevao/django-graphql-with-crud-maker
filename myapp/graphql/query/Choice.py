from graphene_django import DjangoObjectType
from graphene_crud_maker.utils import CustomNode, CustomConnection

from myapp.models import Choice


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice
        filter_fields = {
            'id': ['exact',],
        }
        interfaces = (CustomNode,)
        connection_class = CustomConnection

