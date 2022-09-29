import steamreviews as sr
import pandas as pd


with open("reviews_file.txt", "w") as rev:
    content = sr.download_reviews_for_app_id_batch()
    rev.write(content)

