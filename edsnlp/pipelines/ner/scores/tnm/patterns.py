prefix_pattern = r"(?P<prefix>[cpPyraum]p?)?"

#Tumour pattern must have at least size or spec (no match with TNM)
tumour_pattern = (r"T\s?(?:"
 r"(?P<tumour>([0-4o]|is))(?P<tumour_specification>[abcdx]|mi)|" # Tumour size and tumour spec
 r"(?P<tumour>([0-4o]|is))|" # Tumour size but no tumour spec
 r"(?P<tumour_specification>[abcdx]|mi))" # No Tumour size but tumour spec
                  r"(?:\s?\((?P<tumour_suffix>[^()]{1,10})\))?" # get parenthesis content after T)
                 )

node_pattern = (
    r"(?:[cpPyraum]p?)?N\s?(?P<node>[0-3o]|x)" #get number after N
    r"(?P<node_specification>[abcdx]|mi)?" #get letter after Nx
    r"(?:\((?P<node_suffix>[^()]{1,10})\))?" #get parenthesis content after p
)

metastasis_pattern = (
    r"M\s?(?P<metastasis>([01o]|x))x?"
    r"(?P<metastasis_specification>[abcdx])?" #get letter after Nx
)
pleura_pattern = r"PL\s?(?P<pleura>([0123]|x))" #For lung cancer 
resection_completeness = r"R\s?(?P<resection_completeness>[012])"

version_pattern = (
    r"\(?(?P<version>uicc|accj|tnm|UICC|ACCJ|TNM)"
    r"\s+([éeE]ditions|[éeE]d\.?)?\s*"
    r"(?P<version_year>\d{4}|\d{2})\)?"
)

spacer = r"(.|\n){1,5}"
TNM_space = r"(\s*[,\/]?\s*)?" #allow comma between TNM (eg: "pT1b, N0, R0")

exclude_pattern = r"(?!\s*T\s?[0-9]\s*(?![abcdx]?N))" # Exclude  matchs with T1, T2 , T 1, etc ...
# exclude_pattern = ""
tnm_pattern = f"(?<={version_pattern}{spacer})?"
tnm_pattern += prefix_pattern + r"\s*" + f"({tumour_pattern})"
tnm_pattern += TNM_space+ f"({node_pattern})?"
tnm_pattern += TNM_space+ f"({metastasis_pattern})?"
tnm_pattern += TNM_space+ f"({pleura_pattern})?"
tnm_pattern += TNM_space+ f"({resection_completeness})?"
tnm_pattern += f"({spacer}{version_pattern})?"
tnm_pattern = r"(?:\b|^)" + exclude_pattern+ tnm_pattern + r"(?:\b|$)"
 