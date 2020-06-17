#!/usr/bin/env python3

'''
Simple terminal-based tool for calculating BMI and TEE.

References:
https://en.wikipedia.org/wiki/Body_mass_index
https://en.wikipedia.org/wiki/Basal_metabolic_rate#BMR_estimation_formulas
https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
'''

import argparse
import typing

# todo(Gustav): print percentage to next (or normal) bmi prime


def calculate_bmr1(weight: float, height: float, age: float, is_male: bool) -> float:
    '''
    Calculate basal metabolic rate according to the original
    Harris–Benedict equations published in 1918 and 1919.
    '''
    bmr_male = 66.5 + 13.75*weight + 5.003*height - 6.755*age
    bmr_female = 655 + 9.563*weight + 1.850*height - 4.676*age
    return bmr_male if is_male else bmr_female


def calculate_bmr2(weight: float, height: float, age: float, is_male: bool) -> float:
    '''
    Calculate basal metabolic rate according to
    the Harris–Benedict equations revised by Roza and Shizgal in 1984.
    '''
    bmr_male = 88.362 + 13.397*weight + 4.799*height - 5.677*age
    bmr_female = 447.593 + 9.247*weight + 3.098*height - 4.330*age
    return bmr_male if is_male else bmr_female


def calculate_bmr3(weight: float, height: float, age: float, is_male: bool):
    '''
    Calculate basal metabolic rate according to
    the Harris–Benedict equations revised by Mifflin and St Jeor in 1990
    '''
    bmr_male = 10*weight + 6.25*height - 5*age + 5
    bmr_female = 10*weight + 6.25*height - 5*age - 161
    return bmr_male if is_male else bmr_female


def mj_to_kcal(megajoules: float) -> float:
    return 238.85 * megajoules


def print_energy(bmr: float, pal: float):
    energy = bmr * pal
    kcal = mj_to_kcal(energy)
    print("Total Energy Expenditure: {0:0.1f} MJ, ({1:0.0f} kcal)".format(energy, kcal))


# category, upper bmi, upper bmi prime
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


def classify_bmi(bmi: float) -> str:
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


def print_bmi(length: float, weight: float):
    bmi = calculate_bmi(length, weight)
    bmi_prime = calculate_bmi_prime(bmi)
    print("BMI & prime: {0:0.1f} {1:0.0f}% ({2})".format(bmi, bmi_prime*100, classify_bmi(bmi)))


def calculate_weight(length: float, bmi: float):
    lim = length / 100
    lims = lim * lim
    return bmi * lims


def print_bmi_table_weights(length: float):
    def bmi_to_str(bmi: typing.Optional[float]):
        return '' if bmi is None else  '{0:0.1f}'.format(calculate_weight(length, bmi))

    last_upper = None
    for category, bmi_upper, _bmi_prime_upper in BMI:
        print('{}: {} - {}'.format(category, bmi_to_str(last_upper), bmi_to_str(bmi_upper)))
        last_upper = bmi_upper


def main():
    '''parsers arguments and prints bmi information'''
    parser = argparse.ArgumentParser(description='display bmi and estimated TEE')
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
        print_bmi(args.height, args.weight)
        print()
    print_bmi_table_weights(args.height)
    if args.weight is not None and args.age is not None:
        print()
        for bmr_function in [calculate_bmr1, calculate_bmr2, calculate_bmr3]:
            bmr = bmr_function(args.height, args.weight, args.age, args.is_male)
            print_energy(bmr, args.activity)


if __name__ == "__main__":
    main()
