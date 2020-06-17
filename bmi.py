#!/usr/bin/env python3
import argparse
import typing

# calculate basal metabolic rate

# The original Harris–Benedict equations published in 1918 and 1919
def calculate_bmr1(weight: float, height: float, age: float, is_male: bool) -> float:
    bmr_male = 66.5 + 13.75*weight + 5.003*height - 6.755*age
    bmr_female = 655 + 9.563*weight + 1.850*height - 4.676*age
    return bmr_male if is_male else bmr_female


# The Harris–Benedict equations revised by Roza and Shizgal in 1984.
def calculate_bmr2(weight: float, height: float, age: float, is_male: bool) -> float:
    bmr_male = 88.362 + 13.397*weight + 4.799*height - 5.677*age
    bmr_female = 447.593 + 9.247*weight + 3.098*height - 4.330*age
    return bmr_male if is_male else bmr_female


# The Harris–Benedict equations revised by Mifflin and St Jeor in 1990
def calculate_bmr3(weight: float, height: float, age: float, is_male: bool):
    bmr_male = 10*weight + 6.25*height - 5*age + 5
    bmr_female = 10*weight + 6.25*height - 5*age - 161
    return bmr_male if is_male else bmr_female


# The Mifflin St Jeor Equation
def calculate_bmr4(weight: float, height: float, age: float, is_male: bool):
    s = 5 if is_male else -161
    bmr = 10*height + 6.25*height - 5*age + s
    return bmr


def mj_to_kcal(mj: float) -> float:
    return 238.85 * mj


def displayEnergy(bmr: float, pal: float):
    energy = bmr * pal
    print("Total Energy Expenditure: {0:0.1f} MJ, ({1:0.0f} kcal)".format(energy, mj_to_kcal(energy)))


# category, bmi, bmi prime
BMI = [
    ('Very severely underweight', 15, 0.6),
    ('Severely underweight', 16, 0.64),
    ('Underweight', 18.5, 0.74),
    ('Normal (healthy weight)', 25, 1.0),
    ('Overweight', 30, 1.2),
    ('Obese Class I (Moderately obese)', 35, 1.4),
    ('Obese Class II (Severely obese)', 40, 1.6),
    ('Obese Class III (Very severely obese)', None, None)
]


def classifyBmi(bmi: float) -> str:
    for category, bmi_upper, _bmi_prime_upper in BMI:
        if bmi_upper is None or bmi <= bmi_upper:
            return category
    return ''


def calculate_bmi(length: float, weight: float):
    lim = length / 100
    lims = lim * lim
    bmi = weight / lims
    return bmi


def calculate_bmi_prime(bmi: float) -> float:
    upper_limit_optimal = 25
    return bmi/upper_limit_optimal

def displayBmi(length: float, weight: float):
    bmi = calculate_bmi(length, weight)
    bmi_prime = calculate_bmi_prime(bmi)
    print("BMI: {0:0.1f} {1:0.0f}% ({2})".format(bmi, bmi_prime*100, classifyBmi(bmi)))


def calculate_weight(length: float, bmi: float):
    lim = length / 100
    lims = lim * lim
    return bmi * lims


def listWeight(length: float):
    def f(bmi: typing.Optional[float]):
        if bmi is None:
            return ''
        else:
            return '{0:0.1f}'.format(calculate_weight(length, bmi))
    
    last_upper = None
    for category, bmi_upper, _bmi_prime_upper in BMI:
        print('{}: {} - {}'.format(category, f(last_upper), f(bmi_upper)))
        last_upper = bmi_upper


def main():
    parser = argparse.ArgumentParser(description='display bmi and stuff')
    parser.add_argument('height', type=float, help='height in cm')
    parser.add_argument('--weight', type=float, metavar='W', help='weight in kg')
    parser.add_argument('--age', type=float, metavar='A', help='age in years')
    parser.add_argument('--female', action='store_false', dest='is_male', help='for female')
    parser.add_argument('--activity', type=float, default=1.50, help='''activity level:
    Extremely inactive <1.40
    Cerebral palsy patient.

    Sedentary: 1.40 - 1.69
    Office worker getting little or no exercise.

    Moderately active: 1.70 - 1.99
    Construction worker or person running one hour daily.

    Vigorously active: 2.00 - 2.40
    Agricultural worker (non mechanized) or person swimming two hours daily.

    Extremely active >2.40
    Competitive cyclist.
    ''')

    args = parser.parse_args()

    if args.weight is not None:
        displayBmi(args.height, args.weight)
        print()
    listWeight(args.height)
    if args.weight is not None and args.age is not None:
        print()
        for f in [calculate_bmr1, calculate_bmr2, calculate_bmr3, calculate_bmr4]:
            bmr = f(args.height, args.weight, args.age, args.is_male)
            displayEnergy(bmr, args.activity)


if __name__ == "__main__":
    main()
