from django.test import TestCase

from article.models import Article

# Create your tests here.
class ArticleTestCase(TestCase):
    DUMMY_ARTICLE_TITLE = 'Un article créé par test unitaire 😲'
    DUMMY_ARTICLE_CONTENT = 'ALors ca... je ne croyais pas qu\'un jour cela serait possible ! Il est vrai que bon, ce n\'était pas gagné d\'avance mais ils l\'ont fait ! C\'est un vent de "houras" qui plane sur la république, que du bonheur !'

    # On créer un article de base pour effectuer les tests dessus plus bas
    def setUp(self):

        self.articleTestElement = Article()
        self.articleTestElement.title = self.DUMMY_ARTICLE_TITLE
        self.articleTestElement.content = self.DUMMY_ARTICLE_CONTENT
        self.articleTestElement.save()

    # On test que la création d'un article en BDD s'effectue bien
    def test_create_article(self):

        number_of_articles_before_add = Article.objects.count()

        new_article = Article()
        new_article.title = self.DUMMY_ARTICLE_TITLE
        new_article.content = self.DUMMY_ARTICLE_TITLE
        new_article.save()

        number_of_articles_after_add = Article.objects.count()

        self.assertTrue(number_of_articles_after_add == number_of_articles_before_add + 1)

    # On test que la mise à jour de l'article créé dans la fonction 'setUp' s'effectue bien
    def test_update_article(self):

        self.assertEqual(self.articleTestElement.title, self.DUMMY_ARTICLE_TITLE)

        self.articleTestElement.title = 'Changed'
        self.articleTestElement.save()

        tempElement = Article.objects.get(pk=self.articleTestElement.pk)

        self.assertEqual(tempElement.title, 'Changed')

    # On test que la suppression de l'article créé dans la fonction 'setUp' s'effectue bien
    def test_delete_article(self):

        number_of_articles_before_delete = Article.objects.count()

        self.articleTestElement.delete()

        number_of_articles_after_delete = Article.objects.count()

        self.assertTrue(number_of_articles_after_delete == number_of_articles_before_delete -1)


