import csv
import boto3

#call your s3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('acr-ec2-description')
key = 'ec2description.csv'

ec2 = boto3.resource('ec2')

# creates the csv file
with open('/tmp/ec2description.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # creates the header
    header = ['InstanceID', 'State', 'InstanceType', 'SG_ID', 'SG_Name', 'SG_Inbound', 'SG_Outbound']

    # write the header
    writer.writerow(header)

    # collect the data for writing to csv file
    for instance in ec2.instances.all():
        for sg in ec2.security_groups.all():
            if sg.id == instance.security_groups[0]['GroupId']:
                permissionsIN = sg.ip_permissions
                permissionsOUT = sg.ip_permissions_egress
                print('==========PROCESSANDO===========')

        #creates the header
        data = [instance.id, instance.state['Name'], instance.instance_type, instance.security_groups[0]['GroupId'], instance.security_groups[0]['GroupName'], permissionsIN, permissionsOUT]

        # write the data to csv file
        writer.writerow(data)

#upload the data into s3
bucket.upload_file('/tmp/ec2description.csv', key)
