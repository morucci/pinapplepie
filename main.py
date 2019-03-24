import github3
import json

def get_repo_info(gh, _repo):
    try:
        repo = gh.repository(_repo.owner, _repo.name)
    except github3.exceptions.ForbiddenError:
        return
    info = {
        'id': repo.id,
        'name': repo.name,
        'url': repo.url,
        'stars': repo.stargazers_count,
        'html_url': repo.html_url
    }
    return info


def main():
    count = 0
    gh = github3.github.GitHub(token='')
    # https://api.github.com/search/repositories?q=stars:>=500+is:public+fork:false+archived:false
    # See total_count
    for _repo in gh.search_repositories(
            query='stars:>50000 is:public fork:false archived:false'):
        info = get_repo_info(gh, _repo.repository)
        count += 1
        with open('data.json', 'a+') as fd:
            fd.write(json.dumps(info)+'\n')
            fd.flush()
        print("%s registered" % count)
        
main()
