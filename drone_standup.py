"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class UltimateDroneTable(ThreeDScene):
    def construct(self):
        # --- 1. SETUP: PURE BLACK VOID ---
        self.camera.background_color = "#000000"
        
        # DRONE START: High altitude, looking from far away
        self.set_camera_orientation(phi=35 * DEGREES, theta=-135 * DEGREES, zoom=0.6)

        # --- 2. DATA SETUP ---
        rows_data = [
            ["1",  "G G G G G", "0 0 0 0 0", "0 0 0 0 0"],
            ["2",  "L G G G G", "1 0 0 0 0", "0 0 0 0 1"],
            ["3",  "G L G G G", "0 1 0 0 0", "0 0 0 1 0"],
            ["4",  "L L G G G", "1 1 0 0 0", "0 0 0 1 1"],
            ["5",  "G G L G G", "0 0 1 0 0", "0 0 1 0 0"],
            ["6",  "L G L G G", "1 0 1 0 0", "0 0 1 0 1"],
            ["7",  "G L L G G", "0 1 1 0 0", "0 0 1 1 0"],
            ["8",  "L L L G G", "1 1 1 0 0", "0 0 1 1 1"],
            ["9",  "G G G L G", "0 0 0 1 0", "0 1 0 0 0"],
            ["10", "L G G L G", "1 0 0 1 0", "0 1 0 0 1"],
            ["11", "G L G L G", "0 1 0 1 0", "0 1 0 1 0"]
        ]

        # Font sizes reduced by 3 points to stay inside the screen
        f_size = 11  
        h_size = 13  

        # Spacing pulled slightly inward to prevent cutting off
        x_cols = [-4.5, -1.5, 2.0, 5.5]
        y_start = 3.0
        y_step = 0.55

        # --- 3. CLEAN HEADERS ---
        h1 = Text("Row/Index", font_size=h_size, color=LIGHT_GREY, weight=BOLD).move_to(RIGHT * x_cols[0] + UP * y_start)
        h2 = Text("Sequences\nof G and L", font_size=h_size, color=ORANGE, weight=BOLD).move_to(RIGHT * x_cols[1] + UP * y_start)
        
        h3_top = Text("Binary Sequence by", font_size=f_size, color=WHITE)
        h3_bot = Text("Pingala", font_size=h_size, color=ORANGE, weight=BOLD)
        h3 = VGroup(h3_top, h3_bot).arrange(DOWN, buff=0.1).move_to(RIGHT * x_cols[2] + UP * y_start)
        
        h4 = Text("Binary\nNumbers", font_size=h_size, color="#00FFFF", weight=BOLD).move_to(RIGHT * x_cols[3] + UP * y_start)

        headers_group = VGroup(h1, h2, h3)
        
        # --- 4. CLEAN DATA ROWS ---
        base_elements = VGroup()
        reveal_elements = VGroup()

        for i, row in enumerate(rows_data):
            y = y_start - 0.8 - (i * y_step) 
            
            c1 = Text(row[0], font_size=f_size, color=GREY).move_to(RIGHT * x_cols[0] + UP * y)
            c2 = Text(row[1], font="Consolas", font_size=f_size, color="#FF6600", weight=BOLD).move_to(RIGHT * x_cols[1] + UP * y)
            c3 = Text(row[2], font="Consolas", font_size=f_size, color=WHITE, weight=BOLD).move_to(RIGHT * x_cols[2] + UP * y)
            base_elements.add(c1, c2, c3)

            c4 = Text(row[3], font="Consolas", font_size=f_size, color="#00FFFF", weight=BOLD).move_to(RIGHT * x_cols[3] + UP * y)
            reveal_elements.add(c4)

        # Center all data perfectly
        all_data = VGroup(headers_group, h4, base_elements, reveal_elements).center()

        # --- 5. FULL CINEMATIC ANIMATION SEQUENCE ---
        
        # Step 1: Base data fades in while looking from far away
        self.play(FadeIn(headers_group), FadeIn(base_elements), run_time=2)
        self.wait(0.5)

        # Step 2: DRONE SWOOP IN 
        # Camera dynamically flies closer to the data
        self.move_camera(
            phi=65 * DEGREES,    
            theta=-85 * DEGREES, 
            zoom=1.2, # Safe zoom limit so text stays in frame
            run_time=3.5,
            rate_func=smooth
        )
        self.wait(0.5)

        # Step 3: THE NEON REVEAL ("Mirror Image" Moment)
        self.play(FadeIn(h4, shift=DOWN*0.2), run_time=0.5)
        self.play(
            LaggedStart(
                *[FadeIn(item, shift=LEFT * 0.3) for item in reveal_elements],
                lag_ratio=0.1
            ),
            run_time=2.5
        )
        self.wait(1)

        # Step 4: THE "STAND UP" REVEAL 
        # Camera swings to perfectly face the table straight on
        self.move_camera(
            phi=0 * DEGREES,    
            theta=-90 * DEGREES,
            zoom=0.95, # Perfect framing for the straight 2D look
            run_time=3.5,
            rate_func=smooth
        )

        self.wait(3)
