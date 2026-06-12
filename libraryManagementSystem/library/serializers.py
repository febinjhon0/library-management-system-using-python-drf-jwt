from rest_framework import serializers
from .models import Author, Book, Borrow


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(
        source='author.name',
        read_only=True
    )

    class Meta:
        model = Book
        fields = '__all__'


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'