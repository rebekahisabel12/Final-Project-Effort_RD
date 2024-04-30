from .models import Analytical_Method


class AnalyticalMethodRepository:
    def create_method(self, method_name, method_description, sample_matrix, cost_per_sample):
        return Analytical_Method.objects.create(
            method_name=method_name,
            method_description=method_description,
            sample_matrix=sample_matrix,
            cost_per_sample=cost_per_sample
        )

    def get_method_by_id(self, method_id):
        return Analytical_Method.objects.get(pk=method_id)

    def update_method(self, method_id, **kwargs):
        method = Analytical_Method.objects.get(pk=method_id)
        for key, value in kwargs.items():
            setattr(method, key, value)
        method.save()

    def delete_method(self, method_id):
        Analytical_Method.objects.filter(pk=method_id).delete()
