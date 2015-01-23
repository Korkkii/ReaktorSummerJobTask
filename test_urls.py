import requests

urls = ["http://facebook.com/whoisthis",
        "http://github.com/Korkkii",
        "http://fi.linkedin.com/in/korhonenhenri",
        "foo.bar/baz/bar"]
ids = []

for url in urls:
    response = requests.post("http://localhost:8080/shorten", data=url)
    ids.append(response.text)
    print(response.text)
    print(response)

urls.append("foo.baz/baaaarr")
ids.append("notthisone")

for i in [0, 1, 2, 3]:
    response = requests.get("http://localhost:8080/{0}".format(ids[i]), )
    print(response)




