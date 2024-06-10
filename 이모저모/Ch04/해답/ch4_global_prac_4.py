# 전역변수 실습

def my_ave1():
    print(f'함수 my_ave1() 내부:')
    my_list.append(5)
    print(f'전역변수 my_list={my_list}로 변경')
    return sum(my_list)/len(my_list)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave()={my_ave1()}')
print(f'함수 my_ave1() 호출 후, my_list = {my_list}. 변경 되었음.\n')

def my_ave2():
    print(f'함수 my_ave2() 내부:')
    my_list = [1, 2, 3, 4, 5]  # 아예 새롭게 리스트 값을 할당했다면?
    print(f'my_list={my_list}로 재할당. id(my_list)={id(my_list)}로 전역변수 my_list 와 달라짐. '
          f'이름은 같으나 이제 더 이상 같은 변수가 아님.')
    return sum(my_list)/len(my_list)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave2(my_list)={my_ave2()}. ')
print(f'함수 my_ave2() 호출 후, my_list = {my_list}. 변경 안되었음.\n')

def my_ave3():
    print(f'함수 my_ave3() 내부:')
    global my_list
    my_list = [1, 2, 3, 4, 5]  # 다시 새롭게 리스트 값을 할당했다면?
    print(f'my_list={my_list}로 재할당. id(my_list)={id(my_list)}로 전역변수 my_list 와 동일함.')
    return sum(my_list)/len(my_list)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave3(my_list)={my_ave3()}')
print(f'함수 my_ave3() 호출 후, my_list = {my_list}. 변경 되었음.\n')

def my_ave4(my_list):  # my_list = my_list 에 의해 같은 메모리를 참조함
    print(f'함수 my_ave4() 내부:')
    my_list += [5]
    print(f'전역변수 my_list={my_list}로 변경')
    print(f'매개변수 my_list 의 id는 {id(my_list)}. 전역변수 my_list 와 서로 같은 메모리를 참조함')
    return sum(my_list)/len(my_list)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave4(my_list)={my_ave4(my_list)}')
print(f'함수 my_ave4() 호출 후, my_list = {my_list}. 변경 되었음.\n')

def my_ave5(my_list):  # my_list = my_list 에 의해 같은 메모리를 참조함
    print(f'함수 my_ave5() 내부:')
    print(f'my_list = {my_list}')
    print(f'my_list 의 id는 {id(my_list)}. 전역변수 my_list 와 서로 같은 메모리를 참조함')
    my_list = [1, 2, 3, 4, 5]
    print(f'my_list = {my_list}로 재할당')
    print(f'my_list 의 id는 {id(my_list)}. 이제 전역변수 my_list 와 서로 다른 메모리를 참조함')
    return sum(my_list)/len(my_list)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave4(my_list)={my_ave5(my_list)}. ')
print(f'함수 my_ave5() 호출 후, my_list = {my_list}. 변경 안되었음.\n')

def my_ave6(my_list2):  # my_list = my_list 에 의해 같은 메모리를 참조함
    print(f'함수 my_ave6() 내부:')
    print(f'my_list2 = {my_list2}')
    print(f'my_list2 의 id는 {id(my_list2)}. 전역변수 my_list 와 서로 같은 메모리를 참조함')
    my_list2 = [1, 2, 3, 4, 5]
    print(f'my_list2 = {my_list2}로 재할당')
    print(f'my_list2 의 id는 {id(my_list2)}. 이제 전역변수 my_list 와 서로 다른 메모리를 참조함')
    return sum(my_list2)/len(my_list2)

my_list = [1, 2, 3, 4]
print(f'my_list = {my_list}. id(my_list)={id(my_list)}')
print(f'my_list의 평균값은 my_ave6(my_list)={my_ave6(my_list)}. ')
print(f'함수 my_ave6() 호출 후, my_list = {my_list}. 변경 안되었음.')