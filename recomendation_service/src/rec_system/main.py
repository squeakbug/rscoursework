from nlp.nlp_cli import User, main_loop
from domain import calc_measure_main
from recomendation_system import RecomendationSystem, ClosenessStrategy


def main():
    rec_system = RecomendationSystem()
    rec_system.set_closeness_strategy(ClosenessStrategy.NearDistinctSeeds)
    rec_system.calc_measure_function(calc_measure_main)

    user = User()

    while True:
        rc = main_loop(rec_system, user)
        if rc == 1:
            return 0


if __name__ == "__main__":
    main()
