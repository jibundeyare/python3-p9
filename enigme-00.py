from timeit import default_timer as timer

# start benchmark
start = timer()

# votre code ici

# stop benchmark
end = timer()
duration = end - start
print('duration:', duration)
