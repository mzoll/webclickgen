#!/usr/bin/env python

from webclickgen.clickstream_gen import ClickGenerator
from webclickgen.subgens import UserAgentGenerator, URLGenerator

# --- parameters for click-stream
N_CLICKS_TOTAL = int(1E+4)

TIME_DECAY_MEAN_SEC = 30
CLICK_DECAY_MEAN = 10

MEAN_CONCUR_USERS = 200

NUM_PATH0_LEVELS = 8
MIN_NUM_DOC_LEVELS = 1
MAX_NUM_DOC_LEVELS = 10

RESESSION_PROB = 0.2
RESESSION_DIST_MEAN_SEC = 24*60*60
RESESSION_WIDTH_SEC = 60*60


def testClickStreamSampleGen():
    url_gen = URLGenerator(NUM_PATH0_LEVELS, MIN_NUM_DOC_LEVELS, MAX_NUM_DOC_LEVELS)
    ua_gen = UserAgentGenerator()

    g = ClickGenerator(
            MEAN_CONCUR_USERS,
            CLICK_DECAY_MEAN,
            TIME_DECAY_MEAN_SEC,
            RESESSION_PROB,
            RESESSION_DIST_MEAN_SEC,
            RESESSION_WIDTH_SEC,
            [url_gen, ua_gen])

    clicks = []
    for i in range(N_CLICKS_TOTAL):
        clicks.append(g.next())

    print(len(clicks))
    print(clicks[-1])


#----------------------------------------------
if __name__=="__main__":
    testClickStreamSampleGen()

