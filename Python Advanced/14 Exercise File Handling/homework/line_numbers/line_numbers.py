from string import punctuation

with open('test.txt') as input_file, open('output', 'w') as output_file:
    result = []
    for row, line in enumerate(input_file):
        letters_count = 0
        punc_count = 0
        for c in line:
            if c.isalpha():
                letters_count += 1
            elif c in punctuation:
                punc_count += 1
        result.append(f'Line {row + 1}: {line} ({letters_count})({punc_count})')
    output_file.write('\n'.join(result))