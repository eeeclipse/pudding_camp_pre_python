## 과제-20240318-0

import csv

print("MPTI 검사를 시작합니다.")

questions   = open("./mpti-sample.csv", "r", encoding='UTF-8')
question    = list(csv.DictReader(questions))

result = {
    "I" : 0,
    "E" : 0,
    "N" : 0,
    "S" : 0,
    "T" : 0,
    "F" : 0,
    "J" : 0,
    "P" : 0,
}

cnt = 0

while cnt < len(question) :
    print(f"""{question[cnt]["번호"]},  {question[cnt]["지문"]}, {question[cnt]["선택항목1"]}, {question[cnt]["선택항목2"]}""")
    
    answer = input('')
    
    if answer == '1' :
        result[f"{question[cnt]['선택항목1값']}"] += 1
        cnt += 1 
        continue    
    elif answer == '2' :
        result[f"{question[cnt]['선택항목2값']}"] += 1
        cnt += 1 
        continue
    elif answer == 'q' :
        print('테스트를 종료할게요. 다음에 또 만나요.')
        break
    else : 
        print('잘못 입력했어요. 다시 문항을 골라주세요.')
    
    
    
print(result)