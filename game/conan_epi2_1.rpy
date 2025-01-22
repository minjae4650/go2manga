image bg quiz_wide = im.Scale("images/quiz_bg.png", 3000, 1324)
image quiz_wide_2 = im.Scale("images/quiz_bg_2.png", 1500, 1080)
image thief_balance = im.Scale("images/thief_balance.png", 1500, 1080)


image white_tree = im.Scale("images/white_tree.png", 1500, 1080)
image bridge_run = im.Scale("images/bridge_run.png", 1500, 1080)
image bridge_walk = im.Scale("images/bridge_walk.png", 1500, 1080)
image children = im.Scale("images/children.png", 1500, 1080)
image this_map = im.Scale("images/this_map.png", 1500, 1080)
image that_map = im.Scale("images/that_map.png", 1500, 1080)
image op1 = im.Scale("images/op1.png", 1500, 1080)
image op2 = im.Scale("images/op2.png", 1500, 1080)


image scene1 = im.Scale("images/scene1.png", 1500, 1080)
image scene2 = im.Scale("images/scene2.png", 1500, 1080)
image scene3 = im.Scale("images/scene3.png", 1500, 1080)
image scene4 = im.Scale("images/scene4.png", 1500, 1080)
image scene5 = im.Scale("images/scene5.png", 1500, 1080)
image scene6 = im.Scale("images/scene6.png", 1500, 1080)
image scene7 = im.Scale("images/scene7.png", 1500, 1080)
image scene8 = im.Scale("images/scene8.png", 1500, 1080)


image scene9 = im.Scale("images/scene9.png", 1500, 1080)
image scene10 = im.Scale("images/scene10.png", 1500, 1080)
image scene11 = im.Scale("images/scene11.png", 1500, 1080)


image scene12 = im.Scale("images/scene12.png", 1500, 1080)
image scene13 = im.Scale("images/scene13.png", 1500, 1080)
image scene14 = im.Scale("images/scene14.png", 1500, 1080)
image scene15 = im.Scale("images/scene15.png", 1500, 1080)
image scene16 = im.Scale("images/scene16.png", 1500, 1080)
image scene17 = im.Scale("images/scene17.png", 1500, 1080)
image scene18 = im.Scale("images/scene18.png", 1500, 1080)
image scene19 = im.Scale("images/scene19.png", 1500, 1080)
image scene20 = im.Scale("images/scene20.png", 1500, 1080)
image scene21 = im.Scale("images/scene21.png", 1500, 1080)
image scene22 = im.Scale("images/scene22.png", 1500, 1080)
image scene23 = im.Scale("images/scene23.png", 1500, 1080)
image scene24 = im.Scale("images/scene24.png", 1500, 1080)
image scene25 = im.Scale("images/scene25.png", 1500, 1080)


image scene26 = im.Scale("images/scene26.png", 1500, 1080)
image scene27 = im.Scale("images/scene27.png", 1500, 1080)
image scene28 = im.Scale("images/scene28.png", 1500, 1080)
image scene29 = im.Scale("images/scene29.png", 1500, 1080)
image scene30 = im.Scale("images/scene30.png", 1500, 1080)
image scene31 = im.Scale("images/scene31.png", 1500, 1080)
image scene32 = im.Scale("images/scene32.png", 1500, 1080)


image scene33 = im.Scale("images/scene33.png", 1500, 1080)
image scene34 = im.Scale("images/scene34.png", 1500, 1080)
image scene35 = im.Scale("images/scene35.png", 1500, 1080)
image scene36 = im.Scale("images/scene36.png", 1500, 1080)
image scene37 = im.Scale("images/scene37.png", 1500, 1080)



screen fixed_button:
    frame:
        align (0.9, 0.1)
        textbutton "map" action Show("map_screen")

screen map_screen:
    tag menu

    frame:
        align (0.5, 0.5)
        has vbox
        add im.Scale("images/map.png", 1000, 700)
        textbutton "닫기" action Hide("map_screen")

transform moveleft:
    xalign 1.0
    linear 0.5 xalign 0.0

transform moveright:
    xalign 0.0
    linear 0.5 xalign 1.0

label conan_epi2:
    scene black

    show scene1 with fade
    agasa "어디 있는거야"

    show scene2
    agasa "오, 여기 있었군"

    show scene3 with fade
    play sound "audio/박사님 웃음소리.mp3"
    agasa "으하하하하하하하"

    scene black with fade
    stop sound fadeout 2.0
    "어딘가 익숙한 네명의 목소리가 들린다."

    show scene4 with fade
    ayumi "박사님, 이거 진짜 지도예요?"
    agasa "그래, 진짜란다"
    mitsuhiko "그럼 정말 보물이 있는 거군요"
    agasa "그건 직접 가서 확인해 보렴"

    show scene5 with fade
    genta "반드시 보물을 찾고 말겠어"
    mitsuhiko "나도!"
    ayumi "아유미도!"

    scene black with fade
    "아, 나 또 들어와진건가?"
    "이 익숙한 나비넥타이..."
    "또 코난에 빙의되었나보군"
    "그나저나 지도와 보물이라.. 뭘까?"

    show scene6 with fade
    conan "그런데 박사님, 저런 수상한 지도를 어디서 구하셨어요?"

    show scene7 with fade
    agasa "궁금하냐?"
    agasa "끝까지 가 보면 알 수 있을 거다"

    show scene8 with fade
    agasa "그럼 난 여기서 낚시를 하고 있을테니"
    agasa "너희는 실컷 즐기고 오렴"

    show screen fixed_button

    menu:
        "박사님과 더 대화해보기":
            show white_tree with fade
            agasa "우리가 지금 있는 곳은 백골나무란다"
            agasa "우선 런던 다리를 향해 가 보거라"
            jump london_bridge
        "바로 출발하기":
            call screen quiz_wide


screen quiz_wide():
    modal True

    viewport:
        child_size (3000, 1324)
        xalign 0.0 yalign 0.0
        draggable True
        xinitial 1.0
        yinitial 1.0
        add "bg quiz_wide" align (0.0, 0.0)

    text "화면을 뒤져 지금 있는 곳을 알아내세요" xpos 700 ypos 200
    textbutton "정답 입력":

        action Jump("answer_input")

    use fixed_button
    use quick_menu


label answer_input:

    $ answer = renpy.input("정답을 입력하세요")

    if answer.strip() == "백골나무":
        "그래, 우리는 지금 백골나무에 있어"
        jump london_bridge
    else:
        "아닌 것 같아. 다시 생각해보자"
        call screen quiz_wide


label london_bridge:
    scene black

    show scene9 with fade
    ayumi "코난, 너는 어떤 보물일 것 같아?"
    conan "아직 보물인지 확실하지 않으니까.."

    show scene10 with fade
    genta "보물이 확실해"
    genta "틀림 없이 보물일거야. 그렇지, 미츠히코?"
    mitsuhiko "맞아, 다이아몬드 같은 보석이거나"
    mitsuhiko "어쩌면 숨겨 둔 금괴일지도 몰라"
    genta "그러면 좋겠다"
    mitsuhiko "당연하지"
    conan "(그럴리가 있겠냐)"

    show scene11 with fade
    menu:
        "런던 다리에 도착했다. 삐걱삐걱 소리가 들리는 듯 한데 어떻게 할까?"
        "빠르게 뛰어간다":
            conan "뛰어!!!"
            show bridge_run
            "으아아아아아아!!!!!!"
            jump hand_of_devil
        "조심조심 걸어간다":
            conan "얘들아 불안하니까 조심조심 걸어가자"
            ayumi "응, 알았어. 코난"
            jump hand_of_devil


label hand_of_devil:

    scene black

    show scene12 with fade
    mitsuhiko "이름이 런던 다리라서 떨어질까 봐 조마조마했어"
    conan "영화에서 이런 다리는 꼭 끊어지니까"
    "하하하하하하하하하!"


    play sound "audio/다리 끊어지는.mp3"
    show scene13 with fade
    pause 2.0

    show scene14 with fade
    ayumi "말도 안 돼"
    genta "웃어넘길 일이 아니잖아"
    conan "(박사님도 참 우리를 이렇게 위험한 곳에 오게 하시다니)"
    conan "(이제 어떻게 돌아가냐고요)"

    show scene15 with fade

    show scene16 with fade
    mistery_man3 "역시 이 근방은 나침반이 말을 안 듣네요"
    mistery_man2 "그 녀석은 왜 이런 산속에 보물을 숨긴 거야?"
    mistery_man3 "그 녀석은 미스터리물을 좋아했으니까요"
    mistery_man2 "아무리 그래도 너무 지나쳐"

    show scene17 with fade
    mistery_man2 "나 참, 지도에선 5그루던데 여긴 4그루뿐이야"
    mistery_man2 "진짜 여기 맞아?"
    mistery_man3 "그 녀석도 참 운이 없어요"
    mistery_man3 "곧 보물이 손에 들어올 테데 사고로 죽다니 말이죠"

    show scene18 with fade
    mistery_man2 "이봐, 중요한 보물이 걸려 있다고"
    mistery_man2 "대답은 똑바로 해"

    menu:
        "수상한 남자들이 싸우고 있는 것 같다. 어떻게 할까?"
        "말을 걸어본다":
            show children with fade
            conan "위험하잖아요 아저씨"
            ayumi "담뱃불은 잘 꺼서 버리셔야죠"
            conan "산불이라도 나면 어쩌시려고요"
            mistery_man2 "너희들은 뭐냐?"
            genta "저희는 어린이 탐정단이에요"
            show this_map with fade
            conan "(뭐야, 이 지도 엄청 비슷하게 생겼네)"
            mistery_man2 "꼬맹이, 뭘 보는 거냐?"
            conan "안 봤는데요"
            show op1 with fade
            mistery_man2 "이봐, 가자"
            mistery_man3 "가다니, 어디로요?"
            mistery_man2 "잔말 말고 따라와"
            mistery_man3 "빨리"
            mistery_man2 "아파요"
        "좀 더 지켜본다":
            mistery_man3 "아이고, 알겠다고"
            show that_map with fade
            conan "(뭐야, 저 지도 엄청 비슷하게 생겼네)"
            show op2 with fade
            mistery_man2 "이봐, 가자"
            mistery_man3 "가다니, 어디로요?"
            mistery_man2 "잔말 말고 따라와"
            mistery_man3 "빨리"
            mistery_man2 "아파요"

    show scene19 with fade
    conan "(저 사람들은 등산하러 왔다기엔 뭔가 이상해)"
    "이상한 부분 찾기 게임~~(정장, 가죽구두, 지도)"

    show scene20 with fade
    ayumi "얘들아, 지금 우리가 악마의 손에 있는 거 맞지?"
    mitsuhiko "아마 그런 것 같은데"
    genta "코난, 삼나무가 4그루뿐인데 여기 맞아?"
    conan "그래, 여기야"

    "5번째 삼나무를 찾아라"
    conan "봐, 이게 5번째 삼나무야"

    show scene21 with fade
    mitsuhiko "근데 나침반이 말을 안듣네"
    conan "여길 보면 돼"

    call screen tree_ring_puzzle



init python:
    import pygame

    def ring_correct():
        
        renpy.hide_screen("tree_ring_puzzle")
        renpy.jump("after_tree_ring")
        return
    def ring_wrong():
        return
    def mz_success():
        renpy.hide_screen("thief_balance")
        renpy.jump("maze_success")
    def mz_fail():
        renpy.hide_screen("thief_balance")
        renpy.jump("maze_fail")
    def set_mouse_pos(x, y):
        pygame.mouse.set_pos([x, y])

screen tree_ring_puzzle():
    modal True

    default angle = 0
    default error_msg = ""

    frame:
        align (0.5, 0.5)
        xsize 1010
        ysize 800



        has fixed
        add im.Scale("images/나이테.jpg", 1000, 700) xalign 0.0 yalign 0.0

        add Transform("images/나침반.png", rotate=angle, size=(200, 200)) xpos 10 ypos 10

        text "나침반을 알맞은 방향으로 돌려주세요" xalign 0.5 yalign 0.1

        if error_msg:
            text error_msg xalign 0.5 yalign 0.5

        textbutton "닫기":
            action Hide("tree_ring_puzzle")
            xpos 20
            ypos 730

        textbutton "회전":
            xpos 110
            ypos 730
            action [SetScreenVariable("error_msg", ""), SetScreenVariable("angle", (angle + 90) % 360)]

        textbutton "정답 확인":
            xpos 200
            ypos 730
            action If((angle == 270), Function(ring_correct), SetScreenVariable("error_msg", "흠.. 다시 생각해보자"))

    use quick_menu


label after_tree_ring:
    show scene22 with fade
    conan "이쪽 나이테가 간격이 더 넓지?"
    conan "햇빛을 더 많이 받아서 성장이 빠르기 때문이래"

    show scene23 with fade
    ayumi "그럼 저쪽이 남쪽이구나"
    mitsuhiko "그래서 어느 길로 가면 돼?"
    conan "지도 좀 줘봐"

    "악마의 손 그 좁은 문으로 들어가라"

    show scene24 with fade
    conan "악마의 손은 왼손이니까 왼쪽의 두 길이겠지"
    conan "좁은 문으로 들어가라고 했으니까"
    conan "폭이 좁은 맨 왼쪽 길로 가면 돼"

    show scene25 with fade
    mistery_man2 "어째서 저 녀석들이 저 지도를 가지고 있지?"
    mistery_man3 "그나저나 똑똑한 꼬맹이네요"
    mistery_man2 "아무튼 선수를 빼앗기지 않게 서두르지"
    mistery_man3 "네"

    jump spotted_strap


label spotted_strap:
    scene black

    show scene26 with fade
    genta "아까 그 사람들 뭔가 수상했어"
    ayumi "맞아, 틀림없이 우리와 같은 보물을 찾고 있을 거야"
    mitsuhiko "그래, 아까 보물이라고 했으니까"
    genta "맞아 확실해"

    play sound "audio/snake.mp3"
    show scene27 with fade
    pause 2.0

    show scene28 with fade
    pause 1.0

    play sound "audio/splash.mp3"
    show scene29 with fade
    pause 2.0


    show scene30 with fade
    mitsuhiko "누가 좀 살려 주세요"
    genta "정신 차려, 미츠히코"

    show scene31 with fade
    genta "똑바로 서 봐"
    mitsuhiko "어라"

    show scene32
    mitsuhiko "죽는 줄 알았네"
    "하하하하하하하하"

label foot_of_walton:
    scene black

    show scene33 with fade
    play sound "audio/not_matches.mp3"
    mitsuhiko "아무리 좋은 캠핑용 성냥도 젖으면 소용없네"
    genta "젠장, 모닥불을 피워서 젖은 옷을 말리려고 했는데"
    conan "할 수 있어! 가지고 있는걸 모아볼까?"

    "모닥불 피우기~"
    show scene34 with fade

    show scene35 with fade
    mitsuhiko "그런데 정말 끝까지 찾아갈 수 있을까?"
    genta "아까 그 언덕은 어디지? 거길 또 오르긴 싫은데"
    conan "괜찮아"

    show scene36 with fade
    conan "지금 이 근처니까 이쪽으로 이렇게 돌아가면"
    conan "다음 목적지에 도착할 수 있을 거야"
    show scene37 with fade
    genta "좋았어, 그럼 출발하자"

    call screen maze_announce  

label maze_start:
    show screen thief_balance  

screen maze_announce():
    modal True

    add im.Scale("images/thief_balance.png", 1500, 1080) xalign 0.5 yalign 0.5

    frame:
        align (0.5, 0.5)
        has vbox
        text "아슬아슬 절벽을 탈출해야 합니다.\n마우스커서가 절벽으로 떨어지지않도록 주의하면서 통과하세요." xalign 0.5
        textbutton "시작" action [Hide("maze_announce"), Jump("maze_start")] xalign 0.5

screen thief_balance():
    modal True

    on "show" action Function(set_mouse_pos, 700, 1120)

    add im.Scale("images/thief_balance.png", 1500, 1080) xalign 0.5 yalign 0.5
    frame:
        align (0.5, 0.5)
        xsize 962
        ysize 912

        add im.Scale("images/image 4.png", 950, 900)


        imagebutton:
            idle im.Scale("images/maze_hover.png", 900, 900) xalign 0.5 yalign 0.5

            focus_mask True
            action NullAction()
            hovered Function(mz_fail)
            unhovered NullAction()


        imagebutton:
            idle im.Scale("images/maze_exit.png", 50, 50)
            hover im.Scale("images/maze_exit.png", 50, 50)
            focus_mask True
            action Function(mz_success)
            xpos 893
            ypos 85

label maze_fail:

    scene black
    show text "실패" at truecenter
    pause 2.0
    hide text
    jump die_ending

label maze_success:

    scene black
    show text "성공" at truecenter
    pause 2.0
    hide text
    jump vallet_of_weissmuller

label vallet_of_weissmuller:
    scene black
    jump start_mini_game