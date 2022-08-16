from lorem_text import lorem

paragraph_length = 100
f= open("placeholder.txt","w+")
for i in range(100):
    f.write(lorem.paragraphs(paragraph_length))
f.close()