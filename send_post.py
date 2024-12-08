import requests

test_requests = [{'f_name1': '12.03.2012',
                  'f_name2': '+7 984 656 48 54',
                  'f_name3': 'asd@asd.com'
                  },
                 {'f_name1': 'asd@asd.com',
                  'f_name2': '+7 984 656 48 54',
                  'f_name3': 'asdasd.com'
                  },
                 {'f_name1': 'asd@asd.com',
                  'f_name2': '12.03.2012',
                  'f_name3': 'some text'
                  },
                 {'f_name1': '12.03.2012',
                  'f_name2': '+7 984 656 48 54',
                  'f_name3': 'asdasd.com'
                  },
                 {'f_name1': 'asd@asd.com',
                  'f_name2': 'some text',
                  'f_name3': '12.03.2012'
                  },
                 ]

for test_request in test_requests:
    r = requests.post('http://127.0.0.1:5000/post',
                      data=test_request
                      )
    print(r.text)
