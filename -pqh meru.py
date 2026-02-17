"""
Project:  Binary Decode / code Visualization
Copyright (c) 2026 Ruhani Kashni (MathRize)
License: MIT License (See LICENSE file for details)
YouTube: https://www.youtube.com/@MathRize
"""
# --- FIX FOR ENCRYPT / DECRYPT TEXT ---

# 1. Apne text ko ek group mein banayein aur uski original size choti karein (0.5)
final_text = VGroup(
    Text("Encrypt", color=RED),
    Text("डेटा का मार्ग"), # Aapka Hindi text
    Text("Decrypt", color=BLUE)
).arrange(DOWN, buff=0.5).scale(0.5)

# 2. SABSE IMPORTANT: Isko 3D camera se azaad karke screen par "Fix" karein taaki tedha na ho
self.add_fixed_in_frame_mobjects(final_text)

# 3. Ghum kar center mein aane ka effect (Spin & Zoom-in Setup)
final_text.scale(0.01) # Start mein ekdum chota
final_text.rotate(2 * PI) # 360 degree ghuma hua rakhein

# 4. Final Cinematic Animation
self.play(
    final_text.animate.scale(100).rotate(-2 * PI).move_to(ORIGIN), 
    run_time=2.5,
    rate_func=ease_in_out_sine # Smooth Sci-Fi feel ke liye
)

# ----------------------------------------
