'''
yesterday.txt 파일을 읽어서
YESTERDAY라는 단어가 몇번 나왔는지 yesterday_lyric.upper().count('YESTERDAY')
Yesterday라는 단어가 몇번 나왔는지 yesterday_lyric.count('Yesterday')
yesterday라는 단어가 몇번 나왔는지
'''

f = open('yesterday.txt','r')
yesterday_lyric = f.read()
lyric1 = yesterday_lyric.lower()
lyric2 = yesterday_lyric.upper()
lyric3 = yesterday_lyric.title()

print('YESTERDAY는 ',lyric2.count('YESTERDAY'),'번 나왔습니다')
print('Yesterday는 ',lyric3.count('Yesterday'),'번 나왔습니다')
print('yesterday는 ',lyric1.count('yesterday'),'번 나왔습니다')


#강사님 방법
'''
mode - (read) , w (write) , a(append) , rb(read binary) , wb(write binary)

#1f = open ('yesterday.txt' , ' r' )
 yesterday_lyric = f.read()
 f.close()

#2 with open ('yesterday.txt','r') as f:
    yesterday_lyric = f.read ()           #with를 쓰면 close 할 필요가 없으므로 더 편함.들여쓰기해야됨

#3 with open('yesterday.txt') as file:
        lyric = ''
        while 1:
            line = file.readline()       
            if not line:
                break                   #라인별로 한줄 한줄씩 읽어라.무한루프    
            lyric = lyric + line.strip() '\n''
            
print('Number of a word \'YESTERDAY\'', yesterday_lyric.upper().count('YESTERDAY'))
print('Number of a word \'Yesterday\'', yesterday_lyric.upper().count('Yesterday'))
print('Number of a word \'yesterday\'', yesterday_lyric.upper().count('yesterday'))

'''

#file read를 함수로 선언
def file_read(file_name):
    with open('yesterday.txt', 'r') as f:
        lyric = f.read()
        print(lyric)
    return lyric

#함수 호출
yesterday_lyric2 = file_read('yesterday.txt')

print('Number of a word \'YESTERDAY\'', yesterday_lyric2.upper().count('YESTERDAY'))
print('Number of a word \'Yesterday\'', yesterday_lyric2.count('Yesterday'))
print('Number of a word \'yesterday\'', yesterday_lyric2.count('yesterday'))
