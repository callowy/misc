estimate_pi <- function(n) {

  z <- mapply(function(x,y) x^2 + y^2, runif(n), runif(n))

  4 * (length(z[z < 1]) / length(z))
}
