from manim import *
import random

class PingalaSolidCenter(ThreeDScene):
    def construct(self):
        # --- 🎬 SETUP ---
        self.camera.background_color = "#050200" # Deep Black
        
        # --- 🎨 COLORS ---
        G_COLOR = "#FFD700"   # Golden Yellow
        L_COLOR = "#FF4500"   # Deep Orange
        HUD_COLOR = "#00FFFF" # Cyan (Sci-Fi Text)
        
        # --- 1. AMBIENT PARTICLES ---
        stars = VGroup()
        for _ in range(60):
            s = Dot(radius=random.uniform(0.02, 0.05), color=GRAY)
            s.move_to([
                random.uniform(-7, 7),
                random.uniform(-5, 5),
                random.uniform(-5, -2) 
            ])
            s.set_opacity(random.uniform(0.2, 0.6))
            stars.add(s)
        self.add(stars)

        # --- HELPER: SOLID BLOCK ---
        def create_block(text, width=1.6, height=0.9):
            # 1. Background (Glassy Solid)
            bg = Rectangle(width=width, height=height)
            bg.set_fill(BLACK, opacity=0.7) # Dark glass look
            bg.set_stroke(WHITE, width=0, opacity=0)
            
            # 2. Color Logic
            color = G_COLOR if text == "G" else L_COLOR
            if text == "": color = GRAY
            
            # 3. Glowing Text
            txt = Text(text, font="Georgia", font_size=36, color=color)
            if text != "":
                txt.set_glow_factor(0.6)
            
            # 4. Neon Border (Thicker for "Solid" look)
            border = RoundedRectangle(corner_radius=0.1, width=width, height=height)
            border.set_stroke(color, width=3, opacity=0.9)
            
            # Group them
            block = VGroup(bg, border, txt)
            return block

        # --- CAMERA SETUP ---
        # Start with a slight tilt so it looks 3D but is easy to read
        self.set_camera_orientation(phi=50 * DEGREES, theta=-10 * DEGREES)

        # ==========================================
        # STEP 1: n = 1 (Center Stage)
        # ==========================================
        
        # --- HUD (Fixed on Screen) ---
        # Using MathTex for perfect formatting
        hud_n = MathTex("n = 1", color=HUD_COLOR).scale(1.5)
        hud_eq = MathTex("2^1 = 2", color=HUD_COLOR).scale(1.5)
        
        # Position HUD at corners
        hud_n.to_corner(UL, buff=1.0)
        hud_eq.to_corner(UR, buff=1.0)
        
        self.add_fixed_in_frame_mobjects(hud_n, hud_eq)

        # --- TABLE CREATION ---
        b1_g = create_block("G")
        b1_l = create_block("L")
        col1 = VGroup(b1_g, b1_l).arrange(DOWN, buff=0.1)
        
        # CENTER IT
        col1.move_to(ORIGIN)
        
        self.play(FadeIn(col1, shift=IN), Write(hud_n), Write(hud_eq), run_time=1.5)
        self.wait(0.5)

        # ==========================================
        # STEP 2: n = 2 (Copy Paste)
        # ==========================================
        
        # --- UPDATE HUD ---
        self.play(
            Transform(hud_n, MathTex("n = 2", color=HUD_COLOR).scale(1.5).to_corner(UL, buff=1.0)),
            Transform(hud_eq, MathTex("2^2 = 4", color=HUD_COLOR).scale(1.5).to_corner(UR, buff=1.0)),
        )

        # 1. Shift Original Left to make space (Keeping Center balanced)
        self.play(col1.animate.shift(LEFT * 1.0 + UP * 0.5))

        # 2. COPY PASTE ANIMATION
        col1_copy = col1.copy()
        
        self.play(
            col1_copy.animate.next_to(col1, DOWN, buff=0.1),
            run_time=1.0,
            rate_func=rate_functions.ease_out_back
        )

        # 3. FILL NEW COLUMN
        # Create empty blocks
        col2 = VGroup(*[create_block("") for _ in range(4)]).arrange(DOWN, buff=0.1)
        col2.next_to(col1, RIGHT, buff=0.1)
        col2.align_to(col1, UP)
        
        # Fill content
        g_fill = VGroup(create_block("G"), create_block("G")).arrange(DOWN, buff=0.1).move_to(col2[0:2])
        l_fill = VGroup(create_block("L"), create_block("L")).arrange(DOWN, buff=0.1).move_to(col2[2:4])
        
        self.play(FadeIn(g_fill, shift=UP), FadeIn(l_fill, shift=DOWN))
        
        # Re-Center the whole group
        table_2 = VGroup(col1, col1_copy, g_fill, l_fill)
        self.play(table_2.animate.move_to(ORIGIN)) # SNAP TO CENTER
        self.wait(0.5)

        # ==========================================
        # STEP 3: n = 3 (Expansion)
        # ==========================================
        
        # --- UPDATE HUD ---
        self.play(
            Transform(hud_n, MathTex("n = 3", color=HUD_COLOR).scale(1.5).to_corner(UL, buff=1.0)),
            Transform(hud_eq, MathTex("2^3 = 8", color=HUD_COLOR).scale(1.5).to_corner(UR, buff=1.0)),
        )

        # 1. Zoom Out slightly & Move to make space
        self.move_camera(zoom=0.8, run_time=1.0)
        
        # 2. Shift Table Left/Up
        self.play(table_2.animate.shift(LEFT * 1.5 + UP * 1.0))

        # 3. BIG COPY PASTE
        table_3_copy = table_2.copy()
        
        self.play(
            table_3_copy.animate.next_to(table_2, DOWN, buff=0.1),
            run_time=1.2,
            rate_func=rate_functions.ease_out_back
        )

        # 4. FILL FINAL COLUMN
        col3_Gs = VGroup(*[create_block("G") for _ in range(4)]).arrange(DOWN, buff=0.1)
        col3_Ls = VGroup(*[create_block("L") for _ in range(4)]).arrange(DOWN, buff=0.1)
        
        col3 = VGroup(col3_Gs, col3_Ls).arrange(DOWN, buff=0.1)
        col3.next_to(table_2, RIGHT, buff=0.1)
        col3.align_to(table_2, UP)
        
        self.play(
            LaggedStart(
                *[GrowFromCenter(m) for m in col3_Gs],
                *[GrowFromCenter(m) for m in col3_Ls],
                lag_ratio=0.05
            ),
            run_time=1.5
        )
        
        # Re-Center Final Table
        full_grid = VGroup(table_2, table_3_copy, col3)
        self.play(full_grid.animate.move_to(ORIGIN)) # PERFECT CENTER

        # ==========================================
        # GRAND FINALE: 360 CAMERA ROTATION
        # ==========================================
        
        # Glow Effect
        self.play(full_grid.animate.set_stroke(opacity=1).scale(1.1), run_time=1)

        # Remove HUD for the cinematic spin (Optional, keeps view clean)
        self.play(FadeOut(hud_n), FadeOut(hud_eq))

        # The 360 Spin
        # We rotate Theta from -10 to -10 + 360
        self.move_camera(
            phi=60 * DEGREES, # Maintain tilt
            theta=(-10 + 360) * DEGREES, # Full circle
            run_time=6, # Slow and cinematic
            rate_func=smooth
        )
        
        self.wait(1)