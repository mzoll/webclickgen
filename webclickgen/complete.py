from webclickgen.clickstream_gen import ClickGenerator
from webclickgen.subgens import UserAgentGenerator, URLGenerator


def WebClickStreamGen(
        TIME_DECAY_MEAN_SEC = 30,
        CLICK_DECAY_MEAN = 10,

        MEAN_CONCUR_USERS = 200,

        NUM_PATH0_LEVELS = 8,
        MIN_NUM_DOC_LEVELS = 1,
        MAX_NUM_DOC_LEVELS = 10):

    url_gen = URLGenerator(NUM_PATH0_LEVELS, MIN_NUM_DOC_LEVELS, MAX_NUM_DOC_LEVELS)
    ua_gen = UserAgentGenerator()

    g = ClickGenerator(MEAN_CONCUR_USERS, CLICK_DECAY_MEAN, TIME_DECAY_MEAN_SEC, [url_gen, ua_gen])

    return g
