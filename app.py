from trend import get_google_trends
from script import generate_script
from video import create_video_with_text
from insta import upload_video_to_insta

def bot_workflow():
    print("Bot started...")
    
    # 1. Get trending topics
    topics = get_google_trends()
    print("Trending Topics:", topics)
    
    for topic in topics:
        # 2. Generate a script
        script = generate_script(topic)
        print(f"Generated script for '{topic}':\n", script)
        
        # 3. Create a video
        video_file = f"{topic.replace(' ', '_')}"
        create_video_with_text(script, video_file)
        print(f"Video created: {video_file}")
        
        # 4. Upload video
        upload_video_to_insta(topic,video_file)
        print(f"Uploaded video for topic: {topic}")

    print("Bot finished its work for today!")

bot_workflow()

