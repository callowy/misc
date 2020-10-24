estimate_pi <- function(n) {
  # Calculate distance from origin
  z <- mapply(function(x,y) x^2 + y^2, runif(n), runif(n))

  # (area of circle / area of square) = (points in z with distance < 1 / all points in z)
  # points within unit circle / points within unit square
  4 * (length(z[z < 1]) / length(z))
}
