from datetime import datetime
from faker import Faker
import factory
from model_bakery import baker

from apps.oauth.models import AuthUser
from apps.support.models.ticket import Ticket
from apps.support.models.answer import Answer
from config import settings

fake = Faker()


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    title = factory.Sequence(lambda n: 'ticket%d' % n)
    text = fake.text()
    screenshot = factory.django.ImageField()
    create_at = factory.LazyFunction(datetime.now)

# # TicketFactory()  # --> One instance
# # TicketFactory.create_batch(3)
# # TicketFactory.build()  # --> One instance
# # TicketFactory.build_batch()  # --> Batch of 3 instances
#
# # create and save to the database
# # baker.make(MyModel) # --> One instance
# # baker.make(MyModel, _quantity=3) # --> Batch of 3 instances
# #
# # # create and don't save
# # baker.prepare(MyModel) # --> One instance
# # baker.prepare(MyModel, _quantity=3) # --> Batch of 3 instances
