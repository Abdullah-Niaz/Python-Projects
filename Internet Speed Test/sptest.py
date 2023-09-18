import speedtest

st = speedtest.Speedtest()

download = st.download()
upload = st.upload()

download_mbps = round(download/10**6, 2)
upload_mbps = round(upload/10**6, 2)

print("Download Speed is : {} Mbps ".format(download_mbps))
print("Upload Speed is: {} Mbps".format(upload_mbps))
