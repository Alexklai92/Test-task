#!/usr/bin/python
import sys


class TextAlignment:
    def __init__(self):
        self.filename = self.input_filename()
        self.alignment()

    def input_filename(self):
        """Ввод имени файла"""

        return sys.argv if len(sys.argv) > 1 else input('Введите имя файла: ')

    def open_file(self):
        """Чтение файла"""

        try:
            with open(self.filename, encoding='utf-8') as file_text:
                text = file_text.read()
        except FileNotFoundError:
            text = ''
            print('Такого файла нет.')

        return text

    def align_left_text(self):
        """Формирование строки в текст с шириной строк до
        80 символов и выравнивание его по левому краю"""

        text = self.open_file()
        new_list = list()

        for paragraph in text.split('\n'):
            words = paragraph.split(' ')
            counter = 0

            for word in words:
                if counter >= 80 or counter + len(word) >= 80:
                    counter = 0
                    new_list.append('\n')

                if counter != 0 and counter != 80:
                    new_list.append(' ' + word)
                    counter += len(word) + 1
                else:
                    new_list.append(word)
                    counter += len(word)

            new_list.append('\n\n')

        return ''.join(new_list)

    def alignment(self):
        """Выравнивание текста по ширине страницы"""

        text = self.align_left_text()
        width = 80
        paragraphs = [paragraph.splitlines() for paragraph in text.split('\n\n')]

        for paragraph in paragraphs:
            for i, line in enumerate(paragraph[:-1]):
                words = line.split()
                missing_gaps = width - sum(map(len, words))
                cs = len(words) - 1
                spw, mod = divmod(missing_gaps, cs)
                spw = spw if spw > 0 else 1
                whitespace = [' ' * spw] * (cs - mod) + [' ' * (spw + 1) for _ in range(mod)] + ['']
                paragraph[i] = ''.join(w + s for w, s in zip(words, whitespace))

        print('\n\n'.join('\n'.join(paragraph) for paragraph in paragraphs))


if __name__ == '__main__':
    alignment = TextAlignment()
