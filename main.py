dictionary_list = []
all_abbreviations = []
all_translations = []
words_in_the_line = []


def read_dict():
    """Check if dictionary.txt is present and read it into a list."""
    try:
        with open("dictionary.txt") as dictionary:
            for dictionary_line in iter(dictionary): # this whole block of code generates two lists, containing either abbreviation, or translation, but either way on the same position aka they're matching
                words_in_the_line = dictionary_line.split()
                all_abbreviations.append(words_in_the_line[0]) # this adds just the first word to all_abbreviations
                # the below 4 lines add the translation
                translation = " "
                for x in range(2,len(words_in_the_line)):
                    translation = translation + words_in_the_line[x] + " "
                all_translations.append(translation)
        return (all_abbreviations,all_translations)
    except IOError:
        print("Cannot find the file.")
        file_found = False # this is used for the IF clause below
        return file_found


def compare_dict(new_text,all_abbreviations,all_translations):
    """Compare text message with dictionary entries.
    
    Keyword args:
    new_text --- list with orignal text message generated through user input
    all_abbreviations --- list with abbreviations generated through read_dict()
    all_translations --- list with translations generated through read_dict()
    """
    final_message = ""
    for word_position in range(0,len(new_text)):
        current_word = new_text[word_position]
        try:
            match_position = all_abbreviations.index(current_word.upper()) # i think this will execute only if current_word (str) is in all_abbreviations and it will retrn the index number
            final_message = final_message + " " + all_translations[match_position] # all_translation[match_position] makes sures it retrieves the corresponding translation - as we already matched abbreviations with translations
        except:
            final_message = final_message + " " + current_word
    return final_message


# main
if read_dict(): # checks if the file is present and reads it
    new_text = input("Please enter the text: ").split(" ")
    all_abbreviations, all_translations = read_dict() # these are helper variables
    translated_message = compare_dict(new_text,all_abbreviations,all_translations)
    print(translated_message)
