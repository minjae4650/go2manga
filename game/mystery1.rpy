image scene88 = "images/scenes/scene88.png"
image scene88_radio = "images/invest/scene88_radio.png"
image scene88_window = "images/invest/scene88_window.png"
image scene88_person = "images/invest/scene88_person.png"
image scene88_door = "images/invest/scene88_door.png"
image scene88_water = "images/invest/scene88_water.png"

image scene87 = im.Scale("images/scenes/scene87.png", 1500, 1080) # 바다위의 옷

image scene89 = im.Scale("images/scenes/scene89.png", 1500, 1080) # 바닷물
image scene90 = im.Scale("images/scenes/scene90.png", 1500, 1080) # 바닷물 맛보기
image scene91 = im.Scale("images/scenes/scene91.png", 1500, 1080) # 창문 다가가보기
image scene92 = im.Scale("images/scenes/scene92.png", 1500, 1080) # 문 잠겨있기
image scene93 = im.Scale("images/scenes/scene93.png", 1500, 1080) # 라디오
image scene94 = im.Scale("images/scenes/scene94.png", 1500, 1080) # 밤바다

define character_conan = Character('에도가와 코난', color="#c8ffc8")

# 각 조사의 완료 상태를 저장
default investigation_state = {
    "person": False,
    "radio": False,
    "water": False,
    "window": False,
    "door": False
}

# 선택지 진행 상태
default choice_state = {
    "water_1": False,
    "water_2": False,
    "door_1": False,
    "door_2": False,
    "window_1": False,
    "window_2": False
}

default completed_choices = 0

# script.rpy
label mystery1:
    play music "conan_ost_17.ogg"
    call screen mystery1_investigation


######################################
# 조사용 스크린
######################################
screen mystery1_investigation():
    modal True
    add "scene88" xalign 0.5 yalign 0.5

    default main_done = sum(1 for v in investigation_state.values() if v)
    default sub_done = sum(1 for v in choice_state.values() if v)

    # 총 5개 메인 조사 중 몇 개가 True인지 표시
    # text "메인 조사 완료: [main_done] / 5" xpos 50 ypos 30 color "#ffffff"
    # 만약 세부 조사도 보여주고 싶다면 아래처럼 표시할 수도 있음
    # text "세부 선택지 완료: [sub_done]" xpos 50 ypos 60 color "#ffffff"

    imagebutton:
        idle "scene88_person"
        xalign 0.5
        yalign 0.5
        focus_mask True  # 알파 채널을 이용해 곡선 모양 클릭 가능
        mouse "highlight"  # <-- 이 한 줄이면, 버튼에 마우스를 올렸을 때 "highlight" 커서가 표시됨!
        action Show("mystery1_person")

    imagebutton:
        idle "scene88_radio"
        xalign 0.5
        yalign 0.5
        focus_mask True  # 알파 채널을 이용해 곡선 모양 클릭 가능
        mouse "highlight"  # <-- 이 한 줄이면, 버튼에 마우스를 올렸을 때 "highlight" 커서가 표시됨!
        action Show("mystery1_radio")


    imagebutton:
        idle "scene88_water"
        xalign 0.5
        yalign 0.5
        focus_mask True  # 알파 채널을 이용해 곡선 모양 클릭 가능
        mouse "highlight"  # <-- 이 한 줄이면, 버튼에 마우스를 올렸을 때 "highlight" 커서가 표시됨!
        action Show("mystery1_water")


    imagebutton:
        idle "scene88_window"
        xalign 0.5
        yalign 0.5
        focus_mask True  # 알파 채널을 이용해 곡선 모양 클릭 가능
        mouse "highlight"  # <-- 이 한 줄이면, 버튼에 마우스를 올렸을 때 "highlight" 커서가 표시됨!
        action Show("mystery1_window")


    imagebutton:
        idle "scene88_door"
        xalign 0.5
        yalign 0.5
        focus_mask True  # 알파 채널을 이용해 곡선 모양 클릭 가능
        mouse "highlight"  # <-- 이 한 줄이면, 버튼에 마우스를 올렸을 때 "highlight" 커서가 표시됨!
        action Show("mystery1_door")

    # 조사 종료 버튼
    if main_done <= 2:
        textbutton "조사 종료" action Show("investigation_end_few") xpos 50 ypos 100
    elif main_done <= 4:
        textbutton "조사 종료" action Show("investigation_end_some") xpos 50 ypos 100
    else:
        # main_done == 5인 경우
        # 세부조사도 다 끝났는지 체크하고, 끝났다면 자동으로 넘어가게 할 수도 있음
        if sub_done < 6:  # 예: choice_state가 6개라면
            textbutton "조사 종료" action Show("investigation_end_done") xpos 50 ypos 100
        else:
            textbutton "조사 종료" action Show("investigation_end_done") xpos 50 ypos 100
            timer 0.5 action Show("investigation_end_done")


######################################
# 조사 종료 스크린
######################################
screen investigation_end_few():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text "아직 더 조사해보자!"
            textbutton "돌아가기" action Hide("investigation_end_few")

screen investigation_end_some():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text "뭔가 조사할 게 더 있을 것 같은데... 계속 조사하시겠습니까?"
            textbutton "조사 끝내기" action [Hide("investigation_end_some"), Jump("mystery1_finish")]  # 조사 종료
            textbutton "돌아가기" action Hide("investigation_end_some")

screen investigation_end_done():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text "조사를 종료하겠습니까?"
            hbox:
                spacing 20
                textbutton "조사 끝내기" action [Hide("investigation_end_done"), Jump("mystery1_finish")]  # 조사 종료
                textbutton "돌아가기" action Hide("investigation_end_done")

screen investigation_end_done():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text "더 이상 조사할 게 없는 것 같아.."
            hbox:
                spacing 20
                textbutton "조사 끝내기" action [Hide("investigation_end_done"), Jump("mystery1_finish")]  # 조사 종료


######################################
# 조사 하는 스크린
######################################
screen mystery1_person():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text " 가와시마 씨의 등에 진흙과 모래가 묻어 있다.. \n"
            textbutton "닫기" action [
                SetDict(investigation_state, "person", True),
                Hide("mystery1_person"),
                Jump("refresh_investigation_label")
            ]

screen mystery1_radio():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text " 월광 노래가 흘러나오던 테이프 리코더다. \n"
            textbutton "테이프 리코더를 다시 틀어보자." action [
                SetDict(investigation_state, "radio", True),
                Hide("mystery1_radio"),  # 현재 화면 닫기
                Jump("tape_scene_label")  # 라벨로 이동해 대사 처리
            ]
            textbutton "조사 화면으로 돌아가기" action [
                Hide("mystery1_radio"),
                Show("mystery1_investigation")
            ]

screen mystery1_water():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text " 바닥에 물이 흥건히 있다. \n"
            textbutton "무슨 물이지..?" action [
                SetDict(investigation_state, "water", True),
                Hide("mystery1_water"),  # 현재 화면 닫기
                Jump("water_scene_label")  # 라벨로 이동해 대사 처리
            ]
            textbutton "조사 화면으로 돌아가기" action [
                Hide("mystery1_water"),
                Show("mystery1_investigation")
            ]


screen mystery1_window():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text " 밖이 보이는 창문이다. \n"
            textbutton "창문을 더 조사해보자." action [
                SetDict(investigation_state, "window", True),
                Hide("mystery1_window"),  # 현재 화면 닫기
                Jump("window_scene_label")  # 라벨로 이동해 대사 처리
            ]
            textbutton "조사 화면으로 돌아가기" action [
                Hide("mystery1_window"),
                Show("mystery1_investigation")
            ]

screen mystery1_door():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            text " 외부로 나가는 문이다. \n"
            textbutton "문을 더 조사해보자." action [
                SetDict(investigation_state, "door", True),
                Hide("mystery1_door"),  # 현재 화면 닫기
                Jump("door_scene_label")  # 라벨로 이동해 대사 처리
            ]
            textbutton "조사 화면으로 돌아가기" action [
                Hide("mystery1_door"),
                Show("mystery1_investigation")
            ]


######################################
# 조사 하는 화면
######################################
label refresh_investigation_label:
    # 화면이 닫힌 상태이므로, 여기서 다시 조사 스크린을 호출
    call screen mystery1_investigation
    return

label tape_scene_label:
    scene black 
    show scene93 with fade # scene93 배경 설정
    character_conan "뭐지..? 초반에는 아무 소리도 나지 않는걸..?"
    scene black
    call screen mystery1_investigation

label water_scene_label:
    scene black 
    show scene89 with fade # scene93 배경 설정

    menu:
        "물을 맛 본다.":
            show scene90
            character_conan "이 비릿한 짠맛은?!!"
            $ choice_state["water_1"] = True  # 세부 선택지 True
        "냄새를 맡아본다.":
            show scene90
            character_conan "축축한 공기 속에 스며든 이 비릿한 향기... 뭐지?!"
            $ choice_state["water_2"] = True  # 세부 선택지 True

    scene black
    call screen mystery1_investigation

label door_scene_label:
    scene black 
    show scene92 with fade

    menu:
        "문을 열어본다.":
            $ renpy.music.set_volume(0.3, delay=0)  # 음악 볼륨을 줄임
            play sound "lock_door.ogg"
            character_conan "문이 잠겨있는 듯 하다.."
            $ choice_state["door_1"] = True
            $ renpy.music.set_volume(1.0, delay=1)  # 1초 후 원래 볼륨으로 복원
        "문 밖을 바라본다.":
            show scene94
            play sound "sea_sound.ogg"
            character_conan "어두운 밤 바다야."
            $ choice_state["door_2"] = True

    scene black
    stop sound
    call screen mystery1_investigation

label window_scene_label:
    scene black 
    show scene91 with fade

    menu:
        "창문을 열어본다.":
            $ renpy.music.set_volume(0.3, delay=0)  # 음악 볼륨을 줄임
            play sound "lock_door.ogg"
            character_conan "창문이 잠겨있는 듯 하다.."
            $ choice_state["window_1"] = True
            $ renpy.music.set_volume(1.0, delay=1)  # 1초 후 원래 볼륨으로 복원
        "창문 밖을 바라본다.":
            show scene87
            play sound "sea_sound.ogg"
            character_conan "뭐지?! 바다 위에 옷이 있어!"
            $ choice_state["window_2"] = True

    scene black
    stop sound
    call screen mystery1_investigation