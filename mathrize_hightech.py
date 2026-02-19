from manim import *
import random

class ArchitectVsEngineerHighTech(ThreeDScene):
    def construct(self):
        # 1. PREMIUM BLACK BACKGROUND & SPACE THEME
        self.camera.background_color = BLACK
        stars = VGroup(*[
            Dot(radius=random.uniform(0.01, 0.03), color=WHITE, fill_opacity=random.uniform(0.1, 0.4)).move_to(
                [random.uniform(-8, 8), random.uniform(-5, 5), random.uniform(-2, 2)]
            ) for _ in range(100)
        ])
        self.add(stars)

        # High-Tech Colors
        color_G = "#FFD700" # Premium Gold
        color_L = "#FF4500" # Premium Red/Orange
        color_tech = "#00FFFF" # Cyan (For Sci-Fi Energy Effects)

        # ---------------------------------------------------------
        # HELPER FUNCTION (Error-Free Premium Boxes)
        # ---------------------------------------------------------
        def get_premium_box(char, color_hex, w=1.0, h=0.6):
            box = RoundedRectangle(corner_radius=0.1)
            box.stretch_to_fit_width(w).stretch_to_fit_height(h)
            box.set_stroke(color_hex, width=2)
            box.set_fill(BLACK, opacity=0.8)
            
            txt = Text(char, font="Times New Roman", weight=BOLD, color=color_hex).scale(0.8)
            return VGroup(box, txt)

        # ---------------------------------------------------------
        # PART 1: PINGALA'S BLUEPRINT (DRONE SHOT START)
        # ---------------------------------------------------------
        # Start with an epic 3D angled Drone Shot
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES, zoom=0.8)
        
        # Start ambient drone circling
        self.begin_ambient_camera_rotation(rate=0.15)

        patterns = [
            ["G", "G", "G"],
            ["L", "G", "G"],
            ["G", "L", "G"],
            ["L", "L", "G"],
            ["G", "G", "L"]
        ]
        
        pingala_blueprint = VGroup()
        for row in patterns:
            row_group = VGroup(*[get_premium_box(c, color_G if c=="G" else color_L) for c in row])
            row_group.arrange(RIGHT, buff=0.1)
            pingala_blueprint.add(row_group)
        pingala_blueprint.arrange(DOWN, buff=0.1).move_to(OUT * 0.2)

        # Draw the blueprint with a high-tech building effect
        self.play(DrawBorderThenFill(pingala_blueprint), run_time=2, lag_ratio=0.1)
        
        # Holographic Scanner Effect
        scan_line = Line(pingala_blueprint.get_corner(UL) + LEFT*0.5, pingala_blueprint.get_corner(UR) + RIGHT*0.5, color=color_tech)
        scan_line.set_stroke(width=6).set_glow_factor(1)
        
        self.play(scan_line.animate.move_to(pingala_blueprint.get_bottom()), run_time=1.5, rate_func=there_and_back)
        self.remove(scan_line)

        # Stop circling to prepare for the epic morph
        self.stop_ambient_camera_rotation()
        self.wait(0.5)

        # ---------------------------------------------------------
        # PART 2: THE KEDAR BHATT TABLE PREP
        # ---------------------------------------------------------
        kedar_table = VGroup()
        
        # Top Row (Powers of 2)
        powers = ["1", "2", "4", "8", "16", "32", "64", "128"]
        top_row = VGroup(*[get_premium_box(p, WHITE, w=1.0, h=0.6) for p in powers])
        top_row.arrange(RIGHT, buff=0)

        # Bottom Row (L and G Sequence)
        sequence = ["L", "L", "G", "L", "L", "G", "G", "G"]
        bot_row = VGroup(*[get_premium_box(c, color_G if c=="G" else color_L, w=1.0, h=0.6) for c in sequence])
        bot_row.arrange(RIGHT, buff=0)

        kedar_table.add(top_row, bot_row).arrange(DOWN, buff=0)

        # ---------------------------------------------------------
        # PART 3: THE EPIC MORPH & DRONE SWOOP
        # ---------------------------------------------------------
        # Camera swoops perfectly to front-facing (theta = -90) WHILE the table morphs
        self.move_camera(
            phi=0 * DEGREES, 
            theta=-90 * DEGREES, # THIS is the fix that makes it stand perfectly in front
            zoom=0.85, 
            added_anims=[ReplacementTransform(pingala_blueprint, kedar_table)],
            run_time=2.5
        )

        # ---------------------------------------------------------
        # PART 4: HIGH-TECH BOOT UP EFFECT
        # ---------------------------------------------------------
        # A fast "data-loading" pulse runs through the Powers of 2 row
        for box in top_row:
            self.play(
                box[0].animate.set_stroke(color_tech, width=5).set_fill(color_tech, opacity=0.2),
                box[1].animate.set_color(color_tech),
                run_time=0.06
            )
            self.play(
                box[0].animate.set_stroke(WHITE, width=2).set_fill(BLACK, opacity=0.8),
                box[1].animate.set_color(WHITE),
                run_time=0.06
            )

        # Final Cinematic Frame Lock
        frame_box = SurroundingRectangle(kedar_table, color=color_G, buff=0.1, stroke_width=4)
        self.play(Create(frame_box), Flash(frame_box, color=color_tech, line_length=1.5, num_lines=40), run_time=1)
        
        self.play(frame_box.animate.set_glow_factor(0.5), run_time=2)
        self.wait(2)