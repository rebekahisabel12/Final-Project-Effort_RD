from an_organ.models import Analytical_Method
from django.db import transaction
from chromatographyarch.adapters import repository


class DjangoUnitOfWork:
    def __init__(self):
        self.bookmarks = repository.DjangoRepository()

    def __enter__(self):
        transaction.set_autocommit(False)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            transaction.rollback()
        else:
            transaction.commit()
        transaction.set_autocommit(True)
