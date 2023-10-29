def count_letters(text: str):
    text = text.lower()
    keys = []
    for i in text:
        if i.isalpha():
            keys.append(i)
    dictionary_of_letters = dict.fromkeys(keys, 0)
    for i in text:
        if i.isalpha():
            dictionary_of_letters[i] += 1
    return dictionary_of_letters


def calculate_frequency(dictionary_of_letters):
    count_of_letters = sum(i for i in dictionary_of_letters.values())
    for i in dictionary_of_letters:
        dictionary_of_letters[i] /= count_of_letters
    return dictionary_of_letters


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

dictionary = calculate_frequency(count_letters(main_str))
for key, value in dictionary.items():
    print(key, ': ', '%0.2f' % value, sep="")
