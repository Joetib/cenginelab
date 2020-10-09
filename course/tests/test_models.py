from django.test import TestCase
from ..models import User, Episode, EpisodeComment, Course
from django.utils.text import slugify

# Create your tests here.


class BaseTestDataSetup:
    """Base Test Class To setup test data"""

    def setUpdata(self):
        self.user = User.objects.create(
            username="someusername",
            password="somerandompassword",
            email="someemail@gmail.com",
        )
        self.course = Course.objects.create(
            created_by=self.user,
            title="title",
            description="some description",
            picture="/media/some_picture.jpg",
        )


# -----------------------------------------
#       TEST CASES
# -----------------------------------------


class CourseTest(BaseTestDataSetup, TestCase):
    def setUp(self) -> None:
        super().setUpdata()

    def test_course_data(self):
        tests = [
            {
                "created_by": self.user,
                "title": "title",
                "description": "some description",
                "picture": "/media/some_picture.jpg",
            },
        ]
        for test in tests:
            course = Course.objects.create(**test)
            self.assertEqual(course.title, test["title"])
            self.assertEqual(course.description, test["description"])
            self.assertEqual(course.picture, test["picture"])
            self.assertEqual(course.slug, slugify(test["title"]))
