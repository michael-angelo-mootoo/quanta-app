from thermo import Chemical
from scipy.optimize import brentq


def adiabatic_flame_temperature():
    # Reactants at 298.15 K (25°C)
    ch4 = Chemical('methane', T=298.15)
    o2 = Chemical('oxygen', T=298.15)

    # Enthalpy of formation (kJ/mol)
    H_R = 1 * (ch4.Hf / 1000) + 2 * (o2.Hf / 1000)  # H_R = -74.873 kJ

    # Function to compute H_P - H_R at temperature T (K)
    def enthalpy_error(T):
        try:
            # Products at temperature T
            co2 = Chemical('CO2', T=T)
            h2o = Chemical('water', T=T, phase='g')  # Gaseous H2O

            # Reference state at 298.15 K for Δh calculation
            co2_ref = Chemical('CO2', T=298.15)
            h2o_ref = Chemical('water', T=298.15, phase='g')

            # Sensible enthalpy change (kJ/mol)
            delta_h_co2 = (co2.H - co2_ref.H) / 1000
            delta_h_h2o = (h2o.H - h2o_ref.H) / 1000

            # Total enthalpy of products (kJ)
            H_P = 1 * (co2.Hf / 1000 + delta_h_co2) + 2 * (h2o.Hf / 1000 + delta_h_h2o)
            error = H_P - H_R
            print(f"T={T} K, Error={error:.2f} kJ")  # Debug output
            return error
        except Exception as e:
            print(f"Error at T={T} K: {e}")
            return float('inf')

    # Use bracketing method (root lies between 5200 and 5400 K)
    T_adiabatic = brentq(enthalpy_error, 5200, 5400, xtol=1, maxiter=100)
    return T_adiabatic


# Calculate and print the result
T_flame = adiabatic_flame_temperature()
print(f"Adiabatic Flame Temperature: {T_flame:.1f} K")