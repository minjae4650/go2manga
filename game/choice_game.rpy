image 성냥 = im.Scale("images/items/성냥.png", 150, 145)
image 성냥_선택 = im.Scale("images/items/성냥_hover.png", 150, 145)
image 물통 = im.Scale("images/items/물통.png", 92, 190)
image 물통_선택 = im.Scale("images/items/물통_hover.png", 92, 190)
image 손수건 = im.Scale("images/items/손수건.png", 155, 158)
image 손수건_선택 = im.Scale("images/items/손수건_hover.png", 155, 158)
image 밧줄 = im.Scale("images/items/밧줄.png", 130, 157)
image 밧줄_선택 = im.Scale("images/items/밧줄_hover.png", 130, 157)
image 손전등 = im.Scale("images/items/손전등.png", 170, 150)
image 손전등_선택 = im.Scale("images/items/손전등_hover.png", 170, 150)
image 과자 = im.Scale("images/items/과자.png", 130, 192)
image 과자_선택 = im.Scale("images/items/과자_hover.png", 130, 192)

# 선택 상태를 저장할 변수 정의
default 성냥_selected = False
default 물통_selected = False
default 손수건_selected = False
default 밧줄_selected = False
default 손전등_selected = False
default 과자_selected = False

# 정답 아이템 리스트 정의
default correct_answers = ["성냥", "손전등"]


init python:
    # 각 아이템의 선택 상태를 토글하는 함수
    def toggle_item(item_name):
        globals()[f"{item_name}_selected"] = not globals()[f"{item_name}_selected"]

    # 정답 확인 액션 정의
    def verify_answer():
        selected = []
        if 성냥_selected:
            selected.append("성냥")
        if 물통_selected:
            selected.append("물통")
        if 손수건_selected:
            selected.append("손수건")
        if 밧줄_selected:
            selected.append("밧줄")
        if 손전등_selected:
            selected.append("손전등")
        if 과자_selected:
            selected.append("과자")
        
        if set(selected) == set(correct_answers):
            renpy.hide_screen("fire_choice")
            renpy.jump("fire_success")
        else:
            renpy.hide_screen("fire_choice")
            renpy.jump("fire_fail")
        

screen fire_game():
    modal True

    frame:
        align (0.5, 0.5)
        has vbox
        text "모닥불을 피우기 위해 필요한 아이템을 선택해주세요" xalign 0.5
        textbutton "시작" action [Hide("fire_game"), Jump("fire_start")] xalign 0.5

label fire_start:
    window hide
    call screen fire_choice


screen fire_choice():
    modal True

    frame:
        align (0.5, 0.5)
        xsize 912
        ysize 712

        add im.Scale("images/image 4.png", 900, 700)

        imagebutton:
            idle ( "성냥" if not 성냥_selected else "성냥_선택" )
            hover "성냥_선택"
            xpos 100
            ypos 100
            action Function(toggle_item, "성냥")

        imagebutton:
            idle ( "물통" if not 물통_selected else "물통_선택" )
            hover "물통_선택"
            xpos 300
            ypos 100
            action Function(toggle_item, "물통")

        imagebutton:
            idle ( "손수건" if not 손수건_selected else "손수건_선택" )
            hover "손수건_선택"
            xpos 500
            ypos 100
            action Function(toggle_item, "손수건")

        imagebutton:
            idle ( "밧줄" if not 밧줄_selected else "밧줄_선택" )
            hover "밧줄_선택"
            xpos 100
            ypos 300
            action Function(toggle_item, "밧줄")

        imagebutton:
            idle ( "손전등" if not 손전등_selected else "손전등_선택" )
            hover "손전등_선택"
            xpos 300
            ypos 300
            action Function(toggle_item, "손전등")

        imagebutton:
            idle ( "과자" if not 과자_selected else "과자_선택" )
            hover "과자_선택"
            xpos 500
            ypos 300
            action Function(toggle_item, "과자")

        textbutton "확인" xpos 450 ypos 600 action Function(verify_answer)


label fire_fail:
    window show
    "틀린것 같아. 이걸론 불을 붙일 수 없어"
    jump fire_start

label fire_success:
    window show
    jump after_fire
    
