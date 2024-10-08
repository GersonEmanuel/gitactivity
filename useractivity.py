import requests

user = str(input('Digite o nome do usuario: '))
url =   f'https://api.github.com/users/{user}/events'
activity = requests.get(url)
for i in activity.json():
    if i['type'] == 'IssueCommentEvent':
        print(f"- {user}: commented on issue {i['payload']['issue']['number']}")
    elif i['type'] == 'PushEvent':
        print(f"- {user}: pushed to {i['repo']['name']}")
    elif i['type'] == 'IssuesEvent':
        print(f"- {user}: created issue {i['payload']['issue']['number']}")
    elif i['type'] == 'WatchEvent':
        print(f"- {user}: starred {i['repo']['name']}")
    elif i['type'] == 'PullRequestEvent':
        print(f"- {user}: created pull request {i['payload']['pull_request']['number']}")
    elif i['type'] == 'PullRequestReviewEvent':
        print(f"- {user}: reviewed pull request {i['payload']['pull_request']['number']}")
    elif i['type'] == 'PullRequestReviewCommentEvent':
        print(f"- {user}: commented on pull request {i['payload']['pull_request']['number']}")
    elif i['type'] == 'CreateEvent':
        print(f"- {user}: created {i['payload']['ref_type']} {i['payload']['ref']}")
    else:
        print(f"- {user}: {i['type']}")
    


