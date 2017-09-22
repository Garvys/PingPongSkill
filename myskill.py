# -*-: coding utf-8 -*-
""" Skeleton Snips skill. """

class MySkill:
    """ Skeleton Snips skill. """

    def __init__(self, hostname, light_ids):
        """
        :param hostname: hostname for some IoT device
        :param light_ids: A list of light IDs
        """
        self.hostname = hostname
        self.light_ids = light_ids

    def turn_on(self):
        """ Turn on something. """
        print("Turn on")
        
    def turn_off(self):
        """ Turn of something. """
        print("Turn off")

    def set_color_name(self, object_color):
        """ Set an object color. """
        print("Set object color to {}".format(object_color))
