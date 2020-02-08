import json

def return_profile():
	"""Return author's bio"""
	
	profile = {
		'name': 'Agus Richard Lubis',
		'age': 22,
		'address': 'Depok, Jawa Barat',
		'hobbies': ['Stargazing', 'Reading', 'Writing', 'Coding'],
		'is_married': False,
		'list_school': [
			{
				'name': 'SDN 1 Depok Jaya',
				'year_in': 2003,
				'year_out': 2009,
				'major': None
			},
			{
				'name': 'SMPN 2 Depok',
				'year_in': 2009,
				'year_out': 2012,
				'major': None
			},
			{
				'name': 'SMAN 1 Depok',
				'year_in': 2012,
				'year_out': 2015,
				'major': 'Natural Science'
			}
		],
		'skills': [
			{
				'skill_name': 'Web Development',
				'level': 'beginner'
			},
			{
				'skill_name': 'Data Science',
				'level': 'beginner'
			},
			{
				'skill_name': 'Machine Learning',
				'level': 'beginner'
			},
		],
		'interest_in_coding': True
	}

	return json.dumps(profile)

print(return_profile())