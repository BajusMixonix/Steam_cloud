import csv


def months_dict():
    # This function cals 'months_dict' dictionary.

    months_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7,
                   'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    return months_dict


def searching_key():
    # This function calls 'searching_key' list.

    searching_key = ['acousmatic sound', 'acoustic', 'adaptive audio', 'adaptive music',
                     'adaptive dialogue', 'ambience', 'ambient', 'audio', 'auditory',
                     'auditorial', 'background', 'beat', 'bpm', 'composer', 'compressor',
                     'dialogue', 'diegetic sound', 'dynamic audio', 'echo', 'foley',
                     'harmony', 'harmonic', 'hear', 'hertz', 'interactive audio', 'interactive music',
                     'localisation',
                     'melody', 'melodic', 'music', 'noise', ' ost', 'pitch shift', 'rhythm', 'rhythmic',
                     'sfx', 'sonority', 'sonic', 'sonic environment', 'sound', 'sound design',
                     'soundscape', 'sound effect', 'speech', 'spoken word', 'theme', ' tone', 'track',
                     'tune', 'verbal', 'voice', 'voice over']

    return searching_key


def stopwords_english(text_list):
    # This function calls the english stopwords list

    stopwords_english = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves",
                         "you", "your", "yours", "yourself", "yourselves", "he", "him",
                         "his", "himself", "she", "her", "hers", "herself", "it", "its",
                         "itself", "they", "them", "their", "theirs", "themselves", "what",
                         "which", "who", "whom", "this", "that", "these", "those", "am", "is",
                         "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
                         "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because",
                         "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
                         "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down",
                         "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there",
                         "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
                         "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s",
                         "t", "can", "will", "just", "don", "should", "now"]

    new_text_list = []

    for phrase in text_list:
        if phrase not in stopwords_english:
            new_text_list.append(phrase)

    return new_text_list


def searching_key_dictionary():
    
    searching_key_dictionary = [
        
        {'Family': 'Sound family', 'Phrase': 'acousmatic sound', 'Phrase number': 1},
        {'Family': 'Sound family', 'Phrase': 'diegetic sound', 'Phrase number': 2},
        {'Family': 'Sound family', 'Phrase': 'dynamic sound', 'Phrase number': 3},
        {'Family': 'Sound family', 'Phrase': 'sonic', 'Phrase number': 4},
        {'Family': 'Sound family', 'Phrase': 'sonic enviornment', 'Phrase number': 5},
        {'Family': 'Sound family', 'Phrase': 'sound', 'Phrase number': 6},
        {'Family': 'Sound family', 'Phrase': 'sound design', 'Phrase number': 7},
        {'Family': 'Sound family', 'Phrase': 'soundscape', 'Phrase number': 8},
        {'Family': 'Sound family', 'Phrase': 'soundtrack', 'Phrase number': 9},
        {'Family': 'Audio family', 'Phrase': 'audio', 'Phrase number': 10},
        {'Family': 'Audio family', 'Phrase': 'auditory', 'Phrase number': 11},
        {'Family': 'Audio family', 'Phrase': 'auditorial', 'Phrase number': 12},
        {'Family': 'Audio family', 'Phrase': 'interactive audio', 'Phrase number': 13},
        {'Family': 'Audio family', 'Phrase': 'audio design', 'Phrase number': 14},
        {'Family': 'Audio family', 'Phrase': 'audio spectrum', 'Phrase number': 15},
        {'Family': 'Audio family', 'Phrase': 'audio space', 'Phrase number': 16},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'ambience', 'Phrase number': 17},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'ambient', 'Phrase number': 18},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'background', 'Phrase number': 19},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'bg', 'Phrase number': 20},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'dialogue', 'Phrase number': 21},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'dx', 'Phrase number': 22},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'foley', 'Phrase number': 23},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'fol', 'Phrase number': 24},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'music', 'Phrase number': 25},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'mx', 'Phrase number': 26},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'sound effect', 'Phrase number': 27},
        {'Family': 'Michael Cullen sound families', 'Phrase': 'sfx', 'Phrase number': 28},
        {'Family': 'Verbum family', 'Phrase': 'adaptive dialogue', 'Phrase number': 29},
        {'Family': 'Verbum family', 'Phrase': 'localisation', 'Phrase number': 30},
        {'Family': 'Verbum family', 'Phrase': 'speech', 'Phrase number': 31},
        {'Family': 'Verbum family', 'Phrase': 'spoken word', 'Phrase number': 32},
        {'Family': 'Verbum family', 'Phrase': 'verbal', 'Phrase number': 33},
        {'Family': 'Verbum family', 'Phrase': 'verbum', 'Phrase number': 34},
        {'Family': 'Verbum family', 'Phrase': 'voice', 'Phrase number': 35},
        {'Family': 'Verbum family', 'Phrase': 'voice acting', 'Phrase number': 36},
        {'Family': 'Verbum family', 'Phrase': 'voice over', 'Phrase number': 37},
        {'Family': 'Music theory family', 'Phrase': 'compose', 'Phrase number': 38},
        {'Family': 'Music theory family', 'Phrase': 'melody', 'Phrase number': 39},
        {'Family': 'Music theory family', 'Phrase': 'harmony', 'Phrase number': 40},
        {'Family': 'Music theory family', 'Phrase': 'harmonic', 'Phrase number': 41},
        {'Family': 'Music theory family', 'Phrase': 'rhythym', 'Phrase number': 42},
        {'Family': 'Music theory family', 'Phrase': 'rhythmic', 'Phrase number': 43},
        {'Family': 'Music theory family', 'Phrase': 'theme', 'Phrase number': 44},
        {'Family': 'Music theory family', 'Phrase': 'musical phrase', 'Phrase number': 45},
        {'Family': 'Music theory family', 'Phrase': 'leitmotiff', 'Phrase number': 46},
        {'Family': 'Music theory family', 'Phrase': ' tone', 'Phrase number': 47},
        {'Family': 'Music theory family', 'Phrase': 'semitone', 'Phrase number': 48},
        {'Family': 'Music theory family', 'Phrase': 'tempo', 'Phrase number': 49},
        {'Family': 'Music theory family', 'Phrase': 'key signature', 'Phrase number': 50},
        {'Family': 'Music theory family', 'Phrase': ' bar', 'Phrase number': 51},
        {'Family': 'Music theory family', 'Phrase': 'note', 'Phrase number': 52},
        {'Family': 'Music theory family', 'Phrase': 'instrument', 'Phrase number': 53},
        {'Family': 'Music theory family', 'Phrase': 'music form', 'Phrase number': 54},
        {'Family': 'Pragmatic terms family', 'Phrase': ' beat', 'Phrase number': 55},
        {'Family': 'Pragmatic terms family', 'Phrase': 'bpm', 'Phrase number': 56},
        {'Family': 'Pragmatic terms family', 'Phrase': 'beats per minute', 'Phrase number': 57},
        {'Family': 'Pragmatic terms family', 'Phrase': 'compression', 'Phrase number': 58},
        {'Family': 'Pragmatic terms family', 'Phrase': 'echo', 'Phrase number': 59},
        {'Family': 'Pragmatic terms family', 'Phrase': 'hertz', 'Phrase number': 60},
        {'Family': 'Pragmatic terms family', 'Phrase': 'hz', 'Phrase number': 61},
        {'Family': 'Pragmatic terms family', 'Phrase': ' ost', 'Phrase number': 62},
        {'Family': 'Pragmatic terms family', 'Phrase': 'pitch shift', 'Phrase number': 63},
        {'Family': 'Pragmatic terms family', 'Phrase': 'track', 'Phrase number': 64},
        {'Family': 'Pragmatic terms family', 'Phrase': 'tune', 'Phrase number': 65},
        {'Family': 'Pragmatic terms family', 'Phrase': 'lufs', 'Phrase number': 66},
        {'Family': 'Pragmatic terms family', 'Phrase': 'db', 'Phrase number': 67},
        {'Family': 'Pragmatic terms family', 'Phrase': ' db', 'Phrase number': 68},
        {'Family': 'Pragmatic terms family', 'Phrase': 'acoustic', 'Phrase number': 69},
        {'Family': 'Pragmatic terms family', 'Phrase': 'acoustic wave', 'Phrase number': 70},
        {'Family': 'Perception terms family', 'Phrase': 'hear', 'Phrase number': 71},
        {'Family': 'Perception terms family', 'Phrase': 'listen', 'Phrase number': 72},
        {'Family': 'Perception terms family', 'Phrase': 'noise', 'Phrase number': 73},
        {'Family': 'Perception terms family', 'Phrase': 'noisy', 'Phrase number': 74},
        {'Family': 'Perception terms family', 'Phrase': 'silent', 'Phrase number': 75},
        {'Family': 'Perception terms family', 'Phrase': 'silence', 'Phrase number': 76},
        {'Family': 'Perception terms family', 'Phrase': 'quiet', 'Phrase number': 77},
        {'Family': 'Perception terms family', 'Phrase': 'track', 'Phrase number': 78},
        {'Family': 'Perception terms family', 'Phrase': 'track', 'Phrase number': 79},
        
        ]
    
    return searching_key_dictionary


def searching_key_Dict_to_CSV(name_of_CSV_file):
    
    csv_file = name_of_CSV_file
    
    with open(csv_file, "w", encoding="UTF-8") as c:
        
        csv_header = ['Family', 'Phrase', 'Phrase number']
        
        csv_writer = csv.DictWriter(c, fieldnames=csv_header)
        
        csv_writer.writeheader()
        
        csv_writer.writerows(searching_key_dictionary())
        
    return print("CSV file created. Success!")

