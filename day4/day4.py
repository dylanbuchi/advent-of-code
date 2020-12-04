import os
import re


def get_part1(passports: list):

    valid_passports = 0

    fields = get_fields(passports)
    pairs = get_pairs(fields)

    for pair in pairs:
        if (len(pair) == 7):
            valid_passports += 1

    return valid_passports


def get_part2(passports: list):
    valid_passports = 0
    fields = get_fields(passports)
    pairs = get_pairs(fields)
    sorted_pairs = sort_pairs(pairs)

    for pair in sorted_pairs:
        if (len(pair) == 7):
            result = check_passports_by_rules(pair.values())

            if False not in result.values():
                valid_passports += 1

    return valid_passports


def get_fields(passports: list):
    fields = []

    for passport in passports:
        field = passport.split()
        fields.append(field)

    return fields


def get_pairs(fields: list):
    pairs_list = []
    optional_field = 'cid'

    for field_list in fields:
        pairs = {}

        for field in field_list:
            key, value = field.split(':')

            if key == optional_field:
                continue
            else:
                pairs[key] = value

        pairs_list.append(pairs)

    return pairs_list


def sort_pairs(pairs: list):
    sorted_pairs = []

    for pair in pairs:
        sorted_pairs.append({k: pair[k] for k in sorted(pair)})

    return sorted_pairs


def get_passports(file: str):
    with open(file) as f:
        contents = f.read()

    passports = contents.split('\n\n')
    return passports


def check_passports_by_rules(values: list):
    byr, ecl, eyr, hcl, hgt, iyr, pid = values

    ecl_rule = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    hcl_rule = re.match(r'^#[0-9a-f]{6}', hcl)

    hgt_rule = False

    if (hgt.endswith('cm')):
        hgt_num = int(hgt[:-2])
        hgt_rule = 150 <= hgt_num <= 193

    elif (hgt.endswith('in')):
        hgt_num = int(hgt[:-2])
        hgt_rule = 59 <= hgt_num <= 76

    rules = {
        'byr': 1920 <= int(byr) <= 2002,
        'ecl': ecl in ecl_rule,
        'eyr': 2020 <= int(eyr) <= 2030,
        'hcl': hcl_rule != None,
        'hgt': hgt_rule,
        'iyr': 2010 <= int(iyr) <= 2020,
        'pid': len(pid) == 9 and pid.isdigit()
    }

    return rules


def main():
    file = os.path.join(os.getcwd(), 'day4', 'passports.txt')
    passports = get_passports(file)

    part1 = get_part1(passports)
    part2 = get_part2(passports)

    print(f'Part 1: {part1}')
    print(f'Part 2: {part2}')


if __name__ == "__main__":
    main()