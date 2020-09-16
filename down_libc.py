import requests
import sys
import lxml.html
import os

# code_names = ['xenial', 'bionic']

if len(sys.argv) < 2:
    print('usage: {} <version> [codename]'.format(sys.argv[0]))
    print('example: {} 2.23-0ubuntu5 xenial'.format(sys.argv[0]))
    exit(0)

version = sys.argv[1]

os.chdir(os.path.dirname(os.path.abspath(__file__)))

if len(sys.argv) > 2:
    code_name = sys.argv[2]
else:
    if sys.argv[1].startswith('2.23'):
        code_name = 'xenial'
    elif sys.argv[1].startswith('2.23'):
        code_name = 'bionic'
    else:
        print('{}: unable to detect codename!'.format(sys.argv[0]))
        exit(0)

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

def get_package_deb(package, code_name, version):
    url = 'https://bugs.launchpad.net/ubuntu/{}/amd64/{}/{}'.format(code_name, package, version)

    print('accessing: {}'.format(url))
    res = requests.get(url)

    if res.status_code != requests.codes.ok:
        print('not 200 while accessing the page.')
        exit(0)

    root = lxml.html.fromstring(res.content)

    down_link = root.xpath('//*[@id="downloadable-files"]/ul/li/a')

    if len(down_link) != 1:
        print(res.text)
        print('failed to find download link !')
        exit(0)

    down_link = down_link[0].attrib['href']

    print('get download link for libc: {}'.format(down_link))

    return download_file(down_link)


get_package_deb('libc6', code_name, version)
get_package_deb('libc6-dbg', code_name, version)

os.system("./merge-libc {} {}".format(version, version))
