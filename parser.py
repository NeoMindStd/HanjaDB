# dependencies:
#   pyyaml
#   hanja
import hanja; from hanja import hangul # 영어, 특수문자를 제외하는 용도

src=open("input/resource",encoding="UTF8")

result=[]
for line in src.readlines():
    if not hanja.is_hanja(line[0]):continue
    
    # 줄바꿈 문자 전처리
    l=line.split('\n')[0]
    
    # 획수 분리를 위한 인덱스 파악
    for i in range(len(l)-1,0,-1):
        if l[i]=='(':break

    # 첫번째 글자는 무조건 한자
    
    # 한글 뜻, 음, 획수, 영어뜻 포함
    #d={'hanja':l[0],'meanings':[],'sounds':[], 'eng_meanings':[], 'strokes':int(l[i+1:-1])}
    
    # 한글 뜻, 음, 획수 포함
    #d={'hanja':l[0],'meanings':[],'sounds':[], 'strokes':int(l[i+1:-1])}
    
    # 한글 뜻, 음만 포함
    d={'hanja':l[0],'meanings':[],'sounds':[]}
    
    l=l[2:i].replace(';',',').split(',') # 영어 뜻을 제대로 분리하려면 수정 필요
    for i in range(len(l)):
        f=False
        for c in l[i]:
            if not (hangul.is_hangul(c) or c==' '):
                f=True
                break
        if f:break
    kor=l[:i]
    eng=l[i:]
    for i in range(len(kor)):kor[i]=kor[i].strip()
    for i in range(len(eng)):eng[i]=eng[i].strip()

    for s in kor:
        tmp=s.split()
        try:
            if tmp[0]=='':raise Exception()
            d['meanings'].append(' '.join(tmp[:-1]))
            if tmp[-1] not in d['sounds']:d['sounds'].append(tmp[-1])
        except:break

    # 영어 뜻을 사용하려면 여기서 영어를 d의 'eng_meanings'에 append

    # Python dictionary to Json entitiy string
    # 영어 뜻을 사용하려면 여기서 json으로 같이 convert
    if not d['meanings'] or not d['sounds']:continue
    d=str(d).replace("'",'"')
    index_m=d.index(' "meanings": [')
    index_s=d.index(' "sounds": [')
    d=[d[1:index_m],d[index_m+1:index_s],d[index_s+1:-1]]
    result.append('{\n\t\t'+'\n\t\t'.join(d)+'\n\t}')

src.close()

# default output is json
# if you need db file? visit to:
# json to sql, csv 'https://numidian.io/convert/json/to/sqlite'
dest=open("output/result.json","w",encoding="UTF8")

dest.write('[\n\t'+',\n\t'.join(result)+'\n]')

dest.close()

