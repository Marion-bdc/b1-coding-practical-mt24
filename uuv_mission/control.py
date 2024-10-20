# control.py

class Controller:
    def __init__(self, Kp, Kd):
        """
        Initialize the controller with the given gains.
        Kp (float): Proportional gain.
        Kd (float): Derivative gain.
        """
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0.0

    def compute_control_action(self, error):
        """
        Compute the control action using a PD controller.
        
        Parameters:
        error (float): Current error e(t).
        
        Returns:
        float: Control action u(t).
        """
        control_action = self.Kp * error + self.Kd * (error - self.previous_error)
        self.previous_error = error
        return control_action