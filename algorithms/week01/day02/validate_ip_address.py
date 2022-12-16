
def validatePart(part):
  if part.isnumeric() and int(part) >= 0 and int(part) <= 255 :
    return True
  else :
    return False


def validateIP(ip):
  """
  @param ip: str
  @return: bool
  """
  # split by "." , if not 4 parts then invalid
  # check if each part is a number between 0 and 255
  part = ''
  countOfParts = 0

  for char in list(ip) :
    if char == '.' and validatePart(part) :
        countOfParts = countOfParts + 1
        part = ''
    else :
        part = part + char
    if countOfParts > 4 :
        return False
  if validatePart(part) :
    countOfParts = countOfParts + 1
  if countOfParts < 4 :
    return False
  return True

print(validateIP("192.168.0.1"))
