# test-sample.R

library(testthat)
source("../r-hw1.r")

test_that("Bond Effective Sensitivity", {
  y = 0.03
  face = 2000000
  couponRate = 0.04
  m = 10
  ppy = 1


  x = getBPV(y, face, couponRate, m,  ppy)
  

  expect_equal(round(x), -1792)
})

test_that("Arrays1") {
  vec = matrix(data = 1:3,nrow = 1,ncol = 3)
  mat = matrix(data = 1:9,nrow = 3,ncol = 3,byrow = T)
  ans = vector(mode = "numeric",length = 3)

  x = MyMatMult(vec,mat)
  
  # x[1] == 30
  expect_equal(x[1], 30)
  # x[2] == 36
  expect_equal(x[2], 36)
  # x[3] == 42
  expect_equal(x[3], 42)

}

test_that("Conditioning") {
  x = FizzBuzz(40,45)
  # x[1] == "buzz" & x[2] == "41" & x[6] == "fizzbuzz"
  expect_equal(x[1], "buzz")
  expect_equal(x[2], "41")
  expect_equal(x[6], "fizzbuzz")
}