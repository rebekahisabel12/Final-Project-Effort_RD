from an_organ.models import Analytical_Method


class DjangoRepository:
    def add(self, method: Analytical_Method) -> None:
        method.save()
