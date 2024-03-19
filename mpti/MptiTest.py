## MptiTest.py
## 과제-20240318-1


import csv

class MptiTest() :
    def __init__(self, location):
        """
        __init__ _summary_

        Args:
            location (str): csv 파일 경로
            
        """
        ## 초기화
        print("MPTI 검사를 시작합니다.")
        
        # questions   = open("./mpti-sample.csv", "r", encoding='UTF-8')
        questions   = open(location, "r", encoding='UTF-8')
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
        
        self.question   = question
        self.result     = result
    
    
    
    def mpti_test(self) : 
        """
        mpti_test 

        Returns:
            result_string (str): MPTI 테스트 결과
        
        """
        
        question        = self.question
        result          = self.result
        result_string   = ""
        
        cnt = 0

        ## TODO
        while cnt < len(question) :
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
                print('!!!!! 잘못 입력했어요. 다시 문항을 골라주세요.')
    
        
        ## TODO
        if cnt == len(question) : 
            if result["I"] < result["E"] : 
                result_string += "E"
            else :
                result_string += "I"
                
            if result["N"] < result["S"] :
                result_string += "S"
            else :
                result_string += "N"
                
            if result["T"] < result["F"] :
                result_string += "F"
            else :
                result_string += "T"
                
            if result["J"] < result["P"] :
                result_string += "P"
            else :
                result_string += "J"
        
            print(f"MPTI 검사결과는 {result_string} 이에요")
        else :
            pass
        
        return result_string
        
    
if __name__ == "__main__" :
    mpti = MptiTest("./mpti-sample.csv")
    mpti.mpti_test()
    
    
""" TEST """
def test_MptiTest(monkeypatch):
    inputs = iter(['1','2','1','1','1', '1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    mpti = MptiTest("./mpti-sample.csv")
    test_input = mpti.mpti_test()
    assert test_input == 'INTJ'