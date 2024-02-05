import requests
def upload_large_file(access_token, file_path,message):
    try:
        # Open the file and get its size
        with open(file_path, "rb") as file:
            file_size = len(file.read())

            print(int(file_size))

        # Initialize the upload session
        
        params = {
            "access_token": access_token,
            "description":message,
            "upload_phase": "start",
            "file_size": file_size,
        }
        response = requests.post("https://graph.facebook.com/v17.0/me/videos", params=params)
        response_data = response.json()

        if "video_id" not in response_data:
            print(f"Error starting upload: {response_data['error']['message']}")
            return

        # Get the video ID and upload session ID
        video_id = response_data["video_id"]
        upload_session_id = response_data["upload_session_id"]

        # Perform chunked uploads
        chunk_size =  50*1024 * 1024  # 4 MB chunks
        offset = 0
        while int(offset) < file_size:
            chunk = min(chunk_size, file_size - offset)
            params = {
                "access_token": access_token,
                "description":message,
                "upload_phase": "transfer",
                "start_offset": offset,
                "upload_session_id": upload_session_id,
            }

            # Read the chunk from the file
            with open(file_path, "rb") as file:
                file.seek(offset)
                chunk_data = file.read(chunk)

            files = {
                "video_file_chunk": chunk_data
            }

            response = requests.post("https://graph.facebook.com/v17.0/me/videos", params=params, files=files)
            response_data = response.json()

            if "start_offset" in response_data:
                # Offset was returned, continue from the returned offset
                offset = response_data["start_offset"]
            elif "video_id" in response_data:
                # Successfully uploaded the chunk
                offset += chunk
            else:
                print(f"Error uploading chunk: {response_data['error']['message']}")
                return

        # Finish the upload
        params = {
            "access_token": access_token,
            "description":message,
            "upload_phase": "finish",
            "upload_session_id": upload_session_id,
        }
        response = requests.post("https://graph.facebook.com/v17.0/me/videos", params=params)
        response_data = response.json()
        print(response_data)

        if "video_id" not in response_data:
            print(f"Error finishing upload: {response_data['error']['message']}")
            return

        print("Upload completed successfully!")
    except requests.RequestException as e:
        print(f"Error during upload: {e}")


if __name__ == "__main__":
    # Replace this variable with your own access token
    access_token = "EAAEafQqhaTgBO4eykX8vXvUlsD0rfo6O5gJciONDWf0Lj4tfX9DPLDVHMDuqVPqpwXWw0EmlGJjjULOJ2KOEdwq2j1tTO12C1XEsX2gf73xZAoKdHVsNa9kN4vU7lJbuUP5DnqWcH2QLC9gfsXcrILjZC17Xjf6C4zpfNvDzPVAt6f1nodpZA5eCX0L8J1QwNFs2qt4PHOy3tRurhPZCNk3FjFihWvgBpJ9jnxQZD"

    # Replace this variable with the path to the large file you want to upload
    file_path = "d:\Global Project\connectifyindia\public\media\short_video2.mp4"
    message="भेजना चाहते हैं हिंदी में मैसेज लेकिन नहीं आती टाइपिंग? इन आसान Tips से मोबाइल से भेजें हिंदी में टेक्स्ट मैसेज"

    upload_large_file(access_token, file_path,message)