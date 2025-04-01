from city_functions import places
def test_city_country():
    get_correct_name=places('santiago','chile')
    assert get_correct_name=='santiago, chile'

# Run pytest in the terminal to execute tests
# Specify the folder to the pytest command in case of multiple 
# tests like pytest city/