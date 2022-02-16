# A typical decorator With an inner() function

def camelcase(s):
    
    # Turn Strings_like_this into StringsLikeThis

    # List Comprehension
    return ''.join([word.capitalize() for word in s.split('_')])

print(camelcase('some_string'))

