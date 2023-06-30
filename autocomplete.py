import re
WORD = 0
POPULARITY = 1


def main():
    run = True
    search_history = {}
    while run:
        searched_word = input('search for the word:')
        if not is_searched_word_vlid(searched_word):
            print('no a valid word')
            continue

        searched_word.lower()
        tab_or_search = input('tab or search (t,s):')
        if tab_or_search == 't':
            display_complete_serch_option(search_history, searched_word)

        elif tab_or_search == 's':
            add_to_search_history(search_history, searched_word)

        # print(search_history)

def is_searched_word_vlid(searched_word):
    if re.match("^[A-Za-z]*$", searched_word):
        return True

def display_complete_serch_option(search_history, searched_word):
    search_history_indent = enter_to_dict_indent(search_history, searched_word)
    if not search_history_indent:
        print('key not in dict')
        return None

    print(search_history_indent['$'])

def enter_to_dict_indent(my_dict, my_keys):
    try:
        my_dict_indent = my_dict
        for key in my_keys:
            my_dict_indent = my_dict_indent[key]

        return my_dict_indent

    except KeyError:
        return None

    except Exception as e:
        raise e 

def add_to_search_history(search_history, searched_word):
    search_history_indent = enter_to_dict_indent(search_history, searched_word)    
    if search_history_indent:
        for word in search_history_indent['^']:
            if word[WORD] == searched_word:
                word[POPULARITY] += 1
                update_max_serched_word(search_history, word)
                break

        else:
            search_history_indent['^'].append([searched_word, 1])

    else:
        builed_new_indents(search_history, searched_word)


def builed_new_indents(search_history, searched_word):
    search_history_indent = False
    index = len(searched_word)
    while not search_history_indent and index > 0:
        index -= 1
        search_history_indent = enter_to_dict_indent(search_history, searched_word[:index])    

    for new_key in searched_word[index:len(searched_word)]:
        search_history_indent.update({new_key : {'^' : [], '$' : [searched_word, 1]}})
        search_history_indent = search_history_indent[new_key]

    else:
        search_history_indent['^'].append([searched_word, 1])

def update_max_serched_word(search_history, word):
    search_history_indent = search_history
    for later in word[WORD]:
        if search_history_indent[later]['$'][POPULARITY] < word[POPULARITY]:
            search_history_indent[later]['$'] = word

        search_history_indent = search_history_indent[later]


if __name__ == '__main__':
    main()