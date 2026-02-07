from manim import *
import numpy as np
import random

class SymphonyArchitectureFixed(ThreeDScene):
    def construct(self):
        # --- SETUP ---
        self.camera.background_color = "#050505"
        
        # Colors
        BLUE_NEON = "#00F0FF" 
        PINK_NEON = "#FF007F" 
        GOLD_ACCENT = "#FFD700"

        # --- PART 1: RECREATE WAVES (Continuity) ---
        
        # Laghu Wave (Blue Spikes)
        laghu_wave = VGroup()
        for x in np.linspace(-1, 1, 40):
            height = 2.0 * np.exp(-5 * x**2)
            line = Line(DOWN * height/2, UP * height/2)
            line.move_to([x - 3.5, 0, 0]) 
            line.set_color(BLUE_NEON).set_stroke(width=3)
            laghu_wave.add(line)

        # Guru Wave (Pink Flow)
        guru_wave = FunctionGraph(
            lambda x: 0.8 * np.sin(10 * x) * np.exp(-0.5 * x**2),
            x_range=[-3, 3],
            color=PINK_NEON
        )
        guru_wave.move_to([3.5, 0, 0])

        # Text Labels
        label_laghu = Text("LAGHU", font_size=34, color=BLUE_NEON).move_to([-3.5, 2.0, 0])
        label_guru = Text("GURU", font_size=34, color=PINK_NEON).move_to([3.5, 2.0, 0])

        self.add(laghu_wave, guru_wave, label_laghu, label_guru)
        self.wait(1)

        # ==========================================
        # PART 2: THE TRANSFORMATION (Waves to Bricks)
        # ==========================================

        # Create The Bricks
        brick_blue = Cube(side_length=1.5)
        brick_blue.set_color(BLUE_NEON).set_opacity(0.8).set_gloss(1.0)
        brick_blue.move_to([-2, 0, 0]) 

        brick_pink = Cube(side_length=1.5)
        brick_pink.set_color(PINK_NEON).set_opacity(0.8).set_gloss(1.0)
        brick_pink.move_to([2, 0, 0]) 

        # Camera goes 3D
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)

        # Animation: Waves morph into Bricks
        # FIX: Using 'smooth' rate_func which is universally supported
        self.play(
            FadeOut(label_laghu), FadeOut(label_guru),
            ReplacementTransform(laghu_wave, brick_blue),
            ReplacementTransform(guru_wave, brick_pink),
            run_time=1.5,
            rate_func=smooth 
        )
        
        # Bricks clash center
        self.play(
            brick_blue.animate.move_to([-0.8, 0, 0]),
            brick_pink.animate.move_to([0.8, 0, 0]),
            run_time=0.5
        )

        # ==========================================
        # PART 3: THE IMARAT (Building the Structure)
        # ==========================================

        # Move Camera back
        self.move_camera(phi=75 * DEGREES, theta=45 * DEGREES, zoom=0.5, run_time=3)

        # Generate Structure
        imarat_bricks = VGroup()
        layers = 6 

        for y in range(layers):
            width = layers - y
            for x in range(width):
                for z in range(width):
                    if (x + y + z) % 2 == 0:
                        color = BLUE_NEON
                    else:
                        color = PINK_NEON
                    
                    b = Cube(side_length=1.0)
                    b.set_color(color).set_opacity(0.9).set_gloss(0.5)
                    b.set_stroke(color, width=1, opacity=0.5)
                    
                    offset = (layers - width) * 0.5
                    pos_x = (x + offset) * 1.05 - (layers * 0.5)
                    pos_y = y * 1.05 - 2 
                    pos_z = (z + offset) * 1.05 - (layers * 0.5)
                    
                    b.move_to([pos_x, pos_y, pos_z])
                    imarat_bricks.add(b)

        self.remove(brick_blue, brick_pink)
        
        # Animation: Construction
        self.play(
            LaggedStart(
                *[
                    FadeIn(b, shift=UP*5) 
                    for b in imarat_bricks
                ],
                lag_ratio=0.01
            ),
            run_time=4,
            rate_func=smooth # Safe function
        )

        # ==========================================
        # PART 4: CINEMATIC CLIMAX
        # ==========================================

        # Floating particles
        particles = VGroup()
        for _ in range(30):
            p = Dot(radius=0.05, color=GOLD_ACCENT)
            p.move_to([
                random.uniform(-4, 4),
                random.uniform(-2, 5),
                random.uniform(-4, 4)
            ])
            particles.add(p)
            
        self.play(
            FadeIn(particles, shift=UP),
            run_time=2
        )

        # Drone Rotation
        self.begin_ambient_camera_rotation(rate=0.2)
        
        # Pulse
        self.play(
            imarat_bricks.animate.set_opacity(1.0),
            rate_func=there_and_back,
            run_time=1
        )
        
        self.wait(3)