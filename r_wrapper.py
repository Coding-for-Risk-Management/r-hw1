import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
import os

# Initialize R source
r = robjects.r
r.source('r-hw1.r')  # Path is now correct relative to root

class RFunctions:
    @staticmethod
    def get_bpv(y, face, coupon_rate, m, ppy):
        return float(r.getBPV(y, face, coupon_rate, m, ppy)[0])
    
    @staticmethod
    def my_mat_mult(vec, mat):
        r_vec = robjects.FloatVector(vec[0])
        r_mat = robjects.matrix(robjects.FloatVector([item for row in mat for item in row]), nrow=len(mat))
        result = r.MyMatMult(r_vec, r_mat)
        return list(result)
    
    @staticmethod
    def fizz_buzz(start, end):
        result = r.FizzBuzz(start, end)
        return list(result)