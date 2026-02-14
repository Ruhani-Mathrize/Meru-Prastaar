"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class MathrizeUltaLogic(ThreeDScene):
    def construct(self):
        # 1. Cinematic 3D Environment Setup
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        self.camera.background_color = "#000000" # Pure Black Background jaisa aapne kaha

        # ---------------------------------------------------------
        # UPGRADED HEADING: 'प्रतिलोम' (Pratiloma)—
        # ---------------------------------------------------------
        # Font aap apne system ke hisaab se change kar sakti hain agar Hindi theek se na aaye
        title_text = Text("'प्रतिलोम' (Pratiloma)—", font="sans-serif", weight=BOLD).scale(0.9)
        title_text.set_color_by_gradient("#00FFFF", "#9D00FF") # Cyan to Purple gradient
        title_text.to_corner(UL)
        
        # Ek cinematic glowing underline
        underline = Line(LEFT, RIGHT, color="#00FFFF").match_width(title_text).next_to(title_text, DOWN, buff=0.1)
        
        title_group = VGroup(title_text, underline)
        self.add_fixed_in_frame_mobjects(title_group) # Keeps title flat on screen

        # Title ki nayi Premium Animation
        self.play(FadeIn(title_text, shift=DOWN * 0.5), run_time=1)
        self.play(Create(underline), run_time=0.5)
        self.play(Flash(underline, color="#00FFFF", line_length=0.3, flash_radius=1.2), run_time=0.6)
        # ---------------------------------------------------------


        # 2. Display the Sequence L L G L L (Baki Sab Exactly Same Hai)
        chars = ["L", "L", "G", "L", "L"]
        letters = VGroup(*[Text(char, font="monospace", weight=BOLD).scale(2) for char in chars])
        letters.arrange(RIGHT, buff=1.0)
        letters.set_color(WHITE)
        
        for letter in letters:
            letter.set_shadow(0.5)

        self.play(FadeIn(letters, shift=UP), run_time=2)
        self.wait(1)

        # 3. Dynamic Number Tracker (Starts at 1)
        current_val = 1
        number_display = Integer(current_val).scale(3)
        number_display.set_color(YELLOW)
        number_display.next_to(letters, DOWN, buff=2)
        
        self.play(FadeIn(number_display, scale=0.5))
        
        cyan_color = "#00FFFF"
        scanner = SurroundingRectangle(letters[-1], color=cyan_color, buff=0.2, stroke_width=4)
        scanner.set_fill(cyan_color, opacity=0.1)

        self.play(Create(scanner))
        self.wait(0.5)

        # 4. The Ulta Logic Execution (Right to Left)
        for i in range(4, -1, -1):
            char = chars[i]
            target_letter = letters[i]

            self.move_camera(phi=65 * DEGREES, theta=(-45 + (4-i)*5) * DEGREES, run_time=1)
            self.play(scanner.animate.move_to(target_letter), run_time=0.8)
            self.play(target_letter.animate.set_color(cyan_color).scale(1.2), run_time=0.3)

            if char == "L":
                new_val = current_val * 2
                op_text = MathTex(r"\times 2").scale(1.5).set_color(GREEN)
            else: # char == "G"
                new_val = (current_val * 2) - 1
                op_text = MathTex(r"\times 2 - 1").scale(1.5).set_color(RED)

            op_text.next_to(target_letter, UP, buff=0.8)
            self.play(FadeIn(op_text, shift=UP*0.5), run_time=0.5)

            self.play(
                number_display.animate.set_value(new_val).set_color(WHITE),
                Flash(number_display, color=YELLOW, line_length=0.4, flash_radius=1.5),
                run_time=0.8
            )
            
            self.play(
                target_letter.animate.set_color(WHITE).scale(1/1.2),
                FadeOut(op_text, shift=UP*0.5),
                number_display.animate.set_color(YELLOW),
                run_time=0.4
            )

            current_val = new_val
            self.wait(0.5)

        # 5. Final Cinematic Pull-out
        self.move_camera(phi=45 * DEGREES, theta=-90 * DEGREES, zoom=0.8, run_time=2)
        
        gold_color = "#FFD700"
        box_final = SurroundingRectangle(number_display, color=gold_color, stroke_width=6)
        final_glow = box_final.copy().set_stroke(opacity=0.5, width=15)
        self.play(Create(box_final), FadeIn(final_glow))

        self.wait(3)
