# src/utils.py

import os


def create_directories():

    folders = [
        "outputs/charts",
        "outputs/reports",
        "outputs/csv"
    ]

    for folder in folders:

        os.makedirs(folder, exist_ok=True)