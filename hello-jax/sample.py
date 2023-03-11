import jax.numpy as jnp
from jax import grad, jit, vmap 
from jax import random 
import time


key = random.PRNGKey(0)
x = random.normal(key, (10,))
print(x)


# multiplying two matrices by finding the dot product 

size = 3000
x = random.normal(key, (size, size), dtype=jnp.float32)

start = time.time()
result = jnp.dot(x, x.T).block_until_ready()
print(result)
end = time.time()
print("Total time elapsed is : ", end - start)
