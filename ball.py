# Description:
# defines the ball class that holds the physical attributes of the ball
# also holds the position, velocity and acceleration of the ball at any given time

import math

class Ball:
    def __init__(self, pos_vec, vel_vec, acceleration_vec):
        # mass in grams
        # diameter in inches
        self.MASS = 145 
        self.DIAMETER = 2.9
        self.AREA = math.pi * (self.DIAMETER / 2) ** 2
        self.pos = pos_vec
        self.vel = vel_vec
        self.accel = acceleration_vec

    def change_ball_pos(self, time_int):
        #changes the ball's position based off its current vel_vec
        return 42

    def change_ball_vel(self, time_int):
        #changes the ball's current velocity based off its current acceleration
        return 42

    def change_ball_accel(self, time_int):
        # change ball's acceleration based off gravity and calculated magnus effect or pitch's break numbers
        return 42

    def update_ball(self, time_int):
        # updates the ball's position, velocity and acceleration over a certain time interval
        self.change_ball_pos(self, time_int)
        self.change_ball_vel(self, time_int)
        self.change_ball_accel(self, time_int)
    
    

        




    


    