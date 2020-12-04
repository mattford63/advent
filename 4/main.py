import re


def to_dict(lol):
    return {l[0]: l[1] for l in lol}


def read_input(vfunc):
    with open("input", "rt") as fd:
        return [
            vfunc(to_dict(k))
            for k in [
                [kp.split(":") for kp in x]
                for x in [p.split() for p in fd.read().split("\n\n")]
            ]
        ].count(True)


def read_input_test():
    with open("input", "rt") as fd:
        return [
            [kp.split(":") for kp in x]
            for x in [p.split() for p in fd.read().split("\n\n")]
        ]


def valid_keys(p):
    return all(k in p for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def validate(p):

    def digit_range(s, lb, ub):
        if re.match(r"^\d{4}$", s):
            i = int(s)
            return i >= lb and i <= ub
        return False

    def height(s):
        r = re.match(r"^(\d+)(\w+)$", s)
        if r:
            i = int(r[1])
            if r[2] == "cm":
                return i >= 150 and i <= 193
            if r[2] == "inches":
                return i >= 59 and i <= 76
        return False

    def hair_color(s):
        if re.match(r"^#([0-9a-f]{6})$", s):
            return True
        return False

    def eye_color(s):
        return any(s == i for i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

    def pid(s):
        if re.match(r"^\d{9}$", s):
            return True
        return False

    if valid_keys(p):
        return all(
            [
                digit_range(p["byr"], 1920, 2002),
                digit_range(p["iyr"], 2010, 2020),
                digit_range(p["eyr"], 2020, 2030),
                height(p["hgt"]),
                hair_color(p["hcl"]),
                eye_color(p["ecl"]),
                pid(p["pid"]),
            ]
        )
    return False


read_input(valid_keys)
read_input(validate)
