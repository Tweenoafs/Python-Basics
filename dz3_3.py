required_dict = {}


def thesaurus(*args):
    for i in sorted(args):
        el = i[0]
        if el in required_dict:
            required_dict[el] += [i]
        else:
            required_dict[el] = [i]
    return required_dict


print(thesaurus('Александра', 'Кирилл', 'Федор', 'Афдотья', 'Кристина', 'Алексей', 'Михаил',
                'Константин', 'Антон', 'Марина'))
