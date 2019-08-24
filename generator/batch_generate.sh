#!/usr/local/bin/zsh
export PYTHONPATH=/usr/local/Cellar/llvm/8.0.1/lib/python2.7/site-packages
python generate_SDL.py > ../sdl2/sdl2.py
python generate_SDL_audio.py > ../sdl2/sdl2_audio.py
python generate_SDL_blendmode.py > ../sdl2/sdl2_blendmode.py
python generate_SDL_clipboard.py > ../sdl2/sdl2_clipboard.py
python generate_SDL_cpuinfo.py > ../sdl2/sdl2_cpuinfo.py
python generate_SDL_error.py > ../sdl2/sdl2_error.py
python generate_SDL_events.py > ../sdl2/sdl2_events.py
python generate_SDL_filesystem.py > ../sdl2/sdl2_filesystem.py
python generate_SDL_gamecontroller.py > ../sdl2/sdl2_gamecontroller.py
python generate_SDL_gesture.py > ../sdl2/sdl2_gesture.py
python generate_SDL_haptic.py > ../sdl2/sdl2_haptic.py
python generate_SDL_hints.py > ../sdl2/sdl2_hints.py
python generate_SDL_joystick.py > ../sdl2/sdl2_joystick.py
python generate_SDL_keyboard.py > ../sdl2/sdl2_keyboard.py
python generate_SDL_keycode.py > ../sdl2/sdl2_keycode.py
python generate_SDL_log.py > ../sdl2/sdl2_log.py
python generate_SDL_messagebox.py > ../sdl2/sdl2_messagebox.py
python generate_SDL_mouse.py > ../sdl2/sdl2_mouse.py
python generate_SDL_pixels.py > ../sdl2/sdl2_pixels.py
python generate_SDL_platform.py > ../sdl2/sdl2_platform.py
python generate_SDL_power.py > ../sdl2/sdl2_power.py
python generate_SDL_rect.py > ../sdl2/sdl2_rect.py
python generate_SDL_render.py > ../sdl2/sdl2_render.py
python generate_SDL_rwops.py > ../sdl2/sdl2_rwops.py
python generate_SDL_scancode.py > ../sdl2/sdl2_scancode.py
python generate_SDL_shape.py > ../sdl2/sdl2_shape.py
python generate_SDL_surface.py > ../sdl2/sdl2_surface.py
python generate_SDL_timer.py > ../sdl2/sdl2_timer.py
python generate_SDL_touch.py > ../sdl2/sdl2_touch.py
python generate_SDL_version.py > ../sdl2/sdl2_version.py
python generate_SDL_video.py > ../sdl2/sdl2_video.py
python generate_SDL_vulkan.py > ../sdl2/sdl2_vulkan.py

python generate_SDL_ttf.py > ../sdl2/sdl2_ttf.py
python generate_SDL_image.py > ../sdl2/sdl2_image.py
python generate_SDL2_gfxPrimitives.py > ../sdl2/sdl2_gfxPrimitives.py
python generate_SDL2_rotozoom.py > ../sdl2/sdl2_rotozoom.py
python generate_SDL2_imageFilter.py > ../sdl2/sdl2_imageFilter.py
python generate_SDL2_framerate.py > ../sdl2/sdl2_framerate.py

