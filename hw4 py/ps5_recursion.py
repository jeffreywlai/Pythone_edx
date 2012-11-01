# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#
def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    if len(aStr) == 0:
        return ''
       
    if aStr.find('#') == -1:
        aStr += '#'
       
    if aStr.find('#') == 0:
        return aStr[1:]
    else:
        char = aStr[aStr.find('#') - 1]
        aStr = aStr[:aStr.find('#') - 1] + aStr[aStr.find('#'):]
        aStr += char
        return reverseString(aStr)

#
# Problem 4: Erician
#
def x_ian(x, word, debug=False):
  if not x:
    if debug:
      print '> no letters, so word is erician'
    return True
 
  letter = x[0]
  remaining = x[1:]
 
  if debug:
    print '> looking for %s of %s in %s' % (letter, x, word)
 
  index = word.find(letter)
  if index >= 0:
    if debug:
      print '>   %s found at %d' % (letter, index)
    return x_ian(x[1:], word[index + 1:], debug=debug)
  else:
    if debug:
      print '> m %s not found; word is not erician' % letter
    return False

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    if len(text) < lineLength:
        return text
    thisLineLength = lineLength + len(text.split(' ')[:len(text[:lineLength].strip().split(' '))][-1]) - len(text[:lineLength].strip().split(' ')[-1])
    if text[thisLineLength-1] != ' ':
        thisLineLength += 1
    return text[:thisLineLength] + '\n' + insertNewlines(text[thisLineLength:], lineLength)
