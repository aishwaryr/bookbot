def main():
  book = "books/frankenstein.txt"
  with open(book) as f:
    file_contents = f.read()
    print(create_report(file_contents, book))

def count_words(string):
  words = string.split()
  return len(words)

def count_chars(string):
  char_dict = {" ": 1}
  for i in string:
    if i.lower() in char_dict:
      char_dict[i.lower()] += 1
    else:
      char_dict[i.lower()] = 1
  return char_dict

def count_alphabets_lower(string):
  char_dict = {}
  for i in string:
    lower = i.lower()
    if ord(lower) >=97 and ord(lower) <= 122:
      if lower in char_dict:
        char_dict[lower] += 1
      else:
        char_dict[lower] = 1
  return char_dict

def create_report(string, book):
  report = f"--- Begin report of {book} ---\n"
  report += f"{count_words(string)} words found in the document\n"
  char_count = count_alphabets_lower(string)
  for c in char_count:
    str = f"The '{c}' character was found {char_count[c]} times\n"
    report += str
  report += "--- End report ---"
  return report

main()
