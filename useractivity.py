import requests


def get_activities(user):
    activity =   requests.get(f'https://api.github.com/users/{user}/events')
    return activity.json() if activity.status_code == 200 else None


try:
    user = str(input('which user would you like to view activity? '))
    activities = get_activities(user)
    if activities == None:
        raise NameError
except NameError:
    print('User not found ')

else:
    print('user found ')
    print('These are the latests events from {user}')
    for i in activities:
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
    


