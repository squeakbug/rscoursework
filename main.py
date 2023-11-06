from cli import main_loop
from domain import calc_measure_main
from recomendation_system import RecomendationSystem, ClosenessStrategy


def main():
    rec_system = RecomendationSystem()
    rec_system.set_closeness_strategy(ClosenessStrategy.NearDistinctSeeds)
    rec_system.calc_measure_function(calc_measure_main)

    likes = []
    dislikes = []

    while True:
        rc = main_loop(rec_system, likes, dislikes)
        if rc == 1:
            return 0


if __name__ == "__main__":
    main()
