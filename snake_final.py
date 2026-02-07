from manim import *
import numpy as np
import random  # <--- Yeh zaruri hai particles ke liye

class SnakeRhythmFinal(Scene):
    def construct(self):
        # --- 🎬 SETUP 🎬 ---
        self.camera.background_color = "#050200" # Dark Warm Background

        # --- 🎨 COLORS 🎨 ---
        GOLD_TEXT = "#FFD700" 
        ORANGE_MARK = "#FF4500"
        SNAKE_GLOW = "#FF8C00" # Orange Wave Line

        # --- DATA SETUP 📝 ---
        # 12 Syllables of Bhavani Ashtakam
        syllables = [
            "न", "ता", "तो",   # Set 1 (L G G)
            "न", "मा", "ता",   # Set 2 (L G G)
            "न", "ब", "न्धु",  # Set 3 (L G G)
            "र्न", "दा", "ता"  # Set 4 (L G G)
        ]
        
        # Rhythm Markers
        markers = ["|", "S", "S"] * 4 

        # --- FONT SETUP 🅰️ ---
        hindi_font = "Nirmala UI"
        try:
            test = Text("अ", font=hindi_font)
            font_to_use = hindi_font
        except:
            font_to_use = "sans-serif"
            syllables = ["Na", "Taa", "To", "Na", "Maa", "Taa", "Na", "Ban", "Dhu", "Na", "Daa", "Taa"]

        # ==========================================
        # SCENE 1: THE DECODING (Na Ta To) 🔍
        # ==========================================
        
        demo_group = VGroup()
        for i in range(3):
            s_text = Text(syllables[i], font=font_to_use, font_size=60, color=GOLD_TEXT)
            m_text = Text(markers[i], font="Verdana", font_size=40, color=ORANGE_MARK)
            m_text.next_to(s_text, UP, buff=0.3)
            pair = VGroup(s_text, m_text)
            demo_group.add(pair)

        demo_group.arrange(RIGHT, buff=0.8)
        
        math_label = Text("L   -   G   -   G", font_size=36, color=ORANGE_MARK)
        math_label.next_to(demo_group, DOWN, buff=0.5)

        # Animate Entry
        self.play(
            LaggedStart(*[FadeIn(x, shift=UP) for x in demo_group], lag_ratio=0.2),
            run_time=2
        )
        self.play(Write(math_label))
        self.wait(1)

        # ==========================================
        # SCENE 2: THE ASSEMBLY (12 Syllables) 🧩
        # ==========================================

        self.play(FadeOut(demo_group), FadeOut(math_label))

        snake_body = VGroup()
        for i in range(12):
            s_text = Text(syllables[i], font=font_to_use, font_size=48, color=GOLD_TEXT)
            m_text = Text(markers[i], font="Verdana", font_size=30, color=ORANGE_MARK)
            m_text.next_to(s_text, UP, buff=0.2)
            n_text = Text(str(i+1), font_size=20, color=GRAY)
            n_text.next_to(s_text, DOWN, buff=0.2)

            segment = VGroup(s_text, m_text, n_text)
            snake_body.add(segment)

        snake_body.arrange(RIGHT, buff=0.6)
        snake_body.move_to(ORIGIN)

        self.play(
            LaggedStart(*[FadeIn(s, scale=0.5) for s in snake_body], lag_ratio=0.1),
            run_time=3
        )
        self.wait(1)

        # ==========================================
        # SCENE 3: THE SNAKE MOTION (Magic!) 🐍✨
        # ==========================================

        # 1. Path
        snake_path = FunctionGraph(
            lambda x: 0.8 * np.sin(2 * x),
            x_range=[-7, 7],
            color=SNAKE_GLOW
        )
        snake_path.set_stroke(width=2, opacity=0.5)

        # 2. Tracker
        phase_tracker = ValueTracker(0)

        # 3. Updater Function
        def update_snake(mob):
            phase = phase_tracker.get_value()
            for i, segment in enumerate(mob):
                x_pos = (i * 0.8) - 4.5
                y_pos = 0.8 * np.sin(2 * (x_pos + phase))
                
                segment.move_to([x_pos, y_pos, 0])
                
                # Rotation logic
                slope = np.cos(2 * (x_pos + phase))
                angle = np.arctan(slope) * 0.5 
                segment.rotate(angle - segment.get_angle())

        self.play(Create(snake_path), run_time=1)
        snake_body.add_updater(update_snake)

        # 4. Animate Crawling
        self.play(
            phase_tracker.animate.set_value(-2 * PI),
            run_time=6,
            rate_func=linear
        )

        # 5. Particles (Ab ye chalega!)
        particles = VGroup()
        for _ in range(25):
            p = Dot(color=ORANGE_MARK, radius=0.05)
            p.move_to([random.uniform(-5, 5), random.uniform(-1, 1), 0])
            particles.add(p)
            
        self.play(FadeIn(particles))
        
        # 6. Continue
        self.play(
            phase_tracker.animate.set_value(-4 * PI),
            particles.animate.shift(LEFT*3).set_opacity(0),
            run_time=6,
            rate_func=linear
        )

        snake_body.remove_updater(update_snake)
        self.wait(2)