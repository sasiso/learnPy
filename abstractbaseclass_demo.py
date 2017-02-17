import abc
from abc import ABCMeta


class Processor:
    """

    """

    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def process(self, image):
        """
        process Input Image
        :param image: Input Image
        :return: A processed Image
        """
        return NotImplemented

    @abc.abstractmethod
    def enable(self):
        """
        Enables processor
        """
        return NotImplemented

    @abc.abstractmethod
    def disable(self):
        """
        Disables processor
        """
        return NotImplemented


class IlluminationCorrection(Processor):

    def __init__(self, factor):
        super(IlluminationCorrection, self).__init__()
        self._factor = factor
        self._enabled = True

    def enable(self):
        """
        Enable processor
        :return:
        """
        self._enabled = True

    def disable(self):
        self._enabled = False

    def set_factor(self, factor):
        self._factor = factor

    def process(self, image):
        if self._enabled:
            print "IlluminationCorrection processing Image", self._factor
        else:
            print "IlluminationCorrection disabled", self._factor


class Another(Processor):

    def __init__(self, factor):
        super(Another, self).__init__()
        self._factor = factor

    def process(self, image):
        print "Another processing Image"


class ImageProcessingChain:
    """

    """

    def __init__(self):
        self._processors = []

    def add_processor(self, processor):
        """

        :param processor:
        :return:
        """
        self._processors.append(processor)

    def process(self, image):
        """

        :param image:
        :return:
        """
        for p in self._processors:
            p.process(image)

        return image

chain = ImageProcessingChain()
illumination_correction = IlluminationCorrection(1)

chain.add_processor(illumination_correction)
chain.add_processor(Another(3))


chain.process("string")
illumination_correction.disable()
chain.process("string")

illumination_correction.enable()
chain.process("string")

illumination_correction.set_factor(10)
chain.process("string")
