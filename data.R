library(readr)
library(dplyr)

#' Load Winnipeg Data
#'
#' @param File name as string
#' @return Dataframe of assessment data
#' @export
#'
#' @examples
loadData <- function(file){
    assessmentData <- read.csv(file)
    assessmentData['Total.Living.Area.Num'] <- as.numeric(assessmentData$Total.Living.Area) %>% replace(is.na(.), 0)
    assessmentData['Assessed.Land.Area.Num'] <- as.numeric(assessmentData$Assessed.Land.Area) %>% replace(is.na(.), 0)
    assessmentData['Total.Assessed.Value.Num'] <- readr::parse_number(assessmentData$Total.Assessed.Value) %>% replace(is.na(.), 0)
    return(assessmentData)
}


