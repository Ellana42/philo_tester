# TODO Add deaths and min eaten count
# TODO Add interruption for never die
from collections import Counter
import os
from typing import List

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
    "5 800 200 200 2",
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


class Action:
    def __init__(self, time, philo, action):
        self.time = time
        self.philo = philo
        self.action = action

    @staticmethod
    def line_to_action(line_output):
        words = line_output.split(" ")
        if len(words) > 3:
            return (words[0], words[1], words[3])
        if len(words) == 3:
            return (words[0], words[1], words[2])
        return (None, None, None)


class Philo:
    def __init__(self, index: int, actions: List[Action]):
        self.index = index
        self.actions = actions

    def get_nb_meals(self):
        nb_meals = 0
        for action in self.actions:
            if action.action == "eating":
                nb_meals += 1
        return nb_meals

    def is_dead(self):
        nb_meals = 0
        for action in self.actions:
            if action.action == "died":
                return 1
        return 0


class Simulation:
    def __init__(self, actions: List[Action]):
        self.actions = actions
        self.philos = self.init_philos()

    def init_philos(self):
        philos = {}
        for action in self.actions:
            philos.setdefault(action.philo, []).append(action)
        philos_list = []
        for i in range(len(philos)):
            philos_list.append(Philo(i, philos[str(i)]))
        return philos_list


def parse_output(output):
    actions = [Action(**Action.line_to_action(line)) for line in output.split("\n")]
    actions = {}
    for line in output.split("\n"):
        action = line_to_action(line)
        if action[0] is not None:
            if action[1] not in actions:
                actions[action[1]] = []
            actions[action[1]].append(action[0])
    return actions


def count_min_eat(output):
    actions = parse_output(output)
    return Counter(actions["eating"]).most_common()[:-2:-1][0][1]


def print_output(v, output):
    # print(output)
    if v == 0:
        print(colored(output, "blue"))
        print("----------------------")
        print(colored(f"Min meals : {count_min_eat(output)}", "green"))
        if "die" in output:
            print(colored("Death", "red"))
        else:
            print(colored("No death", "green"))
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
