from manim import *
import numpy as np

class PinkSoundWave(Scene):
    def construct(self):
        # --- SETUP ---
        self.camera.background_color = "#050505"

        # --- COLORS ---
        BLUE_WAVE = "#00F0FF" 
        PINK_WAVE = "#FF007F" # Hot Pink for Guru

        # --- FONT & SIZE SETUP ---
        hindi_font = "Nirmala UI"
        try:
            test = Text("अ", font=hindi_font)
            font_to_use = hindi_font
            laghu_txt_content = "अ, इ, उ"
            guru_txt_content = "आ, ई, ऊ"
        except:
            font_to_use = "sans-serif"
            laghu_txt_content = "a, i, u"
            guru_txt_content = "aa, ee, oo"

        # Sizes Adjusted
        TITLE_SIZE = 36    # Increased slightly (approx 3-5%)
        SUBTITLE_SIZE = 48 # Decreased by ~10%

        # --- POSITIONING VARS ---
        # Wave ko thoda neeche shift karne ke liye offset
        WAVE_SHIFT_DOWN = 0.6 

        # ==========================================
        # LEFT SIDE: LAGHU (Blue Pulse)
        # ==========================================

        # 1. Create Laghu Wave
        laghu_wave = VGroup()
        for x in np.linspace(-1, 1, 40):
            height = 2.5 * np.exp(-5 * x**2) * (0.5 + 0.5 * np.random.rand()) 
            line = Line(DOWN * height/2, UP * height/2)
            # Position: Left side (-3.5) and Shifted Down
            line.move_to([x - 3.5, -WAVE_SHIFT_DOWN, 0]) 
            line.set_color(BLUE_WAVE)
            line.set_stroke(width=3)
            laghu_wave.add(line)

        laghu_glow = laghu_wave.copy()
        laghu_glow.set_stroke(width=8, opacity=0.3).set_color(BLUE)

        # 2. Text Labels
        # Text ko wave se kaafi upar rakhenge
        label_laghu = Text("LAGHU (Short)", font_size=TITLE_SIZE, color=BLUE_WAVE)
        # Text position: Thoda upar fixed position par
        label_laghu.move_to([-3.5, 2.0, 0]) 
        
        sub_laghu = Text(laghu_txt_content, font=font_to_use, font_size=SUBTITLE_SIZE, color=WHITE)
        sub_laghu.next_to(label_laghu, DOWN, buff=0.3)

        # ==========================================
        # RIGHT SIDE: GURU (Pink Flow)
        # ==========================================

        # 1. Create Guru Wave
        guru_wave = FunctionGraph(
            lambda x: 0.8 * np.sin(10 * x) * np.exp(-0.5 * x**2),
            x_range=[-3, 3],
            color=PINK_WAVE
        )
        # Position: Right side (3.5) and Shifted Down
        guru_wave.move_to([3.5, -WAVE_SHIFT_DOWN, 0])
        guru_wave.set_stroke(width=4)

        guru_glow = guru_wave.copy()
        guru_glow.set_stroke(width=10, opacity=0.3).set_color(PINK)

        # 2. Text Labels
        label_guru = Text("GURU (Long)", font_size=TITLE_SIZE, color=PINK_WAVE)
        label_guru.move_to([3.5, 2.0, 0]) # Align with Laghu label height
        
        sub_guru = Text(guru_txt_content, font=font_to_use, font_size=SUBTITLE_SIZE, color=WHITE)
        sub_guru.next_to(label_guru, DOWN, buff=0.3)

        # ==========================================
        # ANIMATION
        # ==========================================

        # PART 1: LAGHU ENTRY
        self.play(
            FadeIn(laghu_wave),
            FadeIn(laghu_glow),
            Write(label_laghu),
            Write(sub_laghu),
            run_time=1
        )

        # Fast Tick Animation
        self.play(
            laghu_wave.animate.scale(1.2).set_color(WHITE),
            laghu_glow.animate.scale(1.3).set_opacity(0.6),
            run_time=0.1, 
            rate_func=there_and_back
        )
        self.play(
            laghu_wave.animate.set_color(BLUE_WAVE),
            laghu_glow.animate.set_opacity(0.3),
            run_time=0.1
        )
        self.wait(0.5)

        # PART 2: GURU ENTRY
        self.play(
            FadeIn(guru_wave),
            FadeIn(guru_glow),
            Write(label_guru),
            Write(sub_guru),
            run_time=1.5
        )

        # Smooth Stretch Animation
        self.play(
            guru_wave.animate.stretch(1.3, dim=0), # Stretch wider
            guru_glow.animate.stretch(1.3, dim=0),
            run_time=2.5,
            rate_func=there_and_back
        )
        
        # PART 3: LOOPING COMPARISON
        for _ in range(2):
            self.play(
                laghu_wave.animate.scale(1.1),
                guru_wave.animate.scale(1.05),
                run_time=0.6,
                rate_func=there_and_back
            )
        
        self.wait(2)