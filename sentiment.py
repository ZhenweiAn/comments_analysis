import paddlehub as hub
from pyltp import SentenceSplitter
from tqdm import tqdm
def get_score(filename):
    senta = hub.Module(name="senta_bilstm")
    f = open(filename,'r',encoding = 'utf-8')
    
    cnt = 0
    score = 0.0
    print(len(f.readlines()))
    return
    for line in tqdm(f.readlines()):
        input_dict = {'text':[line]}
        if line == '' or line == "\r" or line == "\n":
            continue
        result = senta.sentiment_classify(data=input_dict)
        score += result[0]['positive_probs']
        cnt += 1
    print(score)
    print(cnt)
    print(score / cnt)
  

def get():
    senta = hub.Module(name="senta_bilstm")
    text = ['我一路向北，离开有你的季节，你说你好累，已无法再爱上谁','快乐','悲伤','夕阳西下，断肠人在天涯','']
    input_dict = {'text':text}
        
    result = senta.sentiment_classify(data=input_dict)
    for r in result:
        print(r)
print(get())