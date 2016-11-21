from psychopy import core, visual, event


if __name__ == "__main__":

    debug = False

    if debug:
        size = [1440, 900]
    else:
        size = [1024, 768]

    gamma = None

    win = visual.Window(size=size,
                        units="norm",
                        fullscr=True,
                        gamma=gamma,
                        allowGUI=False)

    light = visual.GratingStim(win,
                               tex=None,
                               mask="circle",
                               units="pix",
                               size=700,
                               colorSpace="rgb255")

    text = visual.TextStim(win,
                           pos=(.7, .7),
                           height=.08)
                            

    current_index = 0
    digit_vals = [0, 10, 20, 40, 60, 80, 100, 120,
                  140, 160, 180, 200, 220, 240, 255]
    keys = ["left", "right", "escape"]

    while True:

        digit = digit_vals[current_index]

        light.color = digit
        text.text = digit

        light.draw()
        text.draw()
        win.flip()

        action, = event.waitKeys(keyList=keys)

        if action == "left":
            current_index -= 1
        elif action == "right":
            current_index += 1
        elif action == "escape":
            core.quit()

        current_index = max(current_index, 0)
        current_index = min(current_index, len(digit_vals) - 1)
