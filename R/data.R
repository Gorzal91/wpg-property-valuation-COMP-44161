# R/data.R
library(dplyr)
library(readr)

#' Load Winnipeg Assessment Data
#'
#' @param file Path to CSV file
#' @return Dataframe with assessment data and numeric columns
#' @export
#' @examples

loadData <- function(file) {

  # Load data
  assessmentData <- read_csv(file, col_types = cols(.default = "c"))

  # Check existing columns
  existing_cols <- colnames(assessmentData)
  
  # Create numeric columns if they don't exist

  if (!"total_living_area_Num" %in% existing_cols) {
    assessmentData$total_living_area_Num <- as.numeric(assessmentData$total_living_area) %>% replace(is.na(.), 0)
  }
  
  if (!"assessed_land_area_Num" %in% existing_cols) {
    assessmentData$assessed_land_area_Num <- as.numeric(assessmentData$assessed_land_area) %>% replace(is.na(.), 0)
  }
  
  if (!"total_assessed_value_Num" %in% existing_cols) {
    assessmentData$total_assessed_value_Num <- parse_number(assessmentData$total_assessed_value) %>% replace(is.na(.), 0)
  }

  return(assessmentData)
}

