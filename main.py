import instaloader
from instaloader import Instaloader, Profile

L = instaloader.Instaloader()

PROFILE = input("Enter the instagram profile name: ")
profile = Profile.from_username(L.context, PROFILE)

posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda post: post.likes, reverse=True)

for post in posts_sorted_by_likes:
	L.download_post(post, PROFILE)
