import os

from termcolor import colored

base_args = [
    "",
    "1",
    "1 2",
    "1 2 3",
    "4 500 abc 200",
    "4 500 200 2.9",
    "4 -500 200 200",
    "4 2147483648 200 200",
    "0 800 200 200",
    "500 100 200 200",
    "4 2147483647 200 200",
    "4 200 2147483647 200",
    "4 800 200 2147483647",
    "2 800 200 200",
]

base_args2 = [
    "5 800 200 200",
    "5 0 200 200",
    "5 800 0 200",
    "5 800 200 0",
    "5 800 0 0",
    "5 800 200 200 0",
    "4 410 200 200",
    "1 200 200 200",
    "4 2147483647 0 0",
    "4 200 210 200",
    "2 600 200 800",
    "4 310 200 200",
    "3 400 100 100 3",
]

args = [
    "",
    "1",
    "1 2",
    "1 2 3",
    "4 500 abc 200",
    "4 500 200 2.9",
    "4 -500 200 200",
    "4 2147483648 200 200",
    "0 800 200 200",
    "500 100 200 200",
    # "4 2147483647 200 200",
    # "4 200 2147483647 200",
    # "4 800 200 2147483647",
    "4 200 2147 200",
    "4 800 200 2147",
    # "2 800 200 200",
]
args2 = [
    "5 800 200 200 9",
    "5 0 200 200",
    "5 800 0 200 9",
    "5 800 200 0 9",
    "5 800 0 0 9",
    "5 800 200 200 0",
    "4 410 200 200 9",
    "1 200 200 200",
    "4 2147483647 0 0 9",
    "4 200 210 200",
    "2 600 200 800",
    "4 310 200 200",
    "3 400 100 100 3",
]

args3 = [
    "200 800 200 200 9",
    "200 410 200 200",
]


def print_output(v, output):
    # print(output)
    if v == 0:
        print(colored(output, "blue"))
    if v == 1:
        if "no leaks are possible" in output:
            print(colored("NO LEAKS", "green"))
        else:
            print(colored("HAS LEAKS", "red"))
    if v == 2:
        if (
            "ERROR SUMMARY:\x1b[0m \x1b[35m0\x1b[0m errors from \x1b[35m0\x1b[0m contexts"
            in output
        ):
            print(colored("NO DATA RACE", "green"))
        else:
            print(colored("HAS DATA RACE", "red"))


v = 0
valgrinds = ["", "colour-valgrind ", "colour-valgrind --tool=helgrind "]

for i, arg in enumerate(args2):
    for v in range(3):
        print(f"TEST {i} --- args : {arg}")
        cmd = f"{valgrinds[v]}./../philo/philo/philo {arg}"
        print(cmd)
        print("======================================")
        stream = os.popen(cmd)
        output = stream.read()
        print_output(v, output)
        input()
