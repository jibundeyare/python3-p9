from timeit import default_timer as timer

# start benchmark
start = timer()

for _ in range(0, 100000):
    # votre code ici
    pass

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
