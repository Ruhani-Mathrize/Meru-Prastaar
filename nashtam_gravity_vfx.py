from manim import *

class NashtamGravityVFX(ThreeDScene):
    def construct(self):
        self.camera.background_color = "#000000"
        
        # Colors
        COLOR_EVEN = "#00F0FF" 
        COLOR_ODD = "#FF2D55"  
        COLOR_GOLD = "#FFD700" 

        # 1. CAMERA SETUP: Stable Drone View
        self.set_camera_orientation(phi=35 * DEGREES, theta=-20 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.06) # Very slow for stability

        # 2. MAIN NUMBER (Centered Right)
        num_val = 22
        main_num = Text(str(num_val), font="Courier", weight=BOLD, font_size=90)
        main_num.move_to(RIGHT * 3 + UP * 1)
        self.add_fixed_in_frame_mobjects(main_num)
        
        self.play(Write(main_num), run_time=1)

        # 3. MATH DATA
        steps = [
            (22, "EVEN", r"\frac{22}{2}", "L", 11),
            (11, "ODD", r"\frac{11+1}{2}", "G", 6),
            (6, "EVEN", r"\frac{6}{2}", "L", 3),
            (3, "ODD", r"\frac{3+1}{2}", "G", 2),
            (2, "EVEN", r"\frac{2}{2}", "L", 1),
        ]

        result_chars = VGroup()

        # 4. CINEMATIC LOOP
        for i, (curr, parity, formula_latex, char, next_val) in enumerate(steps):
            p_color = COLOR_EVEN if parity == "EVEN" else COLOR_ODD
            
            # --- STEP 1: HISTORY (Left Side - Ultra Compact) ---
            # Font size reduced by another 30% (from 38 to 25)
            step_label = Text(parity, font="Courier", weight=BOLD, font_size=22, color=p_color)
            step_math = MathTex(formula_latex, font_size=28, color=WHITE) 
            step_ui = VGroup(step_label, step_math).arrange(RIGHT, buff=0.2)
            
            # Fixed position on the left, moving down step-by-step
            step_ui.move_to([-5.2, 2.8 - (i * 0.9), 0]) # Reduced vertical gap to 0.9
            self.add_fixed_in_frame_mobjects(step_ui)

            self.play(
                FadeIn(step_ui, shift=RIGHT * 0.2),
                main_num.animate.set_color(p_color).scale(1.05),
                run_time=0.6
            )

            # --- STEP 2: LGLG MOVEMENT (Dropping Downwards) ---
            res_char = Text(char, font="Courier", weight=BOLD, font_size=80, color=COLOR_GOLD)
            
            # Start: Near the calculation
            start_pos = step_ui.get_center()
            # Target: Bottom row, sliding into position (Third/Fourth Quadrant)
            target_pos = DOWN * 2.8 + LEFT * (2.8 - i*1.4)
            
            res_char.move_to(start_pos)
            
            self.play(
                res_char.animate.move_to(target_pos).set_opacity(1),
                Flash(target_pos, color=COLOR_GOLD, flash_radius=0.5, line_length=0.2),
                run_time=0.9,
                rate_func=exponential_decay # Gravity-like feel
            )
            result_chars.add(res_char)

            # --- STEP 3: MORPH NUMBER ---
            if i < len(steps) - 1:
                new_num_mob = Text(str(next_val), font="Courier", weight=BOLD, font_size=90)
                new_num_mob.move_to(main_num.get_center())
                self.remove_fixed_in_frame_mobjects(main_num)
                self.add_fixed_in_frame_mobjects(new_num_mob)
                
                self.play(ReplacementTransform(main_num, new_num_mob), run_time=0.4)
                main_num = new_num_mob

        # 5. FINAL REVEAL (Straightening & Centering)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90*DEGREES, run_time=1.5)
        
        self.play(
            result_chars.animate.arrange(RIGHT, buff=0.5).move_to(ORIGIN).scale(1.4),
            FadeOut(main_num),
            run_time=1.5
        )
        
        # Final Glow
        self.play(Indicate(result_chars, color=COLOR_GOLD, scale_factor=1.2))
        self.wait(3)