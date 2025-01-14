# Finger exercise: Remedy the problem described in the previous
# paragraph. Hint: a simple way to do this is to create a new book by
# appending something to the original book.
#   If a character occurs in the plain text but not in the book,
#   something bad happens. The code_keys dictionary will map each
#   such character to -1, and decode_keys will map -1 to whatever the
#   last character in the book happens to be.

def gen_missing_keys(book, plain_text):
    """Gives a string of missing characters found in plain_text but not in the book"""
    s = ''
    for c in plain_text:
        if book.find(c) == -1:
            s += c
    return s
def gen_code_keys(book, plain_text):
    new_book = book + gen_missing_keys(book, plain_text)
    code_keys = {}
    for c in plain_text:
        code_keys[c] = str(new_book.find(c))
    return code_keys
encoder = lambda code_keys, plain_text: \
    ''.join(['*' + code_keys[c] for c in plain_text])[1:]
# The problem now is that there is a new book generated but the decoder does not have access to the new book
encrypt = lambda book, plain_text: \
    encoder(gen_code_keys(book, plain_text), plain_text)