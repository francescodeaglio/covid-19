import os

root_data_path = os.path.join(
	os.path.dirname(os.path.dirname(__file__)), "data"
)

raw_cases_paths_dict = {
	"italy": os.path.join(
		root_data_path,
		"raw", "cases", "italy",
		"COVID-19"
	),
}

norm_cases_paths = os.path.join(
	root_data_path,
	"norm", "cases",
)

root_figures_path = os.path.join(
	os.path.dirname(os.path.dirname(__file__)), "figures"
)
os.makedirs(root_figures_path, exist_ok=True)