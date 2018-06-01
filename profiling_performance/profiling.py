import cProfile
import pstats

pr = cProfile.Profile()
pr.enable()
import threading


def dummy_func():
    pass


def test_func():
    t = threading.Thread(target=dummy_func)
    t.start()


p = cProfile.Profile()
p.runcall(test_func)
stats = pstats.Stats(p)
stats.sort_stats('cumulative')
stats.print_stats()
