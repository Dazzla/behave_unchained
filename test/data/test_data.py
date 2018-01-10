from polls.models import Question
from django.utils import timezone
from faker import Faker
from 


faker = Faker()

outer_count = 1
while outer_count < 10:
    q = Question(r"{question_text=faker.bs()}?", pub_date=timezone.now())
    q.save()

    inner_count = 1

    while inner_count < 3:
        q.choice_set.create(choice_text=faker.bs(), votes=0)
