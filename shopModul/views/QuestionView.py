from rest_framework.generics import CreateAPIView

from shopModul.models import Question
from shopModul.serializers.QuestionSerializers import SerializerQuestion


class QuestionView(CreateAPIView):

    """
    permission->
    url-> "ask-question/" -> name: ask-question
 
    post: создаёт запрос на званок оператора.
    """
    queryset = Question.objects
    serializer_class = SerializerQuestion