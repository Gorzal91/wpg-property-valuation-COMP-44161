# Technical Test - Artur Gorzalczynski

**Opportunity No. 44161**

# Winnipeg Property Valuation Model

This project develops an **Automated Valuation Model (AVM)** to predict the assessed value of residential properties in Winnipeg using open data from the [City of Winnipeg Open Data Portal](https://data.winnipeg.ca/Assessment-Taxation-Corporate/Assessment-Parcels/d4mq-wa44/about_data).

It was created as part of the **Technical Test Opportunity No. 44161**, following the requirements to:

- Build a simple but well-structured predictive model.
- Use reproducible open-source tools (Python and R).
- Provide clear documentation and accessible communication.

## Accessible Summary (≤200 words)

This project delivers an automated valuation model for residential properties in Winnipeg. The model predicts the assessed value of a property based on its features, specifically the total living area and assessed land area. Two machine learning approaches were implemented: Linear Regression and Random Forest Regressor. The model enables rapid estimation of property values, supporting decision-making processes in property management, investment, and municipal assessment. The outputs include predicted property values, model evaluation metrics, and correlation tables for key features. The code is structured for reproducibility and can be executed in a Python / R environments using open-source libraries. Example predictions are provided for clarity. The model is designed to be modular, allowing integration with additional datasets or property features in the future.

---

## Detailed Technical Summary (≤500 words)

The project develops an automated valuation system for residential properties in Winnipeg using data sourced from the City of Winnipeg Open Data Portal, specifically the Assessment dataset. The workflow follows a structured software development approach to ensure code clarity, reproducibility, and modularity.

### Data Preparation

- Relevant numerical features were extracted: `total_living_area_Num` and `assessed_land_area_Num`.
- The target variable is `total_assessed_value_Num`.
- Missing values in the dataset were identified and handled by replacing `NaN` entries with 0 for numeric features. In the case of the python code, zero values ​​were removed for comparison of results without removal
- All data preprocessing (for Python) steps are documented in the `src` folder.

### Modelling

- **Linear Regression**: provides interpretable coefficients showing the relationship between features and assessed property values.
- **Random Forest Regressor**: a non-linear ensemble method capturing complex interactions between features.
- Both models were trained on 80% of the dataset and tested on 20%, with evaluation metrics including Mean Absolute Error (MAE) and R².

### Outputs

- Predictions are stored in CSV files (`results/outputs`), including example predictions for test properties.
- Model evaluation summaries are saved with clear MAE and R² metrics.
- Feature correlation tables are provided to inform about multicollinearity and variable importance.
- A simple exploratory analysis of the empirical data for the dependent variable was also performed (using Python). A histogram of the variable's distribution is available in the results/figures folder.

### Assumptions

- The model assumes that property value depends primarily on living area and land area.
- Only free and open-source Python libraries are used to maintain reproducibility.
- Large model artifacts (Pickle files) are not included in the repository to comply with GitHub file size limits.

### Reproducibility

- Code is organized in a modular structure (`data`,`notebooks`,`outputs`,`R`, `results/outputs`,`src`).
- Models can be retrained or extended with additional features by executing the Python scripts.
- Example predictions illustrate the use of both Linear Regression and Random Forest models for decision support.

### Summary

This work provides a robust, transparent, and reproducible framework for automated property valuation in Winnipeg. The models are suitable for municipal assessment support, real estate analysis, and other business applications requiring property valuation insights.

For future consideration, integration of additional property and neighborhood-level data could further improve predictive accuracy. Continuous model retraining and validation are recommended to account for evolving market conditions.

#### AI Disclosure

During the preparation of this submission, AI-assisted tools were used exclusively to draft textual descriptions, summaries, and documentation. All data processing, code development, and model implementation were performed manually without AI assistance.
