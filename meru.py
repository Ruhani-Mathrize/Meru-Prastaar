"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
from manim import *

class PingalaSciFiBlueprint(Scene):
    def construct(self):
        # Background Black for "Screen" blend mode in VN
        self.camera.background_color = "#000000"
        
        # Neon Orange/Gold color
        neon_color = "#FFA500"
        
        triangle_data = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1]
        ]
        
        pyramid = VGroup()
        lines_group = VGroup()
        
        for i, row_data in enumerate(triangle_data):
            # Text size chota (0.35)
            row_mobjects = VGroup(*[Text(str(num), color=neon_color, font="Monospace").scale(0.35) for num in row_data])
            row_mobjects.arrange(RIGHT, buff=0.6)
            row_mobjects.center()
            row_mobjects.shift(UP * 2 + DOWN * i * 0.7)
            pyramid.add(row_mobjects)
            
            # Blueprint Connecting Lines (Upar wale elements se niche connect karna)
            if i > 0:
                for j in range(len(row_data) - 1):
                    # Line from Top to Bottom Left
                    l1 = DashedLine(pyramid[i-1][j].get_bottom(), pyramid[i][j].get_top(), color=neon_color, stroke_width=1, stroke_opacity=0.6)
                    # Line from Top to Bottom Right
                    l2 = DashedLine(pyramid[i-1][j].get_bottom(), pyramid[i][j+1].get_top(), color=neon_color, stroke_width=1, stroke_opacity=0.6)
                    lines_group.add(l1, l2)

        # Animation Setup
        # Pehle structure/lines banengi
        self.play(Create(lines_group), run_time=2.5)
        
        # Phir data/numbers pop honge
        for row in pyramid:
            self.play(Write(row), run_time=0.4)
            
        # Glowing effect
        self.play(pyramid.animate.set_opacity(0.6), run_time=0.5)
        self.play(pyramid.animate.set_opacity(1), run_time=0.5)
            

        self.wait(3)
