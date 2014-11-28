# Katie Pitts
# HW 3
#
# See square_wave.mp4 for animation of example code.
# Used a "square" wave to show the difficulty in numerically
# propagating a step function.

import numpy as np
import matplotlib.pyplot as plt

class wave(object):
	""" Class to propagate a wave given some distribution of eta.
	User must provide initial conditions for:
	eta:  water surface with a bump
	H:  water surface height
	dt:  time interval
	dx:  space interval
	N:  No. of grid points
	t:  No. of time points"""

	def __init__(self, H, dt, dx, N, t):

		# Define constants and initial conditions
		self.g = 9.8 # m/s^2
		self.H = H
		self.N = N
		self.dt = dt
		self.dx = dx
		self.t = t


	def solve(self, eta):
		# initialize u as zeros
		u = np.zeros((self.t,self.N)) # m/s
		
		# Calculate new u and eta values with each time step
		for t in range(self.t - 1):
			u[t+1,1:-1] = u[t,1:-1] - self.g * self.dt/self.dx * ( eta[t,1:] - eta[t,:-1] )
			eta[t+1,:] = eta[t,:] - self.H * self.dt/self.dx * ( u[t+1,1:] - u[t+1,:-1] )
					
		return u, eta

	
if __name__ == '__main__':
	H = 10.0 # meters
	dt = 100.0 # seconds, note CFL condition: dx/dt = B(g*H)^0.5, B = some constant
	dx = 1000.0 # meters
	N = 10000 # no. of grid points to step through
	t = 15000 # no. of time points to step through
	x = np.arange(0.0, N*dx, dx) # meters
	# initialize eta as height of H
	eta = np.zeros((t,(N-1))) + H # meters
	# add a bump
	eta[0,1000:1999] = H + 1.0
	#eta[0,:] = H + np.sin(x[:-1]*np.pi/2000000.0)
	wavet = wave(H, dt, dx, N, t)
	u_t, eta_t = wavet.solve(eta)
	
	timestep = np.arange(0,t-1,t/4)
	f, ax = plt.subplots(4, sharex=True, sharey=True)
	for n in range(4):
		ax[n].plot(eta_t[timestep[n],:],label='eta (m)')
		ax[n].plot(u_t[timestep[n],:],label='u (m/s)')
		ax[n].set_title('Time step ' +str(timestep[n]), fontsize='10')
		ax[0].legend(loc='center right', fontsize='10')
	plt.ylim((-2,12))
	plt.xlabel('x (m)')
	plt.show()
	
	print "See square_wave.mp4 for animation of example code."
	
	"""
	# The following code was used to make the frames of the animation
	
	fig = plt.figure(figsize=(10,7))
	
	for t in range(0,t-1,200):
	#for t in range(1):
		plt.clf()
		p1 = plt.plot(eta_t[t,:],label='eta (m)')
		p2 = plt.plot(u_t[t,:],label='u (m/s)')
		plt.xlabel('x (m)')
		plt.ylabel('eta (m); u (m/s)')
		plt.ylim((-2,12))
		plt.legend(loc='center right')
		#plt.show()
		plt.savefig('frames2/frame_%05d.png' % t, dpi=300)"""