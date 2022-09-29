import os
import csv
import filters as fl

def unigram_counter(source_file, destination_file):
    # This function counts unigrams in TXT files

    # Below I open file with raw text from website to read
    # and I create/open a text file to write into
    with open(source_file, 'r', encoding='UTF-8') as clear_review,\
            open(destination_file, 'w', encoding='UTF-8') as unigrams:

        # This is the dictionary where I store words and their counters
        unigram_dictionary = {}

        # That loop reads every line of raw text file and transform it into a list.
        # That indexes of this list are therefore iterated and stored into a dictionary I mentioned at the beginning.
        for line in clear_review:
            words_of_line = line.replace('\n', '').replace('\t', '').split(' ')
            for word in words_of_line:
                if word == '':
                    continue
                elif word in unigram_dictionary:
                    unigram_dictionary[word] += 1
                else:
                    unigram_dictionary[word] = 1

        # It sorts dictionary in order of VALUES, transforming it into list
        unigram_list = sorted(unigram_dictionary.items(), key=lambda x: x[1], reverse=True)

        #Here I order the program to write into CSV file
        uni_writer = csv.writer(unigrams)

        #Here I create first row to be saved in CSV file
        header = ["unigram", "number"]

        #Here I write a row into CSV file
        uni_writer.writerow(header)

        # Here I write next rows
        uni_writer.writerows(unigram_list)

    return print("Operation's done.")

def xo_bigram_counter(source_file, destination_file):
    # This function counts BIGRAMS in REVIEW in form: 'KEY-WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV,\
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        bigrams_next = {}

        for line in REV:
            line_list = line.lower().replace("\n", " ").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if index < len(line_list) - 1:
                            bigram = ngram + ' ' + line_list[index + 1]
                            if bigram in bigrams_next:
                                bigrams_next[bigram] += 1
                            else:
                                bigrams_next[bigram] = 1

        bigrams_next = sorted(bigrams_next.items(), key=lambda x: x[1], reverse=True)

        bigram_writer = csv.writer(NGRAM)

        header = ['bigram','number']

        bigram_writer.writerow(header)

        bigram_writer.writerows(bigrams_next)

    return print("Bigrams counted and stored into CSV file.")


def ox_bigram_counter(source_file, destination_file):
    # This function counts BIGRAMS in REVIEW file in form: 'WORD', 'KEY-WORD'

    with open(source_file, "r", encoding="UTF-8") as REV,\
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        bigrams_previous = {}

        for enil in REV:
            enil = enil.lower()
            enil = enil.replace("\n", " ")
            enil_tsil = enil.split(' ')
            for xedni, margn in enumerate(enil_tsil):
                for key in fl.searching_key():
                    if key in margn:
                        if xedni > 0:
                            bigram_previous = enil_tsil[xedni - 1] + ' ' + margn
                            if bigram_previous in bigrams_previous:
                                bigrams_previous[bigram_previous] += 1
                            else:
                                bigrams_previous[bigram_previous] = 1
                        else:
                            continue

        bigrams_previous = sorted(bigrams_previous.items(), key=lambda x: x[1], reverse=True)

        bigram_writer = csv.writer(NGRAM)

        header = ['bigram', 'number']

        bigram_writer.writerow(header)

        bigram_writer.writerows(bigrams_previous)

    return print("Bigrams counted and stored into CSV file.")

def oox_trigrams_counter(source_file, destination_file):
    # This function counts TRIGRAMS in REVIEW in form: 'WORD', 'WORD', 'KEY-WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        oox_trigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if (index > 1) and (index < len(line_list)):
                            trigram = line_list[index - 2] + ' ' + line_list[index - 1] + ' ' + ngram
                            if trigram in oox_trigrams:
                                oox_trigrams[trigram] += 1
                            else:
                                oox_trigrams[trigram] = 1

        oox_trigrams = sorted(oox_trigrams.items(), key=lambda x: x[1], reverse=True)

        trigram_writer = csv.writer(NGRAM)

        header = ['trigram', 'number']

        trigram_writer.writerow(header)

        trigram_writer.writerows(oox_trigrams)

    return print("Trigrams counted and stored into CSV file.")

def oxo_trigrams_counter(source_file, destination_file):
    # This function counts TRIGRAMS in REVIEW in form: 'WORD', 'KEY-WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        oxo_trigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if (index < len(line_list) - 1) and (index > 0):
                            trigram = line_list[index - 1] + ' ' + ngram + ' ' + line_list[index + 1]
                            if trigram in oxo_trigrams:
                                oxo_trigrams[trigram] += 1
                            else:
                                oxo_trigrams[trigram] = 1

        oxo_trigrams = sorted(oxo_trigrams.items(), key=lambda x: x[1], reverse=True)

        trigram_writer = csv.writer(NGRAM)

        header = ['trigram', 'number']

        trigram_writer.writerow(header)

        trigram_writer.writerows(oxo_trigrams)

    return print("Trigrams counted and stored into CSV file.")

def xoo_trigrams_counter(source_file, destination_file):
    # This function counts TRIGRAMS in REVIEW in form: 'KEY-WORD', 'WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        xoo_trigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if index < len(line_list) - 2:
                            trigram = ngram + ' ' + line_list[index + 1] + ' ' + line_list[index + 2]
                            if trigram in xoo_trigrams:
                                xoo_trigrams[trigram] += 1
                            else:
                                xoo_trigrams[trigram] = 1

        xoo_trigrams = sorted(xoo_trigrams.items(), key=lambda x: x[1], reverse=True)

        trigram_writer = csv.writer(NGRAM)

        header = ['trigram', 'number']

        trigram_writer.writerow(header)

        trigram_writer.writerows(xoo_trigrams)

    return print("Trigrams counted and stored into CSV file.")


def xooo_quadrigrams_counter(source_file, destination_file):
    # This function counts QUADRIGRAMS form REVIEW in form: 'KEY-WORD' 'WORD', 'WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        xooo_quadrigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if index < len(line_list) - 3:
                            quadrigram = ngram + ' ' + line_list[index + 1] + ' ' + line_list[index + 2] + ' ' + line_list[index + 3]
                            if quadrigram in xooo_quadrigrams:
                                xooo_quadrigrams[quadrigram] += 1
                            else:
                                xooo_quadrigrams[quadrigram] = 1

        xooo_quadrigrams = sorted(xooo_quadrigrams.items(), key=lambda x: x[1], reverse=True)

        quadrigram_writer = csv.writer(NGRAM)

        header = ['quadrigram', 'number']

        quadrigram_writer.writerow(header)

        quadrigram_writer.writerows(xooo_quadrigrams)

    return print("Quadrigrams counted and stored into CSV file.")

def oxoo_quadrigrams_counter(source_file, destination_file):
    # This function counts QUADRIGRAMS from REVIEW in form: 'WORD', 'KEY-WORD', 'WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        oxoo_quadrigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if (index > 0) and (index < len(line_list) - 2):
                            quadrigram = line_list[index - 1] + ' ' + ngram + ' ' +line_list[index + 1] + ' ' + line_list[index + 2]
                            if quadrigram in oxoo_quadrigrams:
                                oxoo_quadrigrams[quadrigram] += 1
                            else:
                                oxoo_quadrigrams[quadrigram] = 1

        oxoo_quadrigrams = sorted(oxoo_quadrigrams.items(), key=lambda x: x[1], reverse=True)

        quadrigram_writer = csv.writer(NGRAM)

        header = ['quadrigram', 'number']

        quadrigram_writer.writerow(header)

        quadrigram_writer.writerows(oxoo_quadrigrams)

    return print("Quadrigrams counted and stored into CSV file.")

def ooxo_quadrigrams_counter(source_file, destination_file):
    # This function counts QUADRIGRAMS form REVIEW in form: 'WORD', 'WORD', 'KEY-WORD', 'WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        ooxo_quadrigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if (index > 1) and (index < len(line_list) - 1):
                            quadrigram = line_list[index - 2] + ' ' + line_list[index - 1] + ' ' + ngram + ' ' +line_list[index + 1]
                            if quadrigram in ooxo_quadrigrams:
                                ooxo_quadrigrams[quadrigram] += 1
                            else:
                                ooxo_quadrigrams[quadrigram] = 1

        ooxo_quadrigrams = sorted(ooxo_quadrigrams.items(), key=lambda x: x[1], reverse=True)

        quadrigram_writer = csv.writer(NGRAM)

        header = ['quadrigram', 'number']

        quadrigram_writer.writerow(header)

        quadrigram_writer.writerows(ooxo_quadrigrams)

    return print("Quadrigrams counted and stored into CSV file.")


def ooox_quadrigrams_counter(source_file, destination_file):
    # This function counts QUADRIGRAMS from REVIEW in form: 'WORD', 'WORD', 'WORD', 'KEY-WORD'

    with open(source_file, "r", encoding="UTF-8") as REV, \
            open(destination_file, "w", encoding="UTF-8") as NGRAM:

        ooox_quadrigrams = {}

        for line in REV:
            line_list = line.lower().replace("\n", "").split(' ')
            for index, ngram in enumerate(line_list):
                for key in fl.searching_key():
                    if key in ngram:
                        if (index > 2) and (index < len(line_list)):
                            quadrigram = line_list[index - 3] + ' ' + line_list[index - 2] + ' ' + line_list[index - 1] + ' ' + ngram
                            if quadrigram in ooox_quadrigrams:
                                ooox_quadrigrams[quadrigram] += 1
                            else:
                                ooox_quadrigrams[quadrigram] = 1

        ooox_quadrigrams = sorted(ooox_quadrigrams.items(), key=lambda x: x[1], reverse=True)

        quadrigram_writer = csv.writer(NGRAM)

        header = ['quadrigram', 'number']

        quadrigram_writer.writerow(header)

        quadrigram_writer.writerows(ooox_quadrigrams)

    return print("Quadrigrams counted and stored into CSV file.")