## Run model
source(data.R)

file = "~/44161/Assessment_Parcels_20250919.csv"

df <- loadData(file)
model <- lm('Total.Assessed.Value.Num ~ Total.Living.Area.Num + Assessed.Land.Area.Num', df)

summary(model)
