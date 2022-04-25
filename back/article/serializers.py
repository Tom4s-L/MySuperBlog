from turtle import update
from rest_framework import serializers

from article.models import Article


class ArticleSerializer(serializers.ModelSerializer):

    creationDate = serializers.DateField(source='creation_date')
    
    class Meta:
        model = Article
        exclude = ['creation_date']
            