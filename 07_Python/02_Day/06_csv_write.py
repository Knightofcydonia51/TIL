lunch={
    '김밥지옥': '055-267-2615',
    '밥풀떼기': '054-222-2222',
    '남도식당': '02-222-2222'
}

#1. 방법 1

with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write(f'{item[0]}, {item[1]}\n')
