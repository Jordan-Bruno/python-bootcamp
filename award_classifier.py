# takes average module marks, project marks, and the % of the
# final mark that is based on the module marks
# E.g. if the course is 180-credits, with 90 credits from modules
# and 90 credits from project, PMA_split = 0.5


def award_classifier(PMA_average, proj_marks, PMA_split):
	pmas = PMA_average * PMA_split
	proj = proj_marks * (1 - PMA_split)
	final = pmas + proj
	if final < 50:
		return "Fail"
	elif final < 60:
		return "Pass"
	elif final < 70:
		return "Merit"
	else:
		return "Distinction"