from manim import *

class PingalaCinematicLogic(ThreeDScene):
    def construct(self):
        # Background and Colors
        self.camera.background_color = "#000000"
        COLOR_EVEN = "#00F0FF" # Electric Cyan
        COLOR_ODD = "#FF2D55"  # Neon Red
        COLOR_GOLD = "#FFD700" 

        # 1. INITIAL 3D VIEW (Subtle Tilt for Depth)
        self.set_camera_orientation(phi=45 * DEGREES, theta=-20 * DEGREES)
        
        # 2. THE STARTING NUMBER (Floating in Space)
        num_val = 22
        main_num = Text(str(num_val), font="Courier", weight=BOLD, font_size=120)
        main_num.set_gloss(0.5) # 3D Glossy effect
        
        self.add_fixed_in_frame_mobjects(main_num) # Number fixed in screen center
        self.play(Write(main_num), run_time=1.5)
        self.wait(0.5)

        # 3. THE STEPS DATA
        steps = [
            ("22", "EVEN", "22 / 2", "L", 11),
            ("11", "ODD", "(11+1) / 2", "G", 6),
            ("6", "EVEN", "6 / 2", "L", 3),
            ("3", "ODD", "(3+1) / 2", "G", 2),
            ("2", "EVEN", "2 / 2", "L", 1),
        ]

        result_chars = VGroup()

        # 4. CINEMATIC LOOP
        for i, (val, parity, math, char, next_val) in enumerate(steps):
            # A. Camera Drone Movement (Dheere se ghumega har step par)
            self.move_camera(theta=-(20 + i*15) * DEGREES, run_time=1.2, rate_func=smooth)

            # B. Parity Label (EVEN/ODD Pop-up with Glow)
            p_color = COLOR_EVEN if parity == "EVEN" else COLOR_ODD
            label = Text(f"{parity}", font="Courier", weight=BOLD, font_size=40, color=p_color)
            label.shift(UP * 2.5 + RIGHT * 2)
            
            # C. Math Formula (Floating next to it)
            math_text = Text(math, font="Courier", font_size=30, color=WHITE).next_to(label, DOWN)
            
            # Label aur Math ko 3D space mein fixed rakhna
            self.add_fixed_in_frame_mobjects(label, math_text)
            self.play(
                FadeIn(label, shift=LEFT),
                Write(math_text),
                main_num.animate.set_color(p_color).scale(1.1),
                run_time=0.8
            )

            # D. The Result Character (Laghu/Guru)
            res_char = Text(char, font="Courier", weight=BOLD, font_size=90, color=COLOR_GOLD)
            res_char.move_to(DOWN * 2 + LEFT * (2 - i*1.2)) # Niche line mein set hona
            
            self.play(
                TransformFromCopy(main_num, res_char),
                Flash(res_char, color=COLOR_GOLD, flash_radius=1),
                run_time=1
            )
            result_chars.add(res_char)

            # E. Number Transformation
            if i < len(steps) - 1:
                new_num = Text(str(next_val), font="Courier", weight=BOLD, font_size=120)
                self.remove_fixed_in_frame_mobjects(main_num)
                self.add_fixed_in_frame_mobjects(new_num)
                
                self.play(
                    ReplacementTransform(main_num, new_num),
                    FadeOut(label),
                    FadeOut(math_text),
                    run_time=0.8
                )
                main_num = new_num
            else:
                self.play(FadeOut(label), FadeOut(math_text), FadeOut(main_num), run_time=1)

        # 5. FINAL REVEAL (The Result takes over the screen)
        # Camera wapas samne aayega
        self.move_camera(phi=0*DEGREES, theta=-90*DEGREES, run_time=1.5)
        
        final_group = result_chars.copy()
        self.play(
            final_group.animate.arrange(RIGHT, buff=0.6).move_to(ORIGIN).scale(1.5),
            run_time=2
        )

        # Final Glow and Shine
        self.play(
            Indicate(final_group, color=COLOR_GOLD, scale_factor=1.2),
            final_group.animate.set_color(WHITE), # Shine effect
            run_time=1.5
        )
        self.play(final_group.animate.set_color(COLOR_GOLD))
        self.wait(2)