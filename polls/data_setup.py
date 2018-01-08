# Not currently working as a script
import django
from django.db.models.query import QuerySet
from polls.models import Question, Choice
from django.utils import timezone

django.setup()
assert isinstance(Question.objects.all(), QuerySet)

for i in range(5):
    question_number = i+1
    q = Question(question_text="Question %s" % question_number, pub_date=timezone.now())
    q.save()
    for j in range(5):
        answer_number = j+1
        q.choice_set.create(choice_text="{}.{}".format(question_number, answer_number))
