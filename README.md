# HISTORICAL SHORE LEVEL CALCULATOR
#### Video Demo:  https://youtu.be/46UP-zHoFNM
#### Description:
During the last ice age, the weight of the glaciers led to the formation of a depression within the region of Fennoscandia. During the Holocene, the release of pressure from the melting of glaciers caused the crust of the Earth to rebound, resulting in land rising (uplift) within the Baltic Sea region. While the uplift was more significant during the early Holocene period, it is still happening today. These present uplift rates can be used to calculate historical shore levels.

The project's objective was to automate the calculation developed by geophysicist Martin Ekman in his article, "Calculation of Historical Shore Levels back to 500 A.D. in the Baltic Sea Area due to Postglacial Rebound." The code's current form is simple. It takes most of the variables used in the calculation from the user as inputs and prints the averaged result of the calculations. Although it's a simplistic code, it streamlines a tedious computation. Furthermore, the historical shore level calculator allows the user to specify the year with great precision. Previously, shore levels were typically calculated within specific intervals, such as 50, 100, or 500 years.

The code currently lacks refined measures to verify correct input and to prompt the user again. A very broad try/except (TypeError, UnboundLocalError, ValueError) is used in the main() function for now, instead of verifying inputs at each function. This is done on purpose because in the future version of the code, a number of the variables will be taken from raster files instead of being input by users (more in TODO). The current functions perform the following tasks:

**get_mean_sea_level():** The user has to select a maritime region within the Baltic Sea for which they want to calculate the historical shore level. The regions are listed as keys, with values representing the medium sea-level within the region. The keys are printed for the user so they know what to write as input to call the value.

**get_Ua():** Enter the current uplift rate relative to sea level from mareographic stations. It must be expressed in millimeters per year (mm/yr) and takes decimal values.

**get_Uc():** Use the NKG2016LU model to calculate the current uplift rate from satellite stations. The NKG2016LU model calculates theoretical, climate-free, leveled uplift with a maximum gravity of 0.6 mm. The input must be expressed in millimeters per year (mm/yr).

**get_time():** The user inputs the year for which they want the shore level calculated. The calculator follows Ekman’s original timeframe, calculating shore levels between 500 and 2000 CE. Therefore, a value between 500 and 2000 must be entered.

**calculate_exponential_uplift(Uc, t):** This function creates a dictionary with an exponential uplift value for each year between 500 and 2000 CE. The function searches the dictionary for the year and, if found, provides the corresponding exponential uplift value. I found this to be the best way to understand the code, even if there are better ways to code the loops.

**calculate_uncertainty_value(t):** The shore levels are imprecise. This function calculates the uncertainty value depending on the year being calculated.

**calculate_shorelevel_mareograph(Ua, ΔU, t, E, H0):** This function uses the values from the main function to calculate the shore level with mareographic uplift of Ua.

**calculate_shorelevel_satellite(Uc, ΔU, t, E, H0):** This function takes all values from the main function to calculate the shore level using satellite uplift of Uc.

**main():** Calls all functions beginning with the user-defined inputs. It also establishes a value of 1.2 for ΔU, representing the "static" climatic sea level rise present from 1890 to 2000. After calling all the functions for the inputs, Main() performs three calculations: the uncertainty value, the shore level according to marographs, and the shore level according to satellites. Finally, the code prints the average mareographic and satellite shore levels, followed by the uncertainty value. Creating a separate function to calculate the average of both mareographic and satellite shore levels did not seem necessary.
