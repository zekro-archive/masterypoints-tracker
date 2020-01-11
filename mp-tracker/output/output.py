from abc import ABC, abstractmethod, abstractstaticmethod


class Output(ABC):
    """
    This abstract class is used as 'interface' for
    output drivers where collected data will be
    pushed to.
    """

    @abstractmethod
    def push_data_set(self, data, **kwargs):
        """
        Function which will be executed to push
        data.

        `data : object`
        Data model which will be pushed.

        `**kwargs`
        Additional optional named arguments passed to
        the push function of the output driver.
        """
        pass

    @abstractstaticmethod
    def register_args(parser):
        """
        Static method which will register custom command
        line arguments which then can be passed to the
        constructor of the driver.

        `parser : argparse.Parser`
        Command line parser instance.
        """
        pass

