import os

def createprojectdir(dirname):
    if not os.path.exists(dirname):
        print("Creating Director " + dirname)
        os.makedirs(dirname)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

def write_file(path, data):
    f = open(path, 'w')
    f.writelines(data)
    f.close()

def append_to_file(path, data):
    with open(path, 'a') as file:
        file.writelines(data + '\n')
        file.close()

def delete_file_contents(path):
    with open(path, 'w'):
        pass

def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
        return results

def set_of_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)

