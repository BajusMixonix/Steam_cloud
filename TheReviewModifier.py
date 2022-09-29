# -*- coding: utf-8 -*-
"""
Created on Tue May 17 14:03:48 2022

@author: mikol
"""
import os
import review_cleaner as rc
import Ngrams as ngram

paths = {
         'path_raw_reviews': r'revs\raw_reviews',
         'path_clean_reviews': r'revs\clean_reviews',
                }

ngrams_paths = {
         'path_unigrams': r'ngrams\unigrams',
         'path_bigrams': r'ngrams\bigrams',
         'path_trigrams': r'ngrams\trigrams',
         'path_quadrigrams': r'ngrams\quadrigrams',
                }

# Below: REVIEW selector
for review_file in os.listdir(paths['path_raw_reviews']):

    source_file = os.path.join(paths['path_raw_reviews'], review_file)

    destination_file = os.path.join(paths['path_clean_reviews'], "clean_" + review_file[:-4] + '.csv')

    rc.review_cleaner(source_file, destination_file)


# Below: UNIGRAMS counter on cleared reviews
for clean_file in os.listdir(paths['path_clean_reviews']):

    source_file = os.path.join(paths['path_clean_reviews'], clean_file)

    destination_file = os.path.join(ngrams_paths['path_unigrams'], "UNIgram_" + clean_file[:-4] + '.csv')

    ngram.unigram_counter(source_file, destination_file)


# Below: BIGRAMS counter on cleared reviews
for clean_file in os.listdir(paths['path_clean_reviews']):

    source_file = os.path.join(paths['path_clean_reviews'], clean_file)

    destination_file_1 = os.path.join(ngrams_paths['path_bigrams'], "xo_BIgram_" + clean_file[:-4] + '.csv')
    destination_file_2 = os.path.join(ngrams_paths['path_bigrams'], "ox_BIgram_" + clean_file[:-4] + '.csv')

    ngram.xo_bigram_counter(source_file, destination_file_1)
    ngram.ox_bigram_counter(source_file, destination_file_2)


# Below: TRIGRAMS counter on cleared reviews
for clean_file in os.listdir(paths['path_clean_reviews']):

    source_file = os.path.join(paths['path_clean_reviews'], clean_file)

    destination_file_1 = os.path.join(ngrams_paths['path_trigrams'], "xoo_TRIgram_" + clean_file[:-4] + '.csv')
    destination_file_2 = os.path.join(ngrams_paths['path_trigrams'], "oxo_TRIgram_" + clean_file[:-4] + '.csv')
    destination_file_3 = os.path.join(ngrams_paths['path_trigrams'], "oox_TRIgram_" + clean_file[:-4] + '.csv')

    ngram.xoo_trigrams_counter(source_file, destination_file_1)
    ngram.oxo_trigrams_counter(source_file, destination_file_2)
    ngram.oox_trigrams_counter(source_file, destination_file_3)


# Below: QUADRIGRAMS counter on cleared reviews
for clean_file in os.listdir(paths['path_clean_reviews']):

    source_file = os.path.join(paths['path_clean_reviews'], clean_file)

    destination_file_1 = os.path.join(ngrams_paths['path_quadrigrams'], "xooo_QUADRIgram_" + clean_file[:-4] + '.csv')
    destination_file_2 = os.path.join(ngrams_paths['path_quadrigrams'], "oxoo_QUADRIgram_" + clean_file[:-4] + '.csv')
    destination_file_3 = os.path.join(ngrams_paths['path_quadrigrams'], "ooxo_QUADRIgram_" + clean_file[:-4] + '.csv')
    destination_file_4 = os.path.join(ngrams_paths['path_quadrigrams'], "ooox_QUADRIgram_" + clean_file[:-4] + '.csv')

    ngram.xooo_quadrigrams_counter(source_file, destination_file_1)
    ngram.oxoo_quadrigrams_counter(source_file, destination_file_2)
    ngram.ooxo_quadrigrams_counter(source_file, destination_file_3)
    ngram.ooox_quadrigrams_counter(source_file, destination_file_4)


'''
# Below: visualisation function
for AC_file, HOMM_file in zip(os.listdir(paths['path_AC_clearReviews']),
                              os.listdir(paths['path_HOMM_clearReviews'])):

    source_file_1 = os.path.join(paths['path_AC_clearReviews'], AC_file)
    source_file_2 = os.path.join(paths['path_HOMM_clearReviews'], HOMM_file)

    rc.visualisation(source_file_1)
    rc.visualisation(source_file_2)
'''
