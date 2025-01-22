# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('나', color="#c8ffc8")

define config.mouse = {
    "default": [("gui/cursors/magnify.png", 24, 24)],  # 기본 돋보기 커서
    "highlight": [("gui/cursors/magnify_red.png", 24, 24)]  # 빨간 돋보기 커서
}

label start:

    e "새로운 렌파이 게임을 만들었군요."

    e "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    # 선택지 등장
    menu:
        "코난 보기":
            jump conan_start  # conan_start로 이동
        "추리하러가기":
            jump mystery1
        "2편":
            jump conan_start2
        "게임 종료":
            return  # 게임 종료

    return
