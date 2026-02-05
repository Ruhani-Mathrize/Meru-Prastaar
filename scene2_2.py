"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *
import numpy as np

class Scene2_2_Ultimate_Snake(ThreeDScene):
    def construct(self):
        # --- CONFIGURATION FOR HIGH QUALITY LOOK ---
        self.camera.background_color = "#000000" # Pitch black for contrast
        # Lighting effect for 3D objects
        self.renderer.camera.light_source.move_to(3*IN + 3*LEFT + 3*UP)

        # --- PART 1: THE RHYTHM (Text) ---
        # Camera starting position (Normal 2D)
        self.set_camera_orientation(phi=0 * DEGREES, theta=-90 * DEGREES)

        lgg_pattern = Tex(r"L \quad -- \quad G \quad -- \quad G", font_size=60, color=BLUE_B)
        lgg_pattern.to_edge(UP, buff=1.5) 
        
        self.play(Write(lgg_pattern))
        self.wait(0.5)

        # --- TEXT SIZE FIX ---
        # Heading size ko 20% chota kar diya (scale 0.8) taaki elegant lage
        title = Text("Bhujangaprayatam", color=GOLD, font_size=40).scale(0.8)
        title.next_to(lgg_pattern, DOWN, buff=0.3)
        
        self.play(FadeIn(title, shift=UP*0.2))
        self.wait(1)

        # --- PART 2: THE REALISTIC 3D MORPHING ---
        
        # 1. Move Camera to Dramatic 3D Angle
        self.play(
            title.animate.to_corner(UL).scale(0.7), # Title ko side mein bhej do
            lgg_pattern.animate.fade(0.5), # Pattern ko halka kar do
        )
        self.move_camera(phi=70 * DEGREES, theta=-30 * DEGREES, zoom=1.2, run_time=2.5)

        # 2. Define the Realistic Snake
        def snake_wave_func(t):
            # Complex wave for natural movement
            return np.array([t, 0.5 * np.sin(2 * t), 0.5 * np.cos(2 * t)])

        # Body (Thick, Gradient Color for Scales effect)
        snake_body = ParametricFunction(
            snake_wave_func,
            t_range=[-4, 4],
            stroke_width=15, # Thoda mota taaki body lage
            color=GOLD, # Base color
            shade_in_3d=True,
        ).set_color_by_gradient(GOLD_E, YELLOW, GOLD_E) # Gradient for shiny scales

        # Head (3D Sphere)
        # Head ko curve ke start point par rakhenge
        start_point = snake_wave_func(4) 
        snake_head = Dot3D(point=start_point, radius=0.15, color=GOLD_A)
        
        # Glow (Atmosphere)
        snake_glow = ParametricFunction(
            snake_wave_func,
            t_range=[-4, 4],
            stroke_width=30,
            color=ORANGE,
            stroke_opacity=0.2,
            shade_in_3d=True,
        )

        snake_group = VGroup(snake_glow, snake_body, snake_head)

        # 3. MORPHING MAGIC (Text melts into Snake)
        # Hum L-G-G text ko Snake mein transform kar rahe hain
        self.play(
            ReplacementTransform(lgg_pattern, snake_group),
            run_time=3,
            rate_func=linear
        )
        
        # --- PART 3: THE LIVING MOVEMENT ---
        # Ab snake ko "Alive" dikhayenge, wo screen par tairta hua aage badhega

        # Copy for animation loop
        living_snake_body = snake_body.copy()
        living_snake_head = snake_head.copy()
        living_snake_glow = snake_glow.copy()
        
        # Group banaya taaki sab saath move karein
        living_snake = VGroup(living_snake_glow, living_snake_body, living_snake_head)
        
        # Remove old static snake, add dynamic one
        self.remove(snake_group)
        self.add(living_snake)

        # Movement Updater
        def slither(mob, dt):
            # Puri body ko x-axis par move karo
            mob.shift(RIGHT * dt * 0.5)
            # Head ko thoda bob (hilna) karao taaki zinda lage
            # (Advanced manipulation avoided to keep code stable, simple shift is smoother)
            
        living_snake.add_updater(slither)
        self.wait(4) # Let it slither for 4 seconds
        
        living_snake.remove_updater(slither)

        # --- PART 4: THE CALCULATION (Grand Finale) ---
        
        # Camera wapis upar le aao calculation ke liye
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, zoom=1, run_time=2)
        
        # Snake ko upar shift karo
        self.play(living_snake.animate.shift(UP * 1.5).scale(0.8))

        # High Quality Slots
        slots = VGroup(*[Square(side_length=0.7, color=WHITE, stroke_width=2) for _ in range(12)])
        slots.arrange(RIGHT, buff=0.15)
        slots.move_to(DOWN * 0.5)
        
        # Numbers
        slot_nums = VGroup(*[Text(str(i+1), font_size=16, font="Arial", color=GRAY_B) for i in range(12)])
        for i, sl in enumerate(slots):
            slot_nums[i].next_to(sl, DOWN, buff=0.1)

        self.play(FadeIn(slots, shift=UP), FadeIn(slot_nums), run_time=1.5)

        # The Equation
        eq_part1 = MathTex(r"2^{12}", font_size=80).next_to(slots, DOWN, buff=1)
        eq_part2 = MathTex(r"=", font_size=80).next_to(eq_part1, RIGHT)
        eq_part3 = MathTex(r"4096", font_size=90, color=GOLD).next_to(eq_part2, RIGHT)

        self.play(Write(eq_part1))
        self.play(Write(eq_part2))
        
        # Blast effect for the result
        self.play(TransformFromCopy(slots, eq_part3), run_time=1.5)
        self.play(Indicate(eq_part3, scale_factor=1.2, color=YELLOW))

        self.wait(2)
        
        # Final Fade

        self.play(FadeOut(Group(living_snake, slots, slot_nums, eq_part1, eq_part2, eq_part3, title)))
