def convert(number):
  # alternative use a key, value loop
  sound = ''
  if (number % 3) == 0:
    sound = 'Pling'
  if (number % 5) == 0:
    sound += 'Plang'
  if (number % 7) == 0:
    sound += 'Plong'
  if not sound:
    sound = str(number)
  return sound
