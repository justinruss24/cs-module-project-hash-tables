def word_count(s):
    # Your code here
    ignore = list('":;,.-+=/\|[]}{()*^&')
    words = {}
    filtered = ""
    for i in s:
        if i not in ignore:
            filtered = filtered + i
    for word in filtered.split():
        lower = word.casefold()
        if lower in words:
            words[lower] += 1
        else:
            words[lower] = 1
    return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
