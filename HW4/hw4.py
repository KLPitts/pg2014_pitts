# Katie Pitts
# HW 4
# Create a netcdf file of output from wave simulation in HW 3.

import numpy as np
import netCDF4
import hw3Wave


# Define initial conditions for wave
H = 10.0 # meters
dt = 50.0 # seconds, note CFL condition: dx/dt = B(g*H)^0.5, B = some constant
dx = 500.0 # meters
N = 5000 # no. of grid points to step through
t = 10000 # no. of time points to step through
x = np.arange(0.0, N*dx, dx) # meters
time = np.arange(0.0, t*dt, dt) # seconds
N_eta = N - 1 # one less x space for eta
x_eta = np.arange(0.0, N_eta*dx, dx) # meters

# initialize eta as height of H
eta = np.zeros((t,N_eta)) + H # meters

# adding a step function as my bump
eta[0,1000:1999] = H + 1.0

# call wave class
wavet = hw3Wave.wave(H, dt, dx, N, t)
u_t, eta_t = wavet.solve(eta)

# create netcdf file from output
nc = netCDF4.Dataset('WaveOutput.nc', 'w')
nc.author = 'Pitts'

nc.createDimension('x', N)
nc.createDimension('x_eta', N_eta)
nc.createDimension('time', t)

nc.createVariable('x', 'd', ('x',))
nc.variables['x'][:] = x
nc.variables['x'].units = 'meters'

nc.createVariable('x_eta', 'd', ('x_eta',))
nc.variables['x_eta'][:] = x_eta
nc.variables['x_eta'].units = 'meters'

nc.createVariable('time', 'd', ('time',))
nc.variables['time'][:] = t
nc.variables['time'].units = 'seconds'

nc.createVariable('eta', 'd', ('time','x_eta'))
nc.variables['eta'][:] = eta_t
nc.variables['eta'].units = 'meters'

nc.createVariable('u', 'd', ('time','x'))
nc.variables['u'][:] = u_t
nc.variables['u'].units = 'meters/second'

nc.close()