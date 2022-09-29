# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:31:59 2022

@author: mikol
"""

import csv
import filters as fl
import pandas as pd


def review_cleaner(source_file, destination_file):
    # This function transform raw scan of opinions from website into clear reviews with present keyword
    
    with open(source_file, 'r', encoding="UTF-8") as RAW_file,\
            open(destination_file, 'w', encoding="UTF-8") as CLEAR_file:

        review_header = ['NumberOfReview', 'Date', 'ReviewWithKEY-WORD', 'TextOfReview']

        review_rows = []
        comments_counter = 0
        keyword_counter = 0
        number_column = {}
        date_column = {}
        keyword_column = {}
        text_column = {}

        for text_line in RAW_file:
            text_line = text_line.lower().replace('\n', '').replace('\t', '').split(' ')
            text_line = fl.stopwords_english(text_line)
            if text_line == '':
                continue
            elif "Posted" in text_line:
                text_line.pop(0)
                for month, month_number in zip(fl.months_dict().keys(), fl.months_dict().values()):
                    if month in text_line[0]:
                        text_line.insert(2, str(month_number))
                        text_line.pop(0)
                        comments_counter += 1
                    elif month in text_line[1]:
                        text_line[1] = str(month_number)
                        comments_counter += 1
                if len(text_line) < 3:
                    text_line.append(2022)
                number_column['NumberOfReview'] = comments_counter
                date_column['Date'] = text_line
            else:
                for keyword in fl.searching_key():
                    if keyword in text_line:
                        keyword_counter += 1
                        text_column['TextOfReview'] = text_line
                        keyword_column['ReviewWithKEY-WORD'] = keyword_counter
                        break
                    else:
                        continue
            try:
                review_rows.append(number_column)
                review_rows.append(date_column)
                review_rows.append(keyword_column)
                review_rows.append(text_column)
            except:
                review_rows.append(number_column)
                review_rows.append(date_column)

        review_writer = csv.DictWriter(CLEAR_file, fieldnames=review_header)

        review_writer.writeheader()

        review_writer.writerows(review_rows)

    return print("Reviews filtered and stored into CSV file. Go & check!")


'''
def visualisation(source_file):
    # This function visualise the output data from previous functions in form of charts | Pandas

    with open(source_file, 'r', encoding="UTF-8") as SOURCE:

        source_of_data = pd.read_csv(SOURCE)

        plot_x_values = source_of_data.Date
        plot_y_values = source_of_data.NumberOfReview

        plt.xlabel('Dates of posting reviews')
        plt.ylabel('Number of reviews')

        chart = plt.plot(plot_x_values, plot_y_values)

    return chart
    '''