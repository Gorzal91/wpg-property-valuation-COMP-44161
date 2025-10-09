# R/data.R
library(dplyr)
library(readr)

#' Load Winnipeg Assessment Data
#'
#' @param file Path to CSV file
#' @return Dataframe with assessment data and numeric columns
#' @export
#' @examples
# df <- loadData("assessment_parcels.csv")
loadData <- function(file) {
  # Wczytanie danych
  assessmentData <- read_csv(file, col_types = cols(.default = "c"))

  # Sprawdź istniejące kolumny
  existing_cols <- colnames(assessmentData)
  
  # Tworzenie kolumn numerycznych tylko jeśli nie istnieją
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
