"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class MeruRealMagic(ThreeDScene):
    def construct(self):
        # --- 1. SETTINGS ---
        NEON_GOLD = "#FFD700"
        DEEP_ORANGE = "#FF4500"
        GLASS_OPACITY = 0.5
        
        # --- 2. TITLE (Fixed) ---
        title = Text("Meru Prastaar", color=NEON_GOLD, font_size=42)
        title.to_edge(UP, buff=0.5)
        self.add_fixed_in_frame_mobjects(title)

        # --- 3. CAMERA SETUP ---
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES, distance=20)
        self.begin_ambient_camera_rotation(rate=0.1) # Drone Effect

        # --- 4. GRID ---
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={
                "stroke_color": NEON_GOLD,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            },
            axis_config={"stroke_width": 0} 
        )
        self.add(grid) # Grid add kar diya

        # --- 5. BUILD CUBES (FLAT ON FLOOR) ---
        rows = 5
        cube_size = 1.0
        gap = 0.1
        
        pascal_data = []
        for n in range(rows):
            row_list = []
            for k in range(n + 1):
                val = 1
                if k > 0 and k < n:
                    val = pascal_data[n-1][k-1] + pascal_data[n-1][k]
                row_list.append(val)
            pascal_data.append(row_list)

        all_cubes = VGroup()
        
        for n in range(rows):
            for k in range(n + 1):
                val = pascal_data[n][k]
                # Position logic
                x_pos = (k - n / 2) * (cube_size + gap)
                y_pos = (rows - n) * (cube_size + gap) - 3
                
                cube = Cube(side_length=cube_size)
                cube.set_style(
                    fill_color=DEEP_ORANGE,
                    fill_opacity=GLASS_OPACITY,
                    stroke_color=NEON_GOLD,
                    stroke_width=5, 
                )
                
                text = Text(str(val), color=WHITE, font_size=40, weight=BOLD)
                text.rotate(90 * DEGREES, axis=RIGHT)
                
                group = VGroup(cube, text)
                group.move_to([x_pos, y_pos, 0]) 
                all_cubes.add(group)

        # --- 6. ANIMATION 1: APPEAR (FIXED) ---
        # DrawBorderThenFill use kar rahe hain taaki visible ho
        self.play(
            DrawBorderThenFill(all_cubes),
            run_time=3,
            rate_func=smooth
        )
        
        # --- 7. ANIMATION 2: STAND UP & ZOOM ---
        self.stop_ambient_camera_rotation()

        # Woh "Waoo" moment: Rotate + Zoom
        self.move_camera(
            phi=90*DEGREES,      # Eye Level
            theta=-90*DEGREES,   # Front View
            distance=15,         # Zoom In
            
            # Rotation ab yahan hai
            added_anims=[Rotate(all_cubes, angle=90*DEGREES, axis=RIGHT)],
            
            run_time=4,
            rate_func=smooth
        )


        self.wait(3)
