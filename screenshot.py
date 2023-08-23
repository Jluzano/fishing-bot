import mss
import mss.tools

with mss.mss() as sct:
    # Get information of monitor 2
    monitor_number = 1
    mon = sct.monitors[monitor_number]

    # The screen part to capture
    monitor = {
        "top": mon["top"] + 665,  # 100px from the top
        "left": mon["left"] + 1073,  # 100px from the left
        "width": 85,
        "height": 97,
        "mon": monitor_number,
    }
    output = "picture.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)