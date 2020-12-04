import re

def getLinesForDay(day):
    with open(f'day{day}/input.txt') as f:
        lines = f.read().splitlines()
        lines.append("") # Adding empty line to get last passport
        return lines

def buildPassport(passport, line):
    entities = line.split()
    for entity in entities:
        keyValuePair = entity.split(":")
        passport[keyValuePair[0]] = keyValuePair[1]
    return passport

def byrCheck(passport):
    return 'byr' in passport and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002

def iyrCheck(passport):
    return 'iyr' in passport and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020

def eyrCheck(passport):
    return 'eyr' in passport and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

def hgtCheck(passport):
    if not passport.get('hgt'):
        return False
    hgtMatch = re.compile('([0-9]+)(in|cm)$').match(passport['hgt'])
    if not hgtMatch:
        return False
    HGT_CHK = 'hgt' in passport and bool(hgtMatch)
    hgt = int(hgtMatch.group(1))
    if hgtMatch.group(2) == 'cm':
        HGT_CHK = HGT_CHK and ( hgt >= 150 and hgt <= 193)
    else:
        HGT_CHK = HGT_CHK and ( hgt >= 59 and hgt <= 76)
    return HGT_CHK

def hclCheck(passport):
    if 'hcl' not in passport:
        return False
    hclMatch = re.compile('#[0-9a-f]{6,6}').match(passport.get('hcl'))
    return bool(hclMatch)

def eclCheck(passport):
    if 'ecl' not in passport:
        return False
    return bool(re.compile('amb|blu|brn|gry|grn|hzl|oth').match(passport.get('ecl')))

def pidCheck(passport):
    if 'pid' not in passport:
        return False
    return bool(re.compile('[0-9]{9,9}$').match(passport.get('pid')))

def validateV1(passport):
    BYR_CHK = 'byr' in passport
    IYR_CHK = 'iyr' in passport
    EYR_CHK = 'eyr' in passport
    HGT_CHK = 'hgt' in passport
    HCL_CHK = 'hcl' in passport
    ECL_CHK = 'ecl' in passport
    PID_CHK = 'pid' in passport

    if BYR_CHK and IYR_CHK and EYR_CHK and HGT_CHK and HCL_CHK and ECL_CHK and PID_CHK:
        return True
    else:
        return False

def validateV2(passport):
    if byrCheck(passport) and iyrCheck(passport) and eyrCheck(passport) and hgtCheck(passport) and hclCheck(passport) and eclCheck(passport) and pidCheck(passport):
        return True
    else:
        return False

def run(validate):
    total = 0
    passportBuilder = {}
    validPassports = []
    for line in getLinesForDay(4):
        if len(line) > 0:
            passportBuilder = buildPassport(passportBuilder, line)
        else:
            total += 1
            if validate(passportBuilder):
                validPassports.append(passportBuilder)
            passportBuilder = {}
    print(f'Total passports - {total}')
    return len(validPassports)

print(f'Puzzle 1: Number of valid passports = {run(validateV1)}')


assert not byrCheck({'b':'1920'})
assert not byrCheck({'byr':'1919'})
assert byrCheck({'byr':'1920'})
assert byrCheck({'byr':'1987'})
assert byrCheck({'byr':'2002'})
assert not byrCheck({'byr':'2003'})

assert not iyrCheck({'b':'1920'})
assert not iyrCheck({'iyr':'2009'})
assert iyrCheck({'iyr':'2010'})
assert iyrCheck({'iyr':'2015'})
assert iyrCheck({'iyr':'2020'})
assert not iyrCheck({'iyr':'2021'})

assert not eyrCheck({'b':'1920'})
assert not eyrCheck({'eyr':'2019'})
assert eyrCheck({'eyr':'2020'})
assert eyrCheck({'eyr':'2025'})
assert eyrCheck({'eyr':'2030'})
assert not eyrCheck({'eyr':'2031'})

assert not hgtCheck({'b':'1920'})
assert not hgtCheck({'hgt':'149cm'})
assert hgtCheck({'hgt':'150cm'})
assert hgtCheck({'hgt':'160cm'})
assert hgtCheck({'hgt':'193cm'})
assert not hgtCheck({'hgt':'194cm'})
assert not hgtCheck({'hgt':'58in'})
assert hgtCheck({'hgt':'59in'})
assert hgtCheck({'hgt':'70in'})
assert hgtCheck({'hgt':'76in'})
assert not hgtCheck({'hgt':'77in'})

assert not hclCheck({'b':'1920'})
assert not hclCheck({'hcl':'1920'})
assert hclCheck({'hcl':'#999999'})
assert hclCheck({'hcl':'#099a75'})
assert hclCheck({'hcl':'#abcde9'})
assert not hclCheck({'hcl':'#z34343'})
assert not hclCheck({'hcl':'%999999'})

assert not eclCheck({'h':'#999999'})
assert not eclCheck({'ecl':'123'})
assert not eclCheck({'ecl':'green'})
assert eclCheck({'ecl':'amb'})
assert eclCheck({'ecl':'hzl'})

assert not pidCheck({'el':'amb'})
assert pidCheck({'pid':'989898988'})
assert pidCheck({'pid':'000000001'})
assert not pidCheck({'pid':'823232223222'})
assert not pidCheck({'pid':'33'})
assert not pidCheck({'pid':'oioioiooi'})

print(f'Puzzle 2: Number of valid passports = {run(validateV2)}')
