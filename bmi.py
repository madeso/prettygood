#!/usr/bin/env python3
import argparse


def displayEnergy(length: float, weight: float, age: float, is_male: bool, activity: float = 120):
    energy_rest_male = 66.5 + (13.75 * weight) + (5.003 * length) - (6.775 * age)
    energy_rest_female = 655.1 + (9.563 * weight) + (1.850 * length) - (4.676 * age)
    energy_rest = energy_rest_male if is_male else energy_rest_female
    energy = energy_rest * (activity / 100.0)
    print("Enerrgiförbrukning = {0:0.1f}".format(energy))


def classifyBmi(bmi: float) -> str:
    if bmi < 17.50: return "Undervikt"
    if bmi < 18.50: return "Lite Undervikt"
    if bmi < 24.99: return "Normalvikt"
    if bmi < 29.99: return "Övervikt"
    return "Fetma"


def displayBmi(length: float, weight: float):
    lim = length / 100
    lims = lim * lim
    bmi = weight / lims
    print("BMI: {0:0.1f} {1}".format(bmi, classifyBmi(bmi)))


def listWeight(length: float):
    lim = length / 100
    lims = lim * lim

    print("Undervikt: mindre än {0:0.1f}".format(17.50 * lims))
    print("Lite Undervikt: mindre än {0:0.1f}".format(18.50 * lims))
    print("Normalvikt: {0:0.1f} - {1:0.1f}".format(18.50 * lims, 24.99 * lims))
    print("Övervikt: {0:0.1f} - {1:0.1f}".format(25.00 * lims, lims * 29.99))
    print("Fetma: Mer än {0:0.1f}".format(lims * 30.00))


def main():
    parser = argparse.ArgumentParser(description='display bmi and stuff')
    parser.add_argument('height', type=float, help='height in cm')
    parser.add_argument('--weight', type=float, metavar='W', help='weight in kg')
    parser.add_argument('--age', type=float, metavar='A', help='age in years')
    parser.add_argument('--female', action='store_false', dest='is_male', help='for female')
    parser.add_argument('--activity', type=float, default=120, help='activity')

    args = parser.parse_args()

    listWeight(args.height)
    if args.weight is not None:
        displayBmi(args.height, args.weight)
        if args.age is not None:
            displayEnergy(args.height, args.weight, args.age, args.is_male, args.activity)

if __name__ == "__main__":
    main()
