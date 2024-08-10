# test-sample.R

library(testthat)
source("../r-hw1.r")

test_that("add_numbers works correctly", {
  expect_equal(add_numbers(1, 2), 3)
  expect_equal(add_numbers(-1, -1), -2)
})
