import requests

url = 'https://labour.gov.in/sites/default/files/mpr_february_2024.pdf'
response = requests.get(url)

if response.status_code == 200:
    f = open("Monthlyprogressreport.pdf", "wb")
    f.write(response.content)
    f.close()
else:
    print("Error")

# Note1: In  labour.gov.in only Monthlyprogress report question is correct.

# Note2: In labour.gov.in after clicking media there is no submenu whose name is  photo gallery option not available,
# so the second Question is wrong.

