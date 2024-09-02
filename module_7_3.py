import pprint
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punctuation in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuation, '')
                    words = text.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        list = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                list[name] = words.index(word.lower()) + 1
        return list

    def count(self, word):
        list = {}
        for name, words in self.get_all_words().items():
            list[name] = words.count(word.lower())
        return list

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))
