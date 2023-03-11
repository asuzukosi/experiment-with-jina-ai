import jax.numpy as jnp
from jax import grad, jit, vmap 
from jax import random
import time


key = random.PRNGKey(0)

def selu(x, alpha=1.67, lmbda=1.05):
      return lmbda * jnp.where(x > 0, x, alpha * jnp.exp(x) - alpha)

x = random.normal(key, (1000000,))

# measure time elapsed using regular selu function
start = time.time()
selu(x).block_until_ready()
stop = time.time()

print("time elapsed using regular selu is ", stop - start)


# convert selu function to use jax
selu_jit = jit(selu)
start = time.time()
selu_jit(x).block_until_ready()
stop = time.time()

print("time elapsed using jit selu is ", stop - start)