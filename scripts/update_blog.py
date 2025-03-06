import feedparser
import git
import os

# 벨로그 RSS 피드 URL
rss_url = 'https://api.velog.io/rss/@Hy25u'

# 깃허브 레포지토리 경로
repo_path = '.'

# 'velog-posts' 폴더 경로
posts_dir = os.path.join(repo_path, 'velog-posts')

# 'velog-posts' 폴더가 없다면 생성
if not os.path.exists(posts_dir):
    os.makedirs(posts_dir)

# 레포지토리 로드
repo = git.Repo(repo_path)

# GitHub Actions 환경에서 PAT 가져오기
github_token = os.getenv('GH_PAT')  # GitHub Actions의 Secret에서 PAT 가져오기
remote_url = f"https://x-access-token:{github_token}@github.com/cheonhy25u/velog_study.git"

# RSS 피드 파싱
feed = feedparser.parse(rss_url)

# 각 글을 파일로 저장하고 커밋
for entry in feed.entries:
    file_name = entry.title.replace('/', '-').replace('\\', '-') + '.md'
    file_path = os.path.join(posts_dir, file_name)

    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(entry.description)

        # 깃허브 커밋
        repo.git.add(file_path)
        repo.git.commit('-m', f'Add post: {entry.title}')

# Git 인증을 `GH_PAT`로 설정한 후 Push
origin = repo.remote(name='origin')
origin.set_url(remote_url)  # 원격 저장소 URL을 PAT 방식으로 변경
repo.git.push('origin', 'main')
