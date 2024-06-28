import re

def compare(a, b):
  pattern = re.match(a, b)
  if pattern:
    return pattern.group()
  else:
    pattern = re.match(b, a)
    if pattern:
      return pattern.group()
    else:
      return None

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA