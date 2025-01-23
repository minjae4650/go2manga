# ======================================================
# 이미지 & 상수 설정
# ======================================================
define SCREEN_WIDTH = 1800  # 화면 너비

image bg_ground = "images/bg_cliff.png"           
image character = im.Scale("images/character.png", 41, 100)
image obstacle = im.Scale("images/obstacle.png", 200, 500)  # '구멍' 이미지

image cliff = im.Scale("images/cliff.png", 1500, 1080)
image cliff_success = im.Scale("images/cliff_success.png", 1500, 1080)
image cliff_fail = im.Scale("images/cliff_fail.png", 1500, 1080)

# ======================================================
# 파이썬 클래스 선언
# ======================================================
init python:
    import random, pygame, time
    from renpy.text.text import Text

    class Dino:
        X_POS = 200
        Y_POS = 600   # 바닥 높이(예: 600)
        Y_POS_DOWN = 630
        JUMP_VEL = 10
        
        def __init__(self):
            self.run_imgs = [Transform("character"), Transform("character")] 
            self.down_imgs = [Transform("character"), Transform("character")] 
            self.jump_img = Transform("character")
            self.dead_img = Transform("character")

            self.is_jump = False 
            self.is_down = False 
            self.is_run = True

            self.step_idx = 0
            self.img = self.run_imgs[0]
            self.jump_velocity = self.JUMP_VEL
            self.x = self.X_POS 
            self.y = self.Y_POS
            self.animation_timer = 0
        
        def animate(self, imgs, dt):
            self.animation_timer += dt
            # 0.1초마다 애니메이션 프레임 변경
            if self.animation_timer > 0.1:
                self.step_idx = (self.step_idx + 1) % len(imgs)
                self.img = imgs[self.step_idx]
                self.animation_timer = 0
        
        def run(self, dt):
            self.animate(self.run_imgs, dt)
            self.x = self.X_POS 
            self.y = self.Y_POS
        
        def down(self, dt):
            self.animate(self.down_imgs, dt)
            self.x = self.X_POS
            self.y = self.Y_POS_DOWN
        
        def jump(self, game_speed, dt):
            self.img = self.jump_img
            if self.is_jump:
                # 점프 중이면 y좌표 변경
                self.y -= self.jump_velocity * 3.6
                # 점프 속도 감소(중력)
                self.jump_velocity -= 0.05 * (game_speed * dt)

            # 착지 처리
            if self.jump_velocity < - self.JUMP_VEL: 
                self.is_jump = False
                self.is_run = True
                self.jump_velocity = self.JUMP_VEL
                self.y = self.Y_POS
        
        def dead(self, x, y):
            self.img = self.dead_img
            self.x = x 
            self.y = y
        
        def update(self, game_speed, dt):
            if self.is_run: 
                self.run(dt)
            if self.is_jump:
                self.jump(game_speed, dt)
            if self.is_down:
                self.down(dt)

    class Obstacle:
        def __init__(self, img, y_pos):
            self.img = img 
            self.x = SCREEN_WIDTH
            self.y = y_pos
        
        def update(self, game_speed, dt):
            self.x -= game_speed * dt
        
        def is_out_screen(self):
            return self.x < - SCREEN_WIDTH

    # ============== 구멍(절벽) 클래스 ==============
    class HoleObstacle(Obstacle):
        def __init__(self):
            y_pos = 680
            hole_img = Transform("obstacle")
            super().__init__(hole_img, y_pos)

    # ============== 메인 게임 로직 ==============
    class DinosaurGame(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.game_speed = 1000
            self.obstacles = []
            
            # ----- (1) 제한 시간 & 경과 시간 설정 -----
            self.time_limit = 10.0      # 예: 10초 뒤 성공 처리
            self.elapsed_time = 0.0
            
            self.bg_x = 0 
            self.bg_y = 680
            self.bg_img = Transform("bg_ground")

            self.game_over = False
            self.dino = Dino()

            self.oldst = None
            self.paused = False 
            self.game_over_delay = None
        
        def move_track(self, dt):
            # 배경 스크롤
            if self.bg_x <= - SCREEN_WIDTH:
                self.bg_x = 0
            self.bg_x -= self.game_speed * dt
        
        def create_obstacle(self):
            # 장애물(=구멍) 동시에 최대 3개까지
            if len(self.obstacles) < 3:
                # 이전 구멍 위치가 x < 200이면 다음 구멍 생성
                if not self.obstacles or (self.obstacles and self.obstacles[-1].x < 200):
                    self.obstacles.append(HoleObstacle())
        
        def update_obstacle(self, dt):
            for obstacle in self.obstacles:
                obstacle.update(self.game_speed, dt)
                if obstacle.is_out_screen():
                    self.obstacles.remove(obstacle)
        
        def check_collision(self, dino_render, obs_render, obs):
            dino_width, dino_height = dino_render.get_size()
            obs_width, obs_height = obs_render.get_size()

            dino_rect = pygame.Rect(self.dino.x, self.dino.y, dino_width, dino_height)
            obs_rect = pygame.Rect(obs.x, obs.y, obs_width, obs_height)

            if dino_rect.colliderect(obs_rect):
                # 만약 구멍과 닿았는데 캐릭터가 바닥(y >= 600)이면 실패
                if self.dino.y >= 600:
                    return True  # 실패
                else:
                    return False  # 점프 중이면 통과
            return False
        
        def visit(self):
            # 화면에 그릴 Displayable 리스트
            return [self.dino.img, self.bg_img] + [obs.img for obs in self.obstacles]
        
        def render(self, width, height, st, at):
            render = renpy.Render(width, height)

            if self.oldst is None:
                self.oldst = st 
            dtime = st - self.oldst
            self.oldst = st

            # 게임 오버나 일시정지가 아니면 진행
            if not self.paused and not self.game_over:
                # (2) 경과 시간 누적
                self.elapsed_time += dtime

                # 시간 제한 도달 시 -> 성공 처리
                if self.elapsed_time >= self.time_limit:
                    self.game_over = True
                    self.game_over_delay = None
                    renpy.jump("game_success")

                self.update_obstacle(dtime)
                self.dino.update(self.game_speed, dtime)
                self.move_track(dtime)

             # 배경 스크롤 그리기
            bg_render = renpy.render(self.bg_img, width, height, st, at)
            render.blit(bg_render, (self.bg_x, self.bg_y))
            render.blit(bg_render, (self.bg_x + width, self.bg_y))

            # 캐릭터 그리기
            dino_render = renpy.render(self.dino.img, width, height, st, at)
            render.blit(dino_render, (self.dino.x, self.dino.y))

            # 장애물(=구멍) 생성 & 표시
            self.create_obstacle()
            for obstacle in self.obstacles:
                obs_render = renpy.render(obstacle.img, width, height, st, at)
                render.blit(obs_render, (obstacle.x, obstacle.y))
                if not self.paused and not self.game_over:
                    if self.check_collision(dino_render, obs_render, obstacle):
                        # 충돌 시 실패 처리
                        self.dino.dead(self.dino.x, self.dino.y)
                        self.game_over = True
                        self.game_over_delay = None
                        renpy.jump("game_over")
                        break

            # 남은 시간 표시
            time_left = max(0, self.time_limit - self.elapsed_time)
            time_text = Text(f"TIME LEFT: {time_left:.1f}", color="#FAFAFA", size=30)
            time_render = renpy.render(time_text, width, height, st, at)
            render.blit(time_render, (width - 300, 40))

            # 일정 주기로 자기 자신을 다시 그리도록 요청
            renpy.redraw(self, 0)
            
            return render
        
        def event(self, event, x, y, st):
            if not self.paused and not self.game_over:
                if event.type == pygame.KEYDOWN:
                    # 점프
                    if (event.key == pygame.K_UP or event.key == pygame.K_SPACE) and not self.dino.is_jump:
                        self.dino.is_down = False
                        self.dino.is_run = False
                        self.dino.is_jump = True
                    # 아래 누르면 앉기
                    elif event.key == pygame.K_DOWN and not self.dino.is_jump:
                        self.dino.is_down = True
                        self.dino.is_run = False
                        self.dino.is_jump = False
                if event.type == pygame.KEYUP and not self.dino.is_jump:
                    self.dino.is_down = False
                    self.dino.is_run = True
                    self.dino.is_jump = False

            # Alt 키로 일시정지 토글
            if event.type == pygame.KEYDOWN and (event.key == pygame.K_LALT or event.key == pygame.K_RALT):
                self.paused = not self.paused
                renpy.redraw(self, 0.1)

            # 게임 오버 상태면 이벤트 무시
            if self.game_over:
                raise renpy.IgnoreEvent()

    # 전역 인스턴스
    dino_game = DinosaurGame()

# ======================================================
# 스크린 & 레이블
# ======================================================
screen start_mini_game():
    text "스페이스 바를 눌러 게임을 시작하세요..." color "#ffffff" size 40 xalign 0.5 yalign 0.5
    key "K_SPACE" action Jump("dinosaur_game")

label start_mini_game:
    scene black
    show cliff
    "간단한 점프 게임(구멍 회피)을 시작합니다!"
    play music "audio/cn08.mp3" volume 0.5
    jump dinosaur_game

label dinosaur_game:
    scene black
    show cliff
    call screen dino_runner_game

screen dino_runner_game():
    add dino_game

# --- (A) 성공 레이블 ---
label game_success:
    scene black
    show cliff_success
    "축하합니다! 시간 안에 무사 통과했습니다!"
    stop music fadeout 2.0
    jump double_headed_arrow
    # menu:
    #     "다시하기":
    #         $ dino_game.__init__()  # 게임 인스턴스 재초기화
    #         jump start_mini_game
    #     "끝내기":
    #         jump double_headed_arrow  # 원하는 레이블로 변경

# --- (B) 실패 레이블 ---
label game_over:
    stop music fadeout 2.0
    scene black
    show cliff_fail
    "게임 오버... 절벽에 떨어졌습니다."
    menu:
        "다시하기":
            $ dino_game.__init__()  # 게임 인스턴스 재초기화
            jump start_mini_game
        "끝내기":
            jump die_ending  # 원하는 레이블로 변경