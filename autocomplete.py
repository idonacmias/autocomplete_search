WORD = 0
POPULARITY = 1


def main():
    run = True
    search_history = {}
    while run:
        searched_word = input('search for the word:')
        tab_or_search = input('tab or search (t,s):')
        if tab_or_search == 't':
            display_complete_serch_option(search_history, searched_word)

        elif tab_or_search == 's':
            add_to_search_history(searched_word, search_history)

def display_complete_serch_option(search_history, searched_word):
    try:
        for i in range(5):
            print(search_history[searched_word][i][WORD], search_history[searched_word][i][POPULARITY])

    except KeyError as e:
        print('string not in search history, no tab to complete')

    except IndexError as e:
        print('less then 5 history serch to complete')

def add_to_search_history(searched_word, search_history):
    for i, latter in enumerate(searched_word):
        later_combination = searched_word[:i+1]
        add_to_later_combination(searched_word, later_combination, search_history)

def add_to_later_combination(searched_word, later_combination, search_history):
    try:
        for i, searched_word_in_the_past in enumerate(search_history[later_combination]):
            if searched_word_in_the_past[WORD] == searched_word:
                searched_word_in_the_past[POPULARITY] += 1
                search_history[later_combination].sort(key=take_popularity, reverse=True)
                break

        else:
            search_history[later_combination].append([searched_word, 1])

    except KeyError as e:
        search_history.update({later_combination : [[searched_word, 1]]})
    
def take_popularity(element):
    return element[POPULARITY]

if __name__ == '__main__':
    main()