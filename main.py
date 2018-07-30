import transforms as tr
import numpy as np

theta = tr.params([0, 0, 180])
a = np.array([0.5, 0.5, 0.5, 1])

print(tr.affineTransform(a,theta,[2, 1, 1]))