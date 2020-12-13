import numpy as np 
from .Base_skinterface import BaseSKI
from tods.detection_algorithm.PyodMoGaal import Mo_GaalPrimitive

class Mo_GaalSKI(BaseSKI):
	def __init__(self, **hyperparams):
		super().__init__(primitive=Mo_GaalPrimitive, **hyperparams)

