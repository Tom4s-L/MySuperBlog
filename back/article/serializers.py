from turtle import update
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    updateDate = serializers.DateField(source='update_date')
    
    class Meta:
        model = Article
        exclude = ['update_date']
            