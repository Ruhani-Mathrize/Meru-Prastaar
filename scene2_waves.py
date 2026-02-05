from manim import *
import numpy as np

class Scene2_SoundWaves(Scene):
    def construct(self):
        # --- 1. SETUP: PITCH BLACK ---
        self.camera.background_color = "#000000" # Pure Black
        
        # --- 2. THE TEXT (Na Taato...) ---
        # Sanskrit Text
        txt_full = Text("Na Taato Na Mata", font_size=48, color=WHITE)
        self.play(Write(txt_full))
        self.wait(1)
        
        # Split into Syllables
        # Hum 3 distinct parts banayenge
        syllables = VGroup(
            Text("Na", font_size=60, color=BLUE),
            Text("Ta", font_size=60, color=ORANGE),
            Text("To", font_size=60, color=YELLOW)
        ).arrange(RIGHT, buff=2.5) # Thoda gap badhaya taaki waves fit aayein
        
        self.play(Transform(txt_full, syllables))
        
        # --- 3. THE SOUND WAVES (Replacing Shapes) ---
        
        # Helper function to create Wave
        def create_wave(color, width):
            return FunctionGraph(
                lambda x: np.sin(5 * x) * np.exp(-x**2), # Damped Sine Wave shape
                x_range=[-2, 2],
                color=color
            ).stretch_to_fit_width(width).set_stroke(width=4)

        # Wave 1: Na (Short & Sharp)
        wave_na = create_wave(BLUE, width=1.5)
        wave_na.next_to(syllables[0], DOWN, buff=1)
        
        # Wave 2: Ta (Long)
        wave_ta = create_wave(ORANGE, width=3.0)
        wave_ta.next_to(syllables[1], DOWN, buff=1)
        
        # Wave 3: To (Long - Distinct Color)
        wave_to = create_wave(YELLOW, width=3.0)
        wave_to.next_to(syllables[2], DOWN, buff=1)

        # Animate drawing the waves (Left to Right)
        self.play(
            Create(wave_na, run_time=0.8),
            Create(wave_ta, run_time=1.2),
            Create(wave_to, run_time=1.2)
        )
        
        # --- 4. THE LABELS (Fixing the 122 confusion) ---
        
        # Ab hum 1-2-2 nahi, L-G-G dikhayenge jo Book mein hai
        lbl_na = Text("L", font_size=40, color=BLUE).next_to(wave_na, DOWN, buff=0.5)
        lbl_ta = Text("G", font_size=40, color=ORANGE).next_to(wave_ta, DOWN, buff=0.5)
        lbl_to = Text("G", font_size=40, color=YELLOW).next_to(wave_to, DOWN, buff=0.5)
        
        # Subtitles for context
        sub_na = Text("(Laghu)", font_size=20, color=GRAY).next_to(lbl_na, DOWN, buff=0.2)
        sub_ta = Text("(Guru)", font_size=20, color=GRAY).next_to(lbl_ta, DOWN, buff=0.2)
        sub_to = Text("(Guru)", font_size=20, color=GRAY).next_to(lbl_to, DOWN, buff=0.2)
        
        self.play(
            FadeIn(lbl_na, shift=UP),
            FadeIn(lbl_ta, shift=UP),
            FadeIn(lbl_to, shift=UP)
        )
        self.play(Write(sub_na), Write(sub_ta), Write(sub_to))
        
        self.wait(1)

        # --- 5. THE PULSE (Feel the Music) ---
        # Waves beat karengi rhythm mein
        
        # Na (Fast beat)
        self.play(
            wave_na.animate.scale(1.2).set_color(BLUE_A),
            lbl_na.animate.scale(1.2),
            run_time=0.2
        )
        self.play(
            wave_na.animate.scale(1/1.2).set_color(BLUE),
            lbl_na.animate.scale(1/1.2),
            run_time=0.2
        )
        
        # Ta (Long sustain)
        self.play(
            wave_ta.animate.scale(1.1).set_color(ORANGE),
            lbl_ta.animate.scale(1.2),
            run_time=0.6
        )
        self.play(
            wave_ta.animate.scale(1/1.1).set_color(ORANGE),
            lbl_ta.animate.scale(1/1.2),
            run_time=0.4
        )
        
        # To (Long sustain)
        self.play(
            wave_to.animate.scale(1.1).set_color(YELLOW),
            lbl_to.animate.scale(1.2),
            run_time=0.6
        )
        self.play(
            wave_to.animate.scale(1/1.1).set_color(YELLOW),
            lbl_to.animate.scale(1/1.2),
            run_time=0.4
        )
        
        self.wait(2)