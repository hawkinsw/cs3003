module Forecast where

data Weather = Precipitation Integer | Overcast [Char] | Clear

showWeather :: Weather -> String
showWeather Clear = "The weather is clear."
showWeather (Precipitation inches) = "There are " ++ (show inches) ++ " inches of precipitation."
showWeather (Overcast why) = "It is overcast because of " ++ why ++ "."

instance Show Weather where
    show weather = showWeather weather

instance Eq Weather where
    (==) Clear Clear = True
    (==) (Precipitation o) (Precipitation p) = o==p
    (==) (Overcast o) (Overcast p) = o==p
    (==) _ _ = False


