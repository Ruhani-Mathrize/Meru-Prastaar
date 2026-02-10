"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class MeruPrastaar3D(ThreeDScene):
    def construct(self):
        # --- 1. Colors & Settings ---
        # Tumhara Golden aur Orange theme
        MY_GOLD = "#FFD700"   # Gold
        MY_ORANGE = "#FF8C00" # Orange Glow
        
        # --- 2. Camera Setup (Cinematic 360 View) ---
        # Camera ko thoda upar aur side mein set kiya
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        
        # Camera dhire-dhire ghumna shuru karega (360 degree feel)
        self.begin_ambient_camera_rotation(rate=0.15)

        # --- 3. The Table (Base Grid) ---
        # Ek glowing grid jo table jaisi dikhegi
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": MY_GOLD,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        # Grid ko flat letaya (Horizontal Plane)
        # Note: Manim mein Z-axis upar hoti hai, isliye grid XY plane par hai
        self.add(grid)

        # --- 4. Pascal's Triangle Logic (Meru Prastaar) ---
        rows = 5  # Kitni lines ka pyramid chahiye
        cube_size = 0.8
        gap = 0.2 # Cubes ke beech ka gap

        # Logic to calculate numbers
        pascal_data = []
        for n in range(rows):
            row_list = []
            for k in range(n + 1):
                # nCk formula calculate karne ki jagah simple math
                val = 1
                if k > 0 and k < n:
                    val = pascal_data[n-1][k-1] + pascal_data[n-1][k]
                row_list.append(val)
            pascal_data.append(row_list)

        # --- 5. Creating 3D Objects ---
        all_blocks = VGroup() # Saare blocks ka group

        for n in range(rows):
            for k in range(n + 1):
                val = pascal_data[n][k]
                
                # Positioning logic (Center alignment)
                x_pos = (k - n / 2) * (cube_size + gap)
                y_pos = (rows - n) * (cube_size + gap) - 3 # Thoda peeche shift kiya
                z_pos = 0 # Starting on the grid
                
                # The 3D Cube (Transparent & Glowing)
                cube = Cube(side_length=cube_size)
                cube.set_style(
                    fill_color=MY_ORANGE,
                    fill_opacity=0.2, # Glass effect (Transparent)
                    stroke_color=MY_GOLD,
                    stroke_width=2
                )
                
                # The Number Text
                text = Text(str(val), color=MY_GOLD, font_size=36)
                # Text ko khada karna hai (Rotate 90 degrees)
                text.rotate(90 * DEGREES, axis=RIGHT)
                
                # Cube aur Text ko ek saath group kiya
                block_group = VGroup(cube, text)
                block_group.move_to([x_pos, y_pos, z_pos])
                
                all_blocks.add(block_group)

        # --- 6. The Animation (Emerging from Center) ---
        
        # Pehle sabko chupa do (Scale = 0) aur center me le aao
        start_state = all_blocks.copy()
        start_state.scale(0)
        start_state.move_to([0, 0, 0]) # Center of table

        # "LaggedStart" use karenge taaki ek-ek karke nikle
        # Rate function 'smooth' use kiya hai jo error nahi dega
        self.play(
            Transform(start_state, all_blocks),
            run_time=4,
            lag_ratio=0.1,
            rate_func=smooth # Error-free smooth motion
        )
        
        # --- 7. Final Hold ---
        # Scene ko thodi der chalne do taaki camera ghumta rahe

        self.wait(5)
