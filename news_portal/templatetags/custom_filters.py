from django import template

register = template.Library()


@register.filter
def censor(value):
    # Список нежелательных слов, которые нужно заменить
    bad_words = ['шаг', 'сделать', 'страсти', 'цензурирования', 'слова', 'цензур', 'ильт', 'отличный', 'отличная']

    # Преобразование слов в символы "*"
    for word in bad_words:
        value = value.replace(word, '*' * len(word))

    return value