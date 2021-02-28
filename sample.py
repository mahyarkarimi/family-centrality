import random

test_data_dict = {
    ('v',): [('a',), ('b',)],
    ('b',): [('v',), ('a',)],
    ('a',): [('v',), ('b',)],
}
test_data_dict2 = {
    ('v',): [('a',), ('b',), ('c',)],
    ('b',): [('v',)],
    ('a',): [('v',), ('d',)],
    ('c',): [('v',), ('e',)],
    ('e',): [('c',)],
    ('d',): [('a',)]
}
if __name__ == '__main__':
    with open('d.txt', 'w') as file:
        for i in range(1,30):
            for j in range(1, 30):
                x = random.random()
                if x < 0.2 and i != j:
                    file.write(f'{i} {j}'+ '\n')
                    file.write(f'{j} {i}'+ '\n')
