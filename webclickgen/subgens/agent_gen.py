
import fake_useragent
from fake_useragent import UserAgent
ua = UserAgent()


class UserAgentGenerator(object):
    class UserAgentGen_child(object):
        """ Subclass to UserAgentGenerator which can be spawned through .get_child() and reponds to step() and get_dict() """
        def __init__(self, **kwargs):
            self.reset()
        def step(self):
            pass
        def reset(self):
            """ generate the agent string once """
            self.agent_string = ua.random
        def soft_reset(self):
            pass
        def get_dict(self):
            return {'user_agent': self.agent_string}

    def __init__(self, **child_kwargs):
        """ Generates a random User_agent string """
        self.child_kwargs = child_kwargs

    def get_child(self, **kwargs):
        param_dict = self.child_kwargs.copy()
        param_dict.update(kwargs)
        return self.UserAgentGen_child(**param_dict)

