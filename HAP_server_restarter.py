from os import system, kill, getpid
from signal import CTRL_C_EVENT
from time import sleep
from subprocess import run, Popen

path_to_tv_accessory = "accessories\\TV_accessory.js"
line_to_alter = 88
line_1 = "	var inputHDMI1 = tv.addService(Service.InputSource, \"hdmi\" + i, \"HDMI\" + i ); \n"
line_2 = "	var inputHDMI1 = tv.addService(Service.InputSource, \"hdmi\" + i, \"HDMI\" + \" \\n\\n\\n\" + i ); \n"


def update_accessory():
    # lines = []

    with open(path_to_tv_accessory, "r") as file:
        lines = file.readlines()

    with open(path_to_tv_accessory, "w") as file:

        if lines[line_to_alter] == line_1:
            lines[line_to_alter] == line_2
        else:
            lines[line_to_alter] == line_1

        file.writelines(lines)


if __name__ == "__main__":

    for _ in range(100):

        process = Popen("node Core.js")
        pid = process.pid

        update_accessory()
        kill(pid, CTRL_C_EVENT)
        sleep(1)
