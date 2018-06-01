from pgmpy.models import BayesianModel
import pandas as pd
import numpy as np
from pgmpy.factors.discrete import TabularCPD


def create_model():
	edges_list = [('cebolla', 'distensionAbdominal'),
				  ('cebolla', 'borborigmos'),
				  ('cafe', 'reflujoGastroesofagico'),
				  ('cafe', 'dolorAbdominal'),
				  ('frijol', 'distensionAbdominal'),
				  ('frijol', 'flatulencia'),
				  ('aji', 'sintomasDispepsicos'),
				  ('aji','dolorAbdominal'),
				  ('leche', 'diarrea'),
				  ('leche', 'intolerancia'),
				  ('tomate', 'intolerancia'),
				  ('te','estrenimiento'),
				  ('manzana','borborigmos')]
	model = BayesianModel(edges_list)
	nodes = {'avena': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'aji': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'albahaca': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'apio': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'brocoli': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'coco': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'fresa': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'limon': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'lucuma': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'mango': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'maracuya': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'naranja': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'manzana': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'almendras': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'arroz': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'cafe': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'cebolla': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'res': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'pan': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'huevo': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'jamon': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'leche': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'lechuga': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'papa': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'platano': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'pollo': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'queso': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'te': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'tomate': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'frijol': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'distensionAbdominal': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'flatulencia': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'dolorAbdominal': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'estrenimiento': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},						
			'diarrea': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},						
			'intolerancia': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},
			'borborigmos': {'States': {'bajo', 'medio','alto'},
						'type': 'discrete'},					
						}
	model.add_nodes_from(nodes)


	cpds = [{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'albahaca':  []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'apio':      []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'brocoli':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'coco':      []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'fresa':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'limon':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'lucuma':    []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'mango':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'maracuya':  []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'naranja':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'manzana':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'almendras': []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'arroz':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'cafe':      []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'cebolla':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'res':       []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'pan':       []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'huevo':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'jamon':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'leche':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'lechuga':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'lentejas':  []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'palta':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'pavo':      []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'papa':      []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'platano':   []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'aji':       []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'pollo':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'queso':     []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'te':        []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'tomate':    []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'yogurt':    []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'zanahoria': []}},
			{'Values': np.array([[0.3], [0.4],[0.3]]),'Variables': {'frijol':    []}}]

	tabular_cpds = []
	for cpd in cpds:
		var = list(cpd['Variables'].keys())[0]
		evidence = cpd['Variables'][var]
		values = cpd['Values']
		states = len(nodes[var]['States'])
		evidence_card = [len(nodes[evidence_var]['States'])
						 for evidence_var in evidence]
		tabular_cpds.append(
			TabularCPD(var, states, values, evidence, evidence_card))

	model.add_cpds(*tabular_cpds)	


	cpd_distension = TabularCPD(variable='distensionAbdominal', variable_card=3,
							values=[[0.6, 0.3,0.1,0.65, 0.3,0.05,0.65, 0.3,0.05],
									[0.2, 0.3,0.5,0.25, 0.4,0.35,0.05, 0.3,0.65],
									[0.2, 0.4,0.4,0.1, 0.3,0.60,0.3, 0.4,0.3]],
							evidence=['cebolla','frijol'],
							evidence_card=[3, 3])  

	cpd_intolerancia = TabularCPD(variable='intolerancia', variable_card=3,
							values=[[0.6, 0.3,0.1,0.65, 0.3,0.05,0.65, 0.3,0.05],
									[0.2, 0.3,0.5,0.25, 0.4,0.35,0.05, 0.3,0.65],
									[0.2, 0.4,0.4,0.1, 0.3,0.60,0.3, 0.4,0.3]],
							evidence=['leche', 'tomate'],
							evidence_card=[3, 3])  
	cpd_borborigmos = TabularCPD(variable='borborigmos', variable_card=3,
							values=[[0.6, 0.3,0.1,0.65, 0.3,0.05,0.65, 0.3,0.05],
									[0.2, 0.3,0.5,0.25, 0.4,0.35,0.05, 0.3,0.65],
									[0.2, 0.4,0.4,0.1, 0.3,0.60,0.3, 0.4,0.3]],
							evidence=['manzana','cebolla'],
							evidence_card=[3, 3])  
	cpd_estren = TabularCPD(variable='estrenimiento', variable_card=3,
							values=[[0.15, 0.3,0.55],
									[0.65, 0.3,0.05],
									[0.2, 0.4,0.4]],
							evidence=['te'],
							evidence_card=[3]) 
	cpd_reflujo = TabularCPD(variable='reflujoGastroesofagico', variable_card=3,
							 values=[[0.15, 0.3,0.55],
									[0.65, 0.3,0.05],
									[0.2, 0.4,0.4]],
							evidence=['cafe'],
							evidence_card=[3]) 
	cpd_flat = TabularCPD(variable='flatulencia', variable_card=3,
							values=[[0.15, 0.3,0.55],
									[0.65, 0.3,0.05],
									[0.2, 0.4,0.4]],
							evidence=['frijol'],
							evidence_card=[3, 3])  
	cpd_dolor = TabularCPD(variable='dolorAbdominal', variable_card=3,
							values=[[0.6, 0.3,0.1,0.65, 0.3,0.05,0.65, 0.3,0.05],
									[0.2, 0.3,0.5,0.25, 0.4,0.35,0.05, 0.3,0.65],
									[0.2, 0.4,0.4,0.1, 0.3,0.60,0.3, 0.4,0.3]],
							evidence=['cafe','aji'],
							evidence_card=[3, 3])  

	cpd_diarrea = TabularCPD(variable='diarrea', variable_card=3,
						   values=[[0.15, 0.3,0.55],
									[0.65, 0.3,0.05],
									[0.2, 0.4,0.4]],
							evidence=['leche'],
							evidence_card=[3, 3])  				
							
	model.add_cpds(cpd_distension, cpd_sintDisp, cpd_intolerancia, cpd_estren, cpd_borborigmos,cpd_reflujo,cpd_dolor,cpd_flat,cpd_diarrea)
	model.check_model()
	return model
