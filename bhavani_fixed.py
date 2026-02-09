from manim import *
import random
import numpy as np

class BhavaniDivineFixed(ThreeDScene):
    def construct(self):
        # --- 🎬 SETUP ---
        self.camera.background_color = "#050200" # Pitch Dark
        
        # --- 🎨 COLORS (METALLIC GOLD) ---
        GOLD_1 = "#FFF8DC" # Cornsilk (Light)
        GOLD_2 = "#FFD700" # Pure Gold
        GOLD_3 = "#B8860B" # Dark Gold
        
        CYAN_NEON = "#00F0FF" 
        PINK_NEON = "#FF007F" 

        # --- FONT ---
        hindi_font = "Nirmala UI"
        try:
            test = Text("अ", font=hindi_font)
            font_to_use = hindi_font
        except:
            font_to_use = "sans-serif"

        # ==========================================
        # PART 1: THE DIVINE CHANT
        # ==========================================
        
        lines = [
            "न तातो न माता न बन्धुर्न दाता",
            "न पुत्रो न पुत्री न भृत्यो न भर्ता ।",
            "न जाया न विद्या न वृत्तिर्ममैव",
            "गतिस्त्वं गतिस्त्वं त्वमेका भवानि ॥१॥"
        ]

        shlok_group = VGroup()
        for line in lines:
            t = Text(line, font=font_to_use, font_size=36)
            t.set_color_by_gradient(GOLD_1, GOLD_2, GOLD_3)
            shlok_group.add(t)

        shlok_group.arrange(DOWN, buff=0.6)
        
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(
                        FadeIn(line, shift=UP*0.5),
                        line.animate.set_opacity(1) 
                    )
                    for line in shlok_group
                ],
                lag_ratio=0.5
            ),
            run_time=6 
        )
        self.wait(1)

        # ==========================================
        # PART 2: THE ISOLATION
        # ==========================================

        target_bhavani = Text("भवानि", font=font_to_use, font_size=36)
        target_bhavani.set_color_by_gradient(GOLD_1, GOLD_2)
        # Position match
        target_bhavani.move_to(shlok_group[-1].get_right() + LEFT * 1.5)
        
        self.play(
            FadeOut(shlok_group), 
            FadeIn(target_bhavani), 
            run_time=2
        )
        
        # Move to center
        self.play(
            target_bhavani.animate.move_to(ORIGIN).scale(3).set_color(GOLD_2),
            run_time=2,
            rate_func=rate_functions.smooth
        )
        
        # Glow
        glow = Circle(radius=2, color=GOLD_1, fill_opacity=0.2).move_to(ORIGIN)
        glow.set_stroke(width=0)
        self.play(FadeIn(glow), run_time=1)
        self.play(FadeOut(glow))

        # ==========================================
        # PART 3: EXPLOSION & BINARY
        # ==========================================

        particles = VGroup()
        for _ in range(200):
            p = Dot(radius=0.04, color=GOLD_2)
            p.move_to(target_bhavani.get_center() + [random.uniform(-2, 2), random.uniform(-0.8, 0.8), 0])
            particles.add(p)

        # FIX: Used standard rate function here
        self.play(
            ReplacementTransform(target_bhavani, particles),
            run_time=0.8,
            rate_func=rate_functions.ease_out_expo 
        )

        self.play(
            particles.animate.scale(1.5).rotate(PI/2),
            run_time=1.5
        )

        # Form Binary
        binary_one = Text("1", font_size=80, color=CYAN_NEON).move_to(LEFT)
        binary_zero = Text("0", font_size=80, color=PINK_NEON).move_to(RIGHT)
        binary_group = VGroup(binary_one, binary_zero)
        
        self.play(
            ReplacementTransform(particles[:100], binary_one),
            ReplacementTransform(particles[100:], binary_zero),
            run_time=1.5
        )
        
        lbl = Text("Binary Pattern", font_size=24, color=GRAY).next_to(binary_group, DOWN)
        self.play(FadeIn(lbl))
        self.wait(0.5)

        # ==========================================
        # PART 4: MERU PRASTAAR (3D PYRAMID)
        # ==========================================
        
        self.play(FadeOut(binary_group), FadeOut(lbl))

        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)

        pyramid_group = VGroup()
        rows = 5
        block_size = 1.0
        
        for r in range(rows):
            for c in range(r + 1):
                block = Cube(side_length=block_size)
                block.set_color(GOLD_3) 
                block.set_stroke(color=GOLD_1, width=2) 
                block.set_gloss(1.0) 
                
                x_pos = (c - r / 2) * (block_size + 0.1)
                y_pos = -r * (block_size + 0.1) + 2 
                
                block.move_to([x_pos, y_pos, 0])
                pyramid_group.add(block)

        # Blocks fall from sky
        self.play(
            LaggedStart(
                *[
                    FadeIn(b, shift=UP * 5) 
                    for b in pyramid_group
                ],
                lag_ratio=0.1
            ),
            run_time=4
        )
        
        self.play(
            pyramid_group.animate.set_color(GOLD_2).set_opacity(0.8),
            run_time=1.5
        )
        
        self.begin_ambient_camera_rotation(rate=0.2)
        
        final_title = Text("MERU PRASTAAR", font="Georgia", color=GOLD_1, font_size=40)
        self.add_fixed_in_frame_mobjects(final_title)
        final_title.to_edge(UP)
        
        self.play(Write(final_title))
        self.wait(3)