import csv
from pathlib import Path

from django.core.files import File
from django.db.models.signals import post_save

from .models import Analytical_Method


def log_analyticalmethod_to_csv(sender, instance, **kwargs):
    print("I am a signal! I was called because an Analytical method was saved!"))


    with open(file, "a+", newline="") as csvfile:
        logfile= File(csvfile)
        logwriter= csv.writer(
            logfile,
            delimiter = ",",
        )
        logwriter.writerow(
            [
                instance.method_name,
                instance.method_description,
                instance.sample_matrix,
                instance.cost_per_sample,
                instance.date_added,
            ]
        )

    file = Path(__file__).parent.parent / "chromatographyarch" / "domain" / "created_log.csv"
    print(f"Writing to {file}")


# connect the signal to this receiver
post_save.connect(log_analytical_method_to_csv, sender=Analytical_Method)