#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# exercises-day4.py

"""
Created on Thu Mar 19 10:56:36 2026

@author: geoffreydesena
"""

# %% Exercise 1 - Testing code with py.test
# a. Installed pytest

# b. Write a test for simple_math.py
# 
'''
============================= test session starts ==============================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: /Users/geoffreydesena/Documents/advc-python/day4-bestpractices-2
plugins: anyio-4.10.0
collected 10 items                                                             

lecture_code/pytest/test_fib.py .                                        [ 10%]
lecture_code/pytest/test_fib_params.py ...                               [ 40%]
test_simple_math.py ......                                               [100%]

============================== 10 passed in 0.02s ==============================
'''

# %% Exercise 2 - documenting code
# a. Write docstrings for the functions in simple_math.py

# Docstrings added to simple_math.py


# b. Create a webpage using Sphinx
# html file created: docs/_build/html/index.html

# %% Exercise 3 - Plotting with matplotlib
# a. Clicked through the notebook

# b. Matplotlib

# This is actually where I have found genAI most helpful.
# When I'm designing a plot, I don't want to get wrapped up in the syntax
# of the code. I just want to visualize my ideal plot and then describe what I
# see. ChatGPT has been fantastic for translating my description into a 
# plot using matplotlib.

# The details of what Chat created for me and how I prompted it are in
# exercise-3b.py

from exercise3b import make_vchar_pload_plot, prepare_plot_data

# Option 1: create the plot directly
df_plot, fig, axs = make_vchar_pload_plot(
    wind_pickle_path="hourly_windspeeds_by_wp.pkl",
    pload_pickle_path="Pload_series.pkl",
    wp_key="wp5"
)

# Option 2: just prepare the aligned dataframe
df_plot = prepare_plot_data(
    wind_pickle_path="hourly_windspeeds_by_wp.pkl",
    pload_pickle_path="Pload_series.pkl",
    wp_key="wp5"
)

print(df_plot.head())



# %% Exercise 4 - Fitting datasets
import numpy as np

# load data
measured = np.load("I_q_IPA_exp.npy")
modeled = np.load("I_q_IPA_model.npy")

# Again, I've leveraged chatGPT. I'll never code again...

import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

# Load data
measured = np.load("I_q_IPA_exp.npy")
modeled = np.load("I_q_IPA_model.npy")

# Split into q and intensity
q_exp = measured[:, 0]
I_exp = measured[:, 1]

q_model = modeled[:, 0]
I_model = modeled[:, 1]

# Remove NaNs from experimental data
valid = ~np.isnan(I_exp)
q_exp_valid = q_exp[valid]
I_exp_valid = I_exp[valid]

# Build interpolation function for the model
# Use only the q-range where interpolation is valid
model_interp = interp1d(q_model, I_model, kind='linear', bounds_error=False, fill_value=np.nan)

# Interpolate model onto experimental q values
I_model_on_exp = model_interp(q_exp_valid)

# Keep only points where interpolation returned valid numbers
valid_interp = ~np.isnan(I_model_on_exp)
q_fit = q_exp_valid[valid_interp]
I_exp_fit = I_exp_valid[valid_interp]
I_model_fit = I_model_on_exp[valid_interp]

# Define objective function: sum of squared residuals
def objective(scale):
    residuals = I_exp_fit - scale * I_model_fit
    return np.sum(residuals**2)

# Minimize with respect to scale factor
result = minimize_scalar(objective)
best_scale = result.x

print("Best scale factor:", best_scale)
print("Minimum objective value:", result.fun)

# Scaled model for plotting
I_model_scaled = best_scale * I_model_fit

# Plot
plt.figure(figsize=(8, 5))
plt.plot(q_fit, I_exp_fit, 'o', label='Experimental data', markersize=4)
plt.plot(q_fit, I_model_scaled, '-', label=f'Scaled model (scale={best_scale:.4g})', linewidth=2)

plt.xlabel("Scattering vector q")
plt.ylabel("Scattering strength I(q)")
plt.title("Experimental vs Scaled Theoretical Model")
plt.legend()
plt.grid(True)
plt.show()

