instr = input('Введите выражение: ').replace(' ','')

#Распарсить

hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = tuple('+-')
supported_ops = hp_ops + mp_ops + lp_ops
digit_chars = tuple(map(str, range(10))) + tuple('.-')

actions = list()
d = dict()
d['opr'] = 'First'
d['val'] = None
actions.append(d)


for letter in instr:
    if letter in supported_ops and (i > 0):
        actions.append({'opr': letter, 'val': ''})
        pass
    elif letter in digit_chars:
        actions[-1]['val'] += letter
        pass