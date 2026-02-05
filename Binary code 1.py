"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *
import numpy as np

class Scene2_TheLoneliness(ThreeDScene):
    def construct(self):
        # --- CONFIGURATION (Cinematic Look) ---
        self.camera.background_color = "#0a0a0a" # Dark Cinematic Background
        
        # --- PART 1: THE TEXT (Na Taato, Na Mata) ---
        # Sanskrit Text (Transliterated for rendering ease, or use Hindi font if configured)
        text_quote = Text("Na Taato, Na Mata", font_size=48, color=WHITE)
        sub_text = Text("(No Father, No Mother)", font_size=24, color=GRAY).next_to(text_quote, DOWN)
        
        self.play(Write(text_quote), FadeIn(sub_text))
        self.wait(1)
        
        # Focus on "Na Ta To"
        # We isolate the syllables visually
        syllables = VGroup(
            Text("Na", color=RED),
            Text("Ta", color=GOLD),
            Text("To", color=GOLD)
        ).arrange(RIGHT, buff=1.5)
        
        self.play(
            FadeOut(sub_text),
            Transform(text_quote, syllables)
        )
        self.wait(1)

        # --- PART 2: THE DECODING (Laghu vs Guru) ---
        # 1. Show Beats below syllables
        # Na = 1 (Short), Ta = 2 (Long), To = 2 (Long)
        
        # Visual representation: 1 is a Dot, 2 is a Dash/Line
        beat_1 = Dot(radius=0.15, color=RED).next_to(syllables[0], DOWN)
        beat_2 = RoundedRectangle(width=0.8, height=0.15, corner_radius=0.05, color=GOLD).next_to(syllables[1], DOWN)
        beat_3 = RoundedRectangle(width=0.8, height=0.15, corner_radius=0.05, color=GOLD).next_to(syllables[2], DOWN)
        
        beats_group = VGroup(beat_1, beat_2, beat_3)

        self.play(
            FadeIn(beat_1, scale=0.5),
            FadeIn(beat_2, scale=0.5),
            FadeIn(beat_3, scale=0.5)
        )
        
        # Convert to Numbers
        num_1 = MathTex("1", color=RED).next_to(beat_1, DOWN)
        num_2 = MathTex("2", color=GOLD).next_to(beat_2, DOWN)
        num_3 = MathTex("2", color=GOLD).next_to(beat_3, DOWN)
        
        labels = VGroup(
            Text("Laghu (Short)", font_size=20, color=RED).next_to(num_1, DOWN),
            Text("Guru (Long)", font_size=20, color=GOLD).next_to(num_2, DOWN),
            Text("Guru (Long)", font_size=20, color=GOLD).next_to(num_3, DOWN)
        )

        self.play(Write(num_1), Write(num_2), Write(num_3))
        self.play(FadeIn(labels))
        self.wait(2)

        # --- PART 3: THE SNAKE (BHUJANGA PRAYATA) IN 3D ---
        # Transition to 3D View
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, zoom=0.8, run_time=2)
        
        # Move current 2D elements to the top left to make space
        flat_group = VGroup(syllables, beats_group, num_1, num_2, num_3, labels)
        self.play(flat_group.animate.to_corner(UL).scale(0.6))

        # Create the Sine Wave (The Snake Motion)
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            z_range=[-2, 2, 1],
            x_length=10,
            y_length=4,
            z_length=4
        ).add_coordinates()
        
        # Hide axes lines for cleaner look, keep just the wave context
        axes.set_opacity(0.3)

        # The Wave Curve (Bhujanga Prayata Style)
        # Represents the rhythm flow: Short rise, Long fall
        snake_curve = ParametricFunction(
            lambda t: np.array([t, np.sin(3*t), np.cos(3*t)]), # Helix/Snake motion
            t_range=np.array([-PI, PI]),
            color=GOLD,
            stroke_width=6,
            shade_in_3d=True
        )

        snake_text = Text("Bhujanga-Prayata (Snake Motion)", font_size=36, color=YELLOW)
        snake_text.to_edge(DOWN)
        
        # Animate the drawing of the curve
        self.play(Create(axes))
        self.play(Create(snake_curve, run_time=3, rate_func=linear))
        
        # Add a glowing sphere traveling on the curve (The "Beat")
        beat_sphere = Sphere(radius=0.1, color=RED).move_to(snake_curve.get_start())
        
        self.add_fixed_in_frame_mobjects(snake_text) # Text stays flat
        self.play(Write(snake_text))
        
        # Loop the movement on the curve
        self.play(MoveAlongPath(beat_sphere, snake_curve), run_time=4, rate_func=linear)
        
        # Final Dramatic Rotation
        self.begin_ambient_camera_rotation(rate=0.2)

        self.wait(3)
