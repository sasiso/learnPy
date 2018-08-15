from threading import Thread
import multiprocessing



def func():
    for i in range(100):
        print i

if __name__ == "__main__":

    from pycallgraph import PyCallGraph
    from pycallgraph.output import GraphvizOutput
    from pycallgraph.config import Config
    from pycallgraph.globbing_filter import GlobbingFilter

    g = GlobbingFilter(
        exclude=['pycallgraph.*'],
        include=['*'],
    )

    config = Config(trace_filter=g, max_depth=5, include_stdlib=True, include_pycallgraph=True, verbose=False,
                    groups=False)

    with PyCallGraph(output=GraphvizOutput(output_file="thread_time.png"), config=config):
        t = Thread()
        t.start()

    with PyCallGraph(output=GraphvizOutput(output_file="process.png"), config=config):
        o = multiprocessing.Pool(processes=1)
        o.apply(func)