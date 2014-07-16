from videos.models import VideoDetails, UserDetails

def getHomePageValues():
	videos = VideoDetails.objects.all()
	videosList = []
	for i in videos:
		videosList.append(i.videoID)

	return videosList
