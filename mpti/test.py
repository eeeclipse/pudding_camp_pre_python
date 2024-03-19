import csv

print("MPTI 검사를 시작합니다.")

questions   = open("./mpti-sample.csv", "r", encoding='UTF-8')
# question    = csv.reader(questions) 
question    = list(csv.DictReader(questions))


# with open("./mpti-sample.csv", newline = '') as question :
    # questions = csv.reader(question, delimiter=',', quotechar='|')

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

# self.questions  = questions
# self.result     = result

print(question[2]["지문"])
print(type(question[2]))
print(result)

cnt = 0

while cnt < len(question) :
# for i, value in enumerate(question) : 
    print(f"""{question[cnt]["번호"]},  {question[cnt]["지문"]}""")
    print("1 : ", question[cnt]["선택항목1"])
    print("2 : ", question[cnt]["선택항목2"])
    
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

# for i, value in enumerate(questions) : 
    
#     print(i, value['지문'])
#     # print(value('선택항목1'))
#     # print(value('선택항목2'))
#     answer = input('')
    
#     if answer == '1' :
#         result[f"{value['선택항목1값']}"] += 1
#     elif answer == '2' :
#         result[f"{value['선택항목2값']}"] += 1
#     elif answer == 'q' :
#         break
#     else : 
#         print('잘못 입력했어요. 다시 문항을 골라주세요.')

# for i, row in enumerate(questions) : 
#     print(i, row('지문'))
#     print(row('선택항목1'))
#     print(row('선택항목2'))
#     answer = input('')
    
#     if answer == '1' :
#         result[{row('선택항목1값')}] += 1
#     elif answer == '2' :
#         result[row('선택항목2값')] += 1
#     elif answer == 'q' :
#         break
#     else : 
#         print('잘못 입력했어요. 다시 문항을 골라주세요.')

# print(result)