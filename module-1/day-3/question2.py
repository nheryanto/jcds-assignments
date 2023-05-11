if __name__ == '__main__':
    text = input("Enter text: ")
    oldText = input("Enter part from previous text to be replaced: ")
    newText = input("Enter new text: ")
    modifiedText = ''

    i = 0
    while i < len(text):
        if text[i:i+len(oldText)] == oldText: # read note below for future ref (yet to verify)
            modifiedText += newText
            i += len(oldText)
        else:
            modifiedText += text[i]
            i += 1
    print(modifiedText)
    
    # string slicing is not affected by out of range indices
    # i.e. in string[start:stop:step], start and stop can be greater than len(string), returning empty strings
    # this does not apply in string indexing
    # i.e. string[index] with index > len(string) will return a string index out of range error

    # easy solution using string.replace() method
    # string.replace() does not change the string itself, it has to be returned in a new variable
    #if oldText in text:
    #    modifiedText = text.replace(oldText, newText) 
    #print(modifiedText)
