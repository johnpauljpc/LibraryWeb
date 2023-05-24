from django.test import TestCase

from catalog.models import Author

class AuthorModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Author.objects.create(first_name = "Johnpaul", last_name = "Gabriel", date_of_birth = '1998-03-18')
        
    def test_firstNameLabel(self):
        author = Author.objects.get(id=1)
        label = author._meta.get_field('first_name').verbose_name
        print("########   ", label, ': ', author, "  #############")
        self.assertEqual(label, 'first name')

    def test_object_name_is_rendered_as_expected(self):
        author = Author.objects.get(first_name="Johnpaul")
        expects = f'{author.first_name} {author.last_name}'
        print("******************************")
        self.assertEqual(str(author), expects)
        print("-###########################")

    def test_first_name_max_length(self):
        author = Author.objects.get(id=1)
        getLength = author._meta.get_field('first_name').max_length
        print(f"$$$$$$$   {getLength}   $$$$$$$$")
        self.assertTrue(getLength == 100)

    def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1/')