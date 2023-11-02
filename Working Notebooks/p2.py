y0 = np.array([2.0])
N_steps_vector = [16,32,64]

for isteps, N_steps in enumerate(N_steps_vector) :

    logistic_integrator.N_time_steps = N_steps
    logistic_integrator.calculate_solution(y0)

    h = logistic_integrator.delta_t
    if isteps > 0 :
        # Need to take every other entry for the finer resolution
        # so the size of the vectors match
        diff = logistic_integrator.y_solution[::2] - old_solution
        plt.plot(
            logistic_integrator.t_solution[::2],
            diff,
            label="error between h = " + str(h) + " and h = " + str(h/2)
        )
        if isteps == 1 :
            plt.plot(
                logistic_integrator.t_solution[::2],
                diff / order,
                '--',
                label="expected High/Medium error"
            )
    old_solution = logistic_integrator.y_solution

plt.grid()
plt.legend()
plt.ylabel("Solution error")
plt.xlabel("t");