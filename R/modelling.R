library(ggplot2)
library(knitr)
library(tibble)
library(ggcorrplot)

source("R/data.R")

file = "data/assessment_parcels.csv"

df <- loadData(file)

# 1. Correlation analysis between main numeric variables

numeric_df <- df[, c("total_living_area_Num", "assessed_land_area_Num", "total_assessed_value_Num")]

corr <- cor(numeric_df, use = "complete.obs")

corr_rounded <- round(corr, 2)

print(corr)

write.csv(corr_rounded, "results/outputs/r_correlation_table.csv", row.names = TRUE)


# 2. Linear regression model


model <- lm('total_assessed_value_Num ~ total_living_area_Num + assessed_land_area_Num', df) #change . to _

summary(model)

results <- summary(model)$coefficients
write.csv(results, "results/outputs/r_model_summary.csv")


# Save model summary as a table
results_table <- as.data.frame(results)
results_table <- tibble::rownames_to_column(results_table, var = "Variable")
print(results_table, row.names = FALSE)  # wyświetlenie tabeli w konsoli

# 3. Coefficients plot

coef_plot <- results_table[results_table$Variable != "(Intercept)", ]


# add color based on significance level (p-value)

coef_plot <- results_table[results_table$Variable != "(Intercept)", ]
coef_plot$Significant <- ifelse(coef_plot$`Pr(>|t|)` < 0.05, "Yes", "No")

ggplot(coef_plot, aes(x = reorder(Variable, Estimate), y = Estimate, color = Significant)) +
  geom_point(size = 4) +
  geom_errorbar(aes(ymin = Estimate - `Std. Error`, ymax = Estimate + `Std. Error`), width = 0.2) +
  scale_color_manual(values = c("Yes" = "#4AB687", "No" = "#D5F7E6")) +
  coord_flip() +  # Flip coordinates
  labs(title = "Linear Model Coefficients with Std. Error",
       x = "",
       y = "Estimate ± Std. Error") +
  theme_minimal(base_size = 14) +
  theme(legend.position = "bottom")


# Save the plot to png file

ggsave("results/figures/r_model_coefficients.png", width = 8, height = 5)

# 4. Example predictions based on the model 

new_property <- data.frame(
  total_living_area_Num=1500, # example living area in sqft
  assessed_land_area_Num=4000 ) # example land area in sqft
predicted_value <- predict(model, new_property)
cat("Predicted value for new property: $", round(predicted_value, 0), "\n")