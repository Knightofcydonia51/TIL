import boto3
import os
import csv
import traceback

# boto3를 사용하기 위해 선언해주는 변수들
# 참고: NCP Python SDK For Object Storage https://guide.ncloud-docs.com/docs/storage-storage-8-2
service_name = 's3'
endpoint_url = 'https://kr.object.gov-ncloudstorage.com'
region_name = 'kr-standard'

# NCP API 인증키
access_key = '652FF60F064FFB4DA6F1'
secret_key = '20B38778EE5B343FD3C2F2BA13DCC6701C0038BC'

# Log파일 남기기 위한 csv 파일 생성
f = open('log.csv','w', newline='')
wr=csv.writer(f)

# 번호
n=0

# 로컬 경로, 버킷명, 버킷상에서 업로드할 경로
local_directory, bucket, destination = 'test35/','kigepe-edu-was-object-stor-01','test35/' 

# NCP에서 boto3쓸때 선언해줘야하는 값
client = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,aws_secret_access_key=secret_key)

# os에서 탐색하고 있는 현재 경로, 탐색한 현재 경로에 존재하는 디렉토리(list,string), 탐색한 현재 경로에 존재하는 파일들(list,string)
for root, dirs, files in os.walk(local_directory):
    # 파일 순회
    for filename in files:
        
        n+=1 
        
        # root와 filename을 결합하여 하나의 경로명으로 저장
        local_path = os.path.join(root, filename)

        # os상에서의 현재 탐색중인 파일의 상대경로
        relative_path = os.path.relpath(local_path, local_directory)
        
        # 목적지, 상대경로 인자로 받아서 최종적으로 저장될 버킷의 경로로 결합하여 저장
        s3_path = os.path.join(destination, relative_path).replace("\\","/")
        
        # print("s3_path: ", s3_path)
        # print('Searching {0} in {1}'.format(s3_path, bucket))
        # print('Uploading....{filename}'.format(filename=filename))
        
        # 이미 존재하는 디렉토리 업로드시 스킵하는 기능
        try:
            client.head_object(Bucket=bucket, Key=s3_path)
            
            # print("Path found on S3! Skipping {0}...".format(s3_path))
            # try:
                # client.delete_object(Bucket=bucket, Key=s3_path)
            # except:
                # print "Unable to delete %s..." % s3_path
        except:
            try:
                # 업로드
                client.upload_file(local_path, bucket, s3_path)
                # 로그 쓰기
                wr.writerow([n, filename, s3_path])
            
            #에러 발생시 에러 저장
            except:
                err = traceback.format_exc()
                wr.writerow([n, filename, s3_path,'ERROR',err])


