file = open('C:/Users/Administrator/Desktop/pythonone.txt','w')
file.write('hello world!')

#控制在桌面写入的文件名称和内容的函数text_create
def text_create(name, msg):
    desktop_path = 'C:/Users/Administrator/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('done')
#text_create('hello','hello world')

#敏感词过滤
def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return word.replace(censored_word, changed_word)

#text_filter('Python is lame!')


#设计自己的函数
def censored_text_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)

censored_text_create('Try','lame!lame!lame!')

#设计函数，在桌面创建10个文本，以数字命名
def create_file():
    name = 1
    desktop_path = 'C:/Users/Administrator/Desktop/'
    
    while name <= 10:
         full_path = desktop_path + str(name) + '.txt'
         file = open(full_path,'w')
         name = name + 1
         print('done')

create_file()

