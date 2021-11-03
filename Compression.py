

def overlapcheck(string='',length=int(1)):
    count = int(1)
    word = string[-length:]
    while((count+int(1))*length<=len(string)):
        currentword = string[-(count+int(1))*length:-(count)*length]
        if currentword == word:
            count = count+int(1)
        else:
            break
    return {'count':count,'word':word}
# 해당문자를 뒤에서부터 length길이로 잘라서 탐색했을때 같은문자가 연속으로 몇번나오는지 
# count: 연속으로나온횟수 
# word: 잘라서 확인하는 문자열
def charcheck(string='',level = []):
    length = 1
    endpoint = (int)(len(string)/int(2))
    print(endpoint)
    min = None
    while True :
        result =overlapcheck(string= string,length=length)
        backlevel = None
        valueadd = int(0)
        wordadd = ""
        if result['count']*length <= len(level):
            backlevel = level[-result['count']*length]
        if not (backlevel == None):
            valueadd = backlevel['value']
            wordadd = backlevel['word']
        value = (result['count']-int(1))*length + valueadd
        if min == None:
            min = {'value':value,'word':wordadd+result['word']+str(result['count'])}
        elif value > min['value']:
            min = {'value':value,'word':wordadd+result['word']+str(result['count'])}
        if endpoint<=length:
            break
        else:
            length = length+int(1)
    level.append(min)
# 문자열이 들어왓을때, 1에서부터 문자열총길이/2 까지 탐색하며 overlapcheck 에넣어보고
# value = 문자가 줄어든길이 가 가장 높은값을 level에다가 넣음
def compression(string):
    level = []
    for e in range(0,len(string)):
        currentstring = string[0:e+int(1)]
        charcheck(string=currentstring,level=level)
    print(len(level))
    return level[-1]['word']
# 문자를 하나씩 추가하면서
# charcheck 에 넣어주는 함수
# 리턴시 가장높은 level에 word를 반환함
if __name__ == "__main__":
    word = input("압축할 문자를 선택해주세요 : ")
    result = compression(word)
    print(result)