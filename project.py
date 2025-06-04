def get_mean_sea_level():
    regions={"Gulf of Bothnia": 0.2, "Gulf of Finland": 0.2, "Baltic Proper": 0.1, "Kattegat": 0.0}
    for area in regions:
        print(area)
    region=input("Baltic Sea region:")
    if region in regions:
        H0=regions[region]
    return H0

def get_Ua():
    Ua=float(input("Mareograph uplift in mm/yr:"))
    return Ua

def get_Uc():
    Uc=float(input("Satellite uplift in mm/yr:"))
    return Uc

def get_time():                     #get the year for shorelevel calculation
    t=int(input("Year between 500-2000CE:"))
    return t

def calculate_exponential_uplift(Uc, t):    #the exponential uplift per periods
    Exponential_uplift={}
    for year in range(1501,2001):
        Exponential_uplift[year]=0.0*(Uc/6)
    for year in range(1201,1501):
        Exponential_uplift[year]=0.1*(Uc/6)
    for year in range(1001,1201):
        Exponential_uplift[year]=0.2*(Uc/6)
    for year in range(801,1001):
        Exponential_uplift[year]=0.3*(Uc/6)
    for year in range(651,801):
        Exponential_uplift[year]=0.4*(Uc/6)
    for year in range(500,651):
        Exponential_uplift[year]=0.5*(Uc/6)
        if t in Exponential_uplift:
            E=Exponential_uplift[t]
            return E

def calculate_uncertainty_value(t):
    uncertainty_value=(0.2*(2000-1700)+0.3*(1700-t))/1000
    return uncertainty_value

def calculate_shorelevel_mareograph(Ua, ΔU, t, E, H0):
    shorelevel_mareograph =Ua*(2000-1890)/1000 + (Ua + ΔU)*(1890-t)/1000 + E + H0
    return shorelevel_mareograph

def calculate_shorelevel_satellite(Uc, ΔU, t, E, H0):
    shorelevel_satellite=(Uc-ΔU)*(2000-1890)/1000 + Uc*(1890-t)/1000 + E + H0
    return shorelevel_satellite


def main():
    try:
        H0=get_mean_sea_level()
        Ua=get_Ua()
        Uc=get_Uc()
        t=get_time()
        E=calculate_exponential_uplift(Uc, t)
        ΔU=1.2
        uncertainty_value=calculate_uncertainty_value(t)
        shorelevel_mareograph=calculate_shorelevel_mareograph(Ua, ΔU, t, E, H0)
        shorelevel_satellite=calculate_shorelevel_satellite(Uc, ΔU, t, E, H0)
        print(f"Shore level: {round(((shorelevel_mareograph+shorelevel_satellite)/2), 2)}m, ±{round(uncertainty_value, 2)}m")
    except (TypeError, UnboundLocalError, ValueError):
        print("invalid input")

if __name__ == "__main__":
    main()
