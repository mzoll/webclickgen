from webclickgen.clickstream_gen import ClickGenerator
from webclickgen.subgens import UserAgentGenerator, URLGenerator


def WebClickStreamGen(
        MEAN_CONCUR_USERS = 200,
        CLICK_DECAY_MEAN = 10,
        TIME_DECAY_MEAN_SEC = 60,

        RESESSION_PROB = 0.3,
        RESESSION_DIST_MEAN_SEC = 60*60,
        RESESSION_WIDTH_SEC = 15*60,

        NUM_PATH0_LEVELS = 8,
        MIN_NUM_DOC_LEVELS = 1,
        MAX_NUM_DOC_LEVELS = 10):

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

    return g
