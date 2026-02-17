from manim import *
import numpy as np
import random

class AIScanMeru(ThreeDScene):
    def construct(self):
        # --- 1. PURE BLACK SCI-FI VOID ---
        self.camera.background_color = "#000000"
        
        # DRONE START: Looking at the ground from a sharp angle
        self.set_camera_orientation(phi=75 * DEGREES, theta=-90 * DEGREES, zoom=0.6)

        # --- 2. GENERATE MERU PRASTARA DATA ---
        num_rows = 11
        meru_data = []
        for n in range(num_rows):
            row = [1]
            if meru_data:
                last_row = meru_data[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            meru_data.append(row)

        # --- 3. BUILD HOLOGRAPHIC NUMBERS & SCAN BOXES ---
        mountain_rows = VGroup()
        scan_boxes = VGroup()
        
        x_step, y_step = 1.3, 1.0

        for i, row in enumerate(meru_data):
            row_group = VGroup()
            for j, val in enumerate(row):
                x_pos = (j - len(row) / 2.0 + 0.5) * x_step
                y_pos = 4.0 - i * y_step
                
                # Sharp Sci-Fi Text
                txt_color = WHITE if val == 1 else "#00FFFF" # Neon Cyan
                num = Text(str(val), font="Consolas", font_size=32, color=txt_color, weight=BOLD)
                num.move_to(np.array([x_pos, y_pos, 0]))
                row_group.add(num)
            
            mountain_rows.add(row_group)
            
            # --- CREATING THE TRANSPARENT SCAN BOX FOR EACH ROW ---
            # Box surrounds the whole row, initially fully transparent (hidden)
            box = SurroundingRectangle(row_group, buff=0.25)
            box.set_stroke(width=3)
            box.set_fill(opacity=0.3) # The transparent glass look
            box.set_opacity(0)        # Hidden at start
            scan_boxes.add(box)

        # Combine everything to move as one giant 3D structure
        full_mountain = VGroup(mountain_rows, scan_boxes)

        # --- 4. PREPARE THE "LYING DOWN" ERUPTION STATE ---
        full_mountain.rotate(85 * DEGREES, RIGHT)
        full_mountain.move_to(DOWN * 1.5 + IN * 2)

        # Hide elements deep underground for the dramatic entrance
        for row in mountain_rows:
            for num in row:
                num.save_state()
                num.shift(DOWN * 6 + IN * 6).scale(0.01).set_opacity(0)

        # --- 5. CINEMATIC ANIMATION: THE ERUPTION ---
        self.wait(0.5)

        # Bottom-to-Top Eruption
        reversed_rows = list(reversed(mountain_rows))
        eruption_anims = []
        for row in reversed_rows:
            eruption_anims.append(
                LaggedStart(*[Restore(num, run_time=1.2) for num in row], lag_ratio=0.03)
            )

        # Drone Camera flies around while the data erupts from the ground
        self.move_camera(
            phi=60 * DEGREES, 
            theta=-110 * DEGREES, 
            zoom=0.8,
            added_anims=[
                LaggedStart(*eruption_anims, lag_ratio=0.1)
            ],
            run_time=4.0,
            rate_func=smooth
        )
        self.wait(0.5)

        # --- 6. THE HERO STAND-UP ---
        # "ab aapko kaise pata chalega..."
        self.move_camera(
            phi=0 * DEGREES, 
            theta=-90 * DEGREES, 
            zoom=0.85,
            added_anims=[
                full_mountain.animate.rotate(-85 * DEGREES, RIGHT).move_to(ORIGIN)
            ],
            run_time=3.5,
            rate_func=smooth
        )
        self.wait(0.5)

        # --- 7. THE HIGH-TECH AI SCAN (RANDOM TRANSPARENT BOXES) ---
        # "ki hazaron lines mein se yeh kaunsi row ka hai?"
        scan_colors = ["#FF00FF", "#FFFF00", "#00FF00", "#0088FF"] # Pink, Yellow, Neon Green, Blue
        
        # Fast rapid-fire random scans to simulate AI searching
        num_scans = 18 # How many rapid scans
        for _ in range(num_scans):
            # Pick a random row (excluding the very top '1' for better visual effect)
            rand_idx = random.randint(1, num_rows - 1)
            rand_color = random.choice(scan_colors)
            target_box = scan_boxes[rand_idx]
            
            # Flash the box ON
            self.play(
                target_box.animate.set_color(rand_color).set_stroke(rand_color, 4).set_fill(rand_color, 0.4).set_opacity(1),
                run_time=0.08, # Extremely fast!
                rate_func=linear
            )
            # Flash the box OFF
            self.play(
                target_box.animate.set_opacity(0),
                run_time=0.08,
                rate_func=linear
            )

        # --- 8. FINAL HOLD ---
        self.wait(2)