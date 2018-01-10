# Not currently working as a script
from django.db.models.query import QuerySet
from polls.models import Question
from django.utils import timezone
from faker import Faker

faker = Faker()

assert isinstance(Question.objects.all(), QuerySet)

outer_count = 0
while outer_count < 10:
    q = Question(question_text=faker.bs() + "?", pub_date=timezone.now())
    q.save()
    print("OUTER Q= " + str(q.id))
    print("OUTER COUNT: " + str(outer_count))
    inner_count = 0
    while inner_count < 3:
        print("INNER Q= " + str(q.id))
        print("INNER COUNT: " + str(inner_count))
        q.choice_set.create(choice_text=faker.bs() + "!", votes=0)
        inner_count = inner_count + 1
    outer_count = outer_count + 1


