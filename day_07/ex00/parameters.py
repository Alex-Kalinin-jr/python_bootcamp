UP_C = 1.1
DOWN_C = 0.7


class Params:
    def __init__(self):
        self.params = None
    
    def set_etalon_params(self, params: dict):
        """
        Replaces list of presented params by the new one. It is your decision
        which params will be presented: from ["height, weight"] to ["cost", "power"]
        
        :return: None

        """
        self.params = params

    def get_param_from_user(self, param: str):
        """
        Returns user-defined value for param.

        :param param: Parameter for which user inputs the value.
        :type param: string
        :return: user-defined value.
        :rtype: int

        """
        result = ""
        validator = ResultValidator()
        while (True):
            result = input(f"Evaluate your {param}: ")
            # if (result.isdigit() and int(result) > 0):
            if (result.isdigit() and int(result) > 0 
                    and validator.validate_result(int(result), param)):
                break
        return int(result)

    def evaluate_params(self):
        """
        Returns coefficient based on value "1" and corrected according to user params
        compared with etalon params.
        In this implementation: if user param is less than etalon param, then coefficient
        is multiplied with DOWN_C, otherwise with UP_C.

        :return: coefficient.
        :rtype: float

        """
        if not self.params:
            return -1
        
        result = 1
        for param in self.params:
            user_param = self.get_param_from_user(param)
            result *= UP_C if self.params[param] < user_param else DOWN_C
        return result


class ResultValidator:

    def validate_result(self, result, key):
        """
        Sometime params should be within defined borders and under certain conditions
        This method is used to validate user input

        :return: True/False
        :rtype: boolean

        """
        res = True
        if key == 'blushing level':
            res = self._validate_blushing_level(result)
        elif key == 'pupillary dilation':
            res = self._validate_pupillary_dilation(result)
        return res

    def _validate_blushing_level(self, result):
        """
        Validates if result is within range 1-6 for blushing level

        :return: True/False
        :rtype: boolean

        """
        return result >= 1 and result <= 6

    def _validate_pupillary_dilation(self, result):
        """
        Validates if result is within range 2-8 for pupillary dilation

        :return: True/False
        :rtype: boolean

        """
        return result >= 2 and result <= 8
