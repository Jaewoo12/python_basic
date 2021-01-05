'''
yesterday.txt 파일을 읽어서
YESTERDAY라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday라는 단어가 몇번 나왔는지 yesterday_lyric.count('Yesterday')
yesterday라는 단어가 몇번 나왔는지
'''

f=open('yesterday.txt','r')
yesterday_lyric = f.read()
print('YESTERDAY는 ',yesterday_lyric.upper().count('yesterday'),'번 나왔습니다')
#==print('YESTERDAY는 ',yesterday_lyric.count('YESTERDAY'),'번 나왔습니다')
print('Yesterday는 ',yesterday_lyric.count('Yesterday'),'번 나왔습니다')
print('yesterday는 ',yesterday_lyric.count('yesterday'),'번 나왔습니다')