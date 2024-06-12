from rest_framework import serializers

from shopModul.models import News, Paragraph
from shopModul.serializers.FeedbackSerializers import SerializerFeedback_score
from shopModul.serializers.ImgLinkSerializers import SerializerImageLink
from shopModul.serializers.ParagraphSerializers import SerializerParagraphs


class SerializerNews(serializers.ModelSerializer):

    feedback = SerializerFeedback_score(many=True)


    def to_representation(self, instance):
        row_result = super().to_representation(instance)
        avg_score = [score['score'] for score in row_result.get('feedback')]

        if  len(avg_score) > 0 :
            row_result['avg_score'] = int(sum(avg_score) / len(avg_score)/2)
        else:
            row_result['avg_score'] = 0

        return row_result
    class Meta:
        model = News
        fields = ['id', 'title', 'author', 'date', 'feedback', 'img']
class SerializerNewsItemFull(serializers.ModelSerializer):
    def to_representation(self, instance):
        raw_result = super().to_representation(instance)
        raw_Paragraphs = Paragraph.objects.all().filter(news_id=raw_result['id'])
        raw_result['paragraphs'] = SerializerParagraphs(raw_Paragraphs, many=True).data
        return raw_result

    class Meta:
        model = News
        fields = '__all__'
