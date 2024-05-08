def comma(n):
    n = str(n) #문자로 변환
    if n[0] == '-': #-있는경우 따로 고려!!
        return '-' + comma(n[1:])
    if len(n) <= 3: #재귀함수 돌아서 3미만됐을 경우 걔 출력
        return n
    if n.find('.') == -1: #find함수는 그문자 있으면 인덱스값, 없으면 -1 반환
        # print(n.find('.')) #디버깅용
        # print(n)
        return comma(n[:-3]) + ',' + n[-3:] #뒤에 3개만 ,000 이런식으로 하고 앞에 부분은 재귀로 다시보냄
    else: #소수점 전으로 끊고, 소수점 후 끊는것
        return comma(n[:n.find('.')]) + n[n.find('.'):]
    #[출처] 파이썬(python) 숫자의 ,[콤마,쉼표] 제거와 삽입(천단위 회계처리 수)|작성자 SteveLee