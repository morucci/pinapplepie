from github3 import github

def main():
    gh = github.GitHub(token='')
    for _repo in gh.all_repositories(number=10000, per_page=10):
        repo = gh.repository(_repo.owner, _repo.name)
        if repo.archived:
            print("%s skipped as archived" % repo.name)
            continue
        if repo.parent:
            print("%s skipped as forked" % repo.name)
            continue
        if repo.stargazers_count <= 500:
            print("%s skipped as star < 500" % repo.name)
            continue
        print("Name: %s, Star: %s, Url: %s" % (
            repo.name,
            repo.stargazers_count,
            repo.html_url,
            )
        )

main()
