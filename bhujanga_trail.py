"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *
import numpy as np

class BhujangaTrailCinematic(ThreeDScene):
    def construct(self):
        # --- 🎬 SETUP ---
        self.camera.background_color = "#050200" # Pitch Black
        
        # --- 🎨 COLORS (MATCHING YOUR IMAGES) ---
        HEAD_COLOR = "#FFD700"   # Bright Gold Orb
        TRAIL_CORE = "#FFCC00"   # Inner bright yellow
        TRAIL_OUTER = "#FF4500"  # Outer deep orange
        TEXT_GOLD = "#FFD700"

        # --- FONT ---
        hindi_font = "Nirmala UI"
        try:
            test = Text("अ", font=hindi_font)
            font_to_use = hindi_font
        except:
            font_to_use = "sans-serif"

        # Syllables Data
        syllables = [
            "न", "ता", "तो", "न", "मा", "ता", 
            "न", "ब", "न्धु", "र्न", "दा", "ता"
        ]

        # ==========================================
        # 1. 3D CAMERA SETUP
        # ==========================================
        # Camera thoda side se aur upar se dekhega (Like the trail images)
        self.set_camera_orientation(phi=55 * DEGREES, theta=-20 * DEGREES)

        # Background Stars (Depth ke liye)
        stars = VGroup()
        for _ in range(50):
            s = Dot(radius=0.02, color=GRAY).move_to([
                np.random.uniform(-7, 7),
                np.random.uniform(-4, 4),
                -1 # Background mein peeche
            ])
            stars.add(s)
        self.add(stars)

        # ==========================================
        # 2. SNAKE HEAD & TRAIL SETUP
        # ==========================================
        
        # The Glowing Head
        head = Sphere(radius=0.2).set_color(HEAD_COLOR).set_gloss(1.0)
        head_glow = Dot(radius=0.6, color=HEAD_COLOR).set_opacity(0.3)
        snake_head = VGroup(head_glow, head)
        self.add(snake_head)

        # PATH LOGIC (Top Left to Right)
        # Sine wave formula
        def get_snake_path(t):
            x = t
            y = 1.2 * np.sin(1.8 * t) # Wave height and frequency
            z = 0
            return np.array([x, y, z])

        tracker = ValueTracker(-7) # Start far left

        # MOVEMENT UPDATER
        snake_head.add_updater(lambda m: m.move_to(get_snake_path(tracker.get_value())))

        # THE GLOWING TRAIL (TracedPath)
        # Outer thick orange trail
        trail_outer = TracedPath(
            head.get_center,
            stroke_width=16,
            stroke_color=TRAIL_OUTER,
            dissipating_time=None
        )
        # Inner thin yellow trail (for neon look)
        trail_inner = TracedPath(
            head.get_center,
            stroke_width=6,
            stroke_color=TRAIL_CORE,
            dissipating_time=None
        )
        
        self.add(trail_outer, trail_inner)

        # ==========================================
        # 3. ANIMATION: THE CRAWL
        # ==========================================
        
        # "Jab ye 12 akshar is rhythm mein chalte hain..."
        self.play(
            tracker.animate.set_value(5), # Move across screen
            run_time=5,
            rate_func=linear
        )
        
        # Stop tracking
        snake_head.clear_updaters()

        # ==========================================
        # 4. CAMERA MOVE (THE REVEAL)
        # ==========================================
        
        # "Toh wo seedhe nahi..."
        # Camera moves to perfect front view (Graph view)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES, run_time=2)

        # ==========================================
        # 5. SYLLABLES & TITLE APPEAR
        # ==========================================
        
        # "Isliye iska naam rakha gaya..."
        
        # 1. Main Title
        title = Text("Bhujanga-Prayatam", font="Georgia", font_size=55, color=TEXT_GOLD)
        title.next_to(trail_outer, DOWN, buff=1.0)
        
        self.play(Write(title), run_time=1.5)

        # 2. Syllables on the Wave (Visual proof of "12 Akshar")
        # Hum aksharon ko wave ki positions par rakhhenge
        syllable_group = VGroup()
        
        # Calculate positions explicitly based on the wave formula
        # Range -6 to 4.5 covers roughly the visible wave
        x_values = np.linspace(-6, 4.5, 12) 
        
        for i, char in enumerate(syllables):
            x = x_values[i]
            y = 1.2 * np.sin(1.8 * x)
            
            # Text creation
            t = Text(char, font=font_to_use, font_size=36, color=HEAD_COLOR)
            # Position slightly above the wave line
            t.move_to([x, y + 0.5, 0])
            syllable_group.add(t)

        # Animate them popping up
        self.play(
            LaggedStart(
                *[FadeIn(s, shift=DOWN*0.3) for s in syllable_group],
                lag_ratio=0.1
            ),
            run_time=2
        )

        # Final pulsing glow (Goosebumps moment)
        self.play(
            trail_outer.animate.set_stroke(width=20, opacity=0.8),
            trail_inner.animate.set_stroke(width=8),
            title.animate.scale(1.1).set_color("#FFF"), # Flash white briefly
            rate_func=there_and_back,
            run_time=2
        )
        

        self.wait(2)
