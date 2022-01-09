def is_isogram(string):

  # string.lower() sets to lowercase
  # filter filters the given iterable with the help of a function that tests each element in the iterable to be true or not
  # in our case str.isalpha
  string = ''.join(filter(str.isalpha, string.lower()))
  # set is a collection which is unordered and unindexed. No duplicate members.
  return len(string) == len(set(string))

