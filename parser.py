import requests

def parse():
    with open(create_new_file(), 'a') as parsed_file:
        filepath = 'html/index.html'
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            parsed_file.write("const char index_web[] = ")
            while line:
                raw = line.strip()
                raw = raw.replace("\"", "\'")
                parsed_file.write("\"" + raw + "\"\n") # encapsulate each line with ""
                if raw == "<style>":
                    find_inject = get_css().replace("\"", "\'")
                    find_inject = find_inject.replace("\"", "\'")
                    parsed_file.write("\"" + find_inject + "\"\n")

                if raw == "<script>":
                    find_inject = get_js().replace("\"", "\'")
                    find_inject = find_inject.replace("\"", "\'")
                    parsed_file.write("\"" + find_inject + "\"\n")

                line = fp.readline()
                cnt += 1
            parsed_file.write(";\n")

def create_new_file():
    filename = "index_web.c"
    f = open(filename, "w+")
    f.close()
    return filename

def get_css():
    with open('css/index.css', 'r') as file:
        line = requests.post('https://cssminifier.com/raw', data=dict(input=file.read())).text
        return line
    return ""

def get_js():
    with open('js/index.js', 'r') as file:
        line = requests.post('https://javascript-minifier.com/raw', data=dict(input=file.read())).text
        return line
    return ""

parse()
