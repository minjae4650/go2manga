# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
image bg bedroom = im.Scale("images/bg_bedroom.jpg", 1920, 1080)
image bg cinema = im.Scale("images/bg_cinema.jpg", 1920, 1080)

# 게임에서 사용할 캐릭터를 정의합니다.
define m = Character('나', color="#c8ffc8")
define f = Character('친구', color="#ffc8c8")


define config.mouse = {
    "default": [("gui/cursors/magnify.png", 24, 24)],  # 기본 돋보기 커서
    "highlight": [("gui/cursors/magnify_red.png", 24, 24)]  # 빨간 돋보기 커서
}

label start:
    # 어두운 화면에서 시작
    scene black with fade

    # 전화벨 소리
    play sound "audio/phone_ring.mp3" loop

    "따르릉 따르릉 ..."

    # 불이 켜지면서 방 배경으로 전환
    scene bg bedroom with fade
    stop sound fadeout 2.0 # 전화벨 소리 점점 줄어듦

    m "어라 전화네.. 누구지?"

    m "00이? 무슨일로 전화한거지?"

    m "여ㅂ.."

    f "야!! 너 전화 왜 이렇게 늦게받아."

    f "오늘 3시 영화 잊은거 아니지?"

    m "어어.. 안 잊었지 물론..! 근데 무슨 영화 보기로 했더라?"

    f "아 그건 영화관에서 알려줄게! 이따 3시에 영화관에서 보는거다~!!"

    m "어? 무슨 영화길ㄹ.. 뚜 뚜 뚜 ... (끊어진 전화)"

    m "에잇 뭐야 끊었잖아. 하여튼 자기 할 만만 하고 끊는다니까"

    m "또 애니메이션 같은거 보자고 하는거 아냐?"

    m "저번에 봤던 주술? 저주?회전인가 뭔가 또 보러 가는건 아니겠지?"

    m "난 그런 오타쿠같은건 싫은데 말이야.. 아무튼 가보면 알겠지?"

    # 3시 영화관
    scene bg cinema with fade

    m "대체 무슨 영화를 보고 싶은건데?"

    f "바로 이거야!"

    # 영화 선택지
    menu:
        "코난":
            m "코난? 그 추리 만화? 그걸 영화관에서도 봐야해? 티비에서 해주잖아~"
            f "너.. 그 발언 진짜 위험한거야. 극장과 티비는 엄연히 다르다고!!!!!"
            m "아무튼 난 애니메이션 진짜 싫다니까~"
            m "저번에 저주회전인가도 너 때문에 3번이나 보러갔잖아!"
            f "주술회전이야!!!!!!!"
            f "흠흠 어쨋든 오늘은 꼭 이걸 봐야해. 따라와."
            "궁시렁대면서도 결국 상영관으로 들어갔다."
            jump conan
        "다른 영화":
            m "이거구나!"
            f "하핫 아니지롱~ 사실 이거지롱~"
            "코난을 보여준다"
            m "코난? 그 추리 만화? 그걸 영화관에서도 봐야해? 티비에서 해주잖아~"
            f "너.. 그 발언 진짜 위험한거야. 극장과 티비는 엄연히 다르다고!!!!!"
            m "아무튼 난 애니메이션 진짜 싫다니까~"
            m "저번에 저주회전인가도 너 때문에 3번이나 보러갔잖아!"
            f "주술회전이야!!!!!!!"
            f "흠흠 어쨋든 오늘은 꼭 이걸 봐야해. 따라와."
            "궁시렁대면서도 결국 상영관으로 들어갔다."
            jump conan

label conan:
    # 영화 시작 화면
    scene black with fade

    # 선택지 등장
    menu:
        "월광의 소나타":
            jump conan_start  # conan_start로 이동
        "월광의 소나타 2편":
            jump conan_start2
        "월광의 소나타 3편":
            jump conan_start3
        "탐정단 서바이벌":
            jump conan_epi2
        "게임 종료":
            return  # 게임 종료


    return
