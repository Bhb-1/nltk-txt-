import nltk
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
fi= open("C:\\Users\\14501\Desktop\\aaa\\01.txt","r",encoding='UTF-8')#加载要处理的文件
text=fi.read()
str0=re.sub('[^\w ]','',text)
str=re.sub( r'[1-9]+\.?[0-9]*', 'number', str0)#数字换成number
str1=str.lower()#大写换成小写
cutwords1=nltk.word_tokenize(str1)#去分词
#interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']   #定义符号列表
#cutwords2 = [word for word in cutwords1 if word not in interpunctuations]   #去除标点符号
stops = set(stopwords.words("english"))#去停用词
cutwords3 = [word for word in cutwords1 if word not in stops]
word_tokens = word_tokenize(cutwords3)#词典
f = open (r'C:\\Users\\14501\Desktop\\aaa\\result.txt','w')#保存文件
print(cutwords3,file = f)
#print(nltk.pos_tag(nltk.word_tokenize(str))) #对分完词的结果进行词性标注
f.close()
